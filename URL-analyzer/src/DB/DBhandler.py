
import psycopg2
import src.config as config
from pathlib import Path

class DBhandler():
    """
        This class will handle all requests to a database.
    """
    def __init__(self, URLinfo = None):
        self.conn = psycopg2.connect(
           database=config.DB,
            user=config.DB_USERNAME,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            port= config.DB_PORT
        )
        self.URLinfo = URLinfo
        self.cursor = self.conn.cursor()

    def delDB(self):
        sql_str = "DROP SCHEMA IF EXISTS URLanalyzer CASCADE;"
        self.cursor.execute(sql_str)
        self.conn.commit()


    def initDB(self):
        sql_str = "CREATE SCHEMA IF NOT EXISTS URLanalyzer;"
        self.cursor.execute(sql_str)
        sql_str = "CREATE TABLE IF NOT EXISTS URLanalyzer.whitelist (ID 	SERIAL 	PRIMARY KEY, URL TEXT);"
        self.cursor.execute(sql_str)
        sql_str = "CREATE TABLE IF NOT EXISTS URLanalyzer.previousSearches (ID 	SERIAL 	PRIMARY KEY,searchDate DATE DEFAULT CURRENT_DATE,URL TEXT,report json,fishy BOOLEAN);"
        self.cursor.execute(sql_str)
        sql_str = """CREATE OR REPLACE FUNCTION oldSearchesFunc()
          RETURNS TRIGGER
          LANGUAGE PLPGSQL
          AS
        $$
        BEGIN
        	delete from urlanalyzer.previoussearches
        	where CURRENT_DATE  :: timestamp  -  searchDate :: timestamp > interval '3 days';
        	RETURN NULL;
        END;
        $$"""
        self.cursor.execute(sql_str)
        sql_str = """create or replace trigger removeOldSearches
        before insert on urlanalyzer.previoussearches
        EXECUTE PROCEDURE oldSearchesFunc();"""
        self.cursor.execute(sql_str)
        self.conn.commit()
        self.init_createWhitelist() #if it doesnt exist, checked in function

    def init_createWhitelist(self):
        sql_str = "select count(*) from URLanalyzer.whitelist;"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone()[0] != 0: # Whitelist already exist
            return
        else: #white list doesnt exist:
            dataFolder = Path("../src/DB/")
            filename = dataFolder / "whitelist.txt"
            with open(filename) as file:
                for line in file:
                    sql_str = f"INSERT INTO URLanalyzer.whitelist (URL) VALUES ('{line.rstrip()}');"
                    self.cursor.execute(sql_str)
                self.conn.commit()

    def checkURLinWhitelist(self):
        """
            Checks if URL exist in whitelist
            input: URL, output: if it exist(True) or not (False)
        """
        url = self.URLinfo.domain +"."+ self.URLinfo.topDomain
        if self.URLinfo.subDomain != None and self.URLinfo.subDomain != "www.":
            # sql_str = f"select * from URLanalyzer.whitelist where url LIKE '%{self.URLinfo.domain}%' AND '%{self.URLinfo.topDomain}';"
            # above str buggy for many links like:
            # https://answers.microsoft.com/en-us/windows/forum/all/whois-command-not-working-for-windows-10/3a77075e-606c-41be-9f6b-2cde13c2fe95
            # blog.facebook.com
            # and doesnt pick up links as "blog.google.se" as whitelist
            sql_str = f"select * from URLanalyzer.whitelist where url LIKE '%{url}';"
        else:
            sql_str = f"select * from URLanalyzer.whitelist where url = '{url}';"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone() == None:
            return False
        else:
            return True

    def checkURLinpreviousSearches(self):
        """
            Checks if URL exist in previousSearches table
            input: URL, output: if it exist(True) or not (False)
        """
        sql_str = f"select * from URLanalyzer.previousSearches where url = '{self.URLinfo.url}';"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone() == None:
            return False
        else:
            sql_str = f"Select CURRENT_DATE  :: timestamp  -  searchDate :: timestamp from urlanalyzer.previoussearches where url = '{self.URLinfo.url}';"
            self.cursor.execute(sql_str)
            date = self.cursor.fetchone()[0]
            if date.days > 3: # if previous search is older than 3 days -> return false anyways.
                return False
            return True
    def fetchPreviousSearchReport(self):
        """
            Fetches report from a url found in previousSearches table.
            ! Used in combination with the function checkURLinpreviousSearches !
            input: URL, output: report of previously searched URL
        """
        sql_str = f"select report from URLanalyzer.previousSearches where url = '{self.URLinfo.url}';"
        self.cursor.execute(sql_str)
        return self.cursor.fetchone()[0]
    def fetchPreviousSearchPhishiness(self):
        """
            Fetches boolean that holds if a URL is fishy/not fishy from a url found in previousSearches table.
            ! Used in combination with the function checkURLinpreviousSearches !
            input: URL, output: bool
        """
        sql_str = f"select fishy from URLanalyzer.previousSearches where url = '{self.URLinfo.url}';"
        self.cursor.execute(sql_str)
        return self.cursor.fetchone()[0]
    def fetchPreviousSearchDate(self):
        """
            Fetches datetime that holds if a URL is fishy/not fishy from a url found in previousSearches table.
            ! Used in combination with the function checkURLinpreviousSearches !
            input: URL, output: bool
        """
        sql_str = f"Select searchDate from urlanalyzer.previoussearches where url = '{self.URLinfo.url}';"
        self.cursor.execute(sql_str)
        # date = self.cursor.fetchone()[0]
        return self.cursor.fetchone()[0]

    def insertIntopreviousSearches(self, url, report, fishy):
        """
            This function inserts a url into the database
            There is a trigger in the database that deletes url searches older than 3 days after insert
            input: URL, and its report
        """
        sql_str = f"INSERT INTO URLanalyzer.previousSearches (URL, report, fishy) VALUES ('{url}', '{report}', {fishy});"
        self.cursor.execute(sql_str)
        self.conn.commit()

# DB STRING:
        """
CREATE SCHEMA IF NOT EXISTS URLanalyzer;

CREATE TABLE IF NOT EXISTS URLanalyzer.whitelist (
	ID 	SERIAL 	PRIMARY KEY,
	URL TEXT
);

CREATE TABLE IF NOT EXISTS URLanalyzer.previousSearches (
	ID 	SERIAL 	PRIMARY KEY,
	searchDate DATE DEFAULT CURRENT_DATE,
	URL TEXT,
	report TEXT,
    fishy BOOLEAN
);

CREATE OR REPLACE FUNCTION oldSearchesFunc()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
    delete from urlanalyzer.previoussearches
    where CURRENT_DATE  :: timestamp  -  searchDate :: timestamp > interval '3 days';
    RETURN NULL;
END;
$$
create trigger removeOldSearches
before insert on urlanalyzer.previoussearches
EXECUTE PROCEDURE oldSearchesFunc();

drop function if exists oldSearchesFunc;
drop trigger if exists removeOldSearches;

-- drop table urlanalyzer.whitelist;
-- truncate table urlanalyzer.whitelist;
-- SELECT * FROM URLanalyzer.whitelist;
-- INSERT INTO URLanalyzer.whitelist (URL)
-- VALUES ('youtube.com');
-- DROP SCHEMA IF EXISTS URLanalyzer CASCADE;
        """
