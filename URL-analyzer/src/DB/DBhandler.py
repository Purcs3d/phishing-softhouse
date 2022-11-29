# https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application#step-1-creating-the-postgresql-database-and-user
import psycopg2
import src.config as config
from pathlib import Path

# att göra: kolla upp lösenord, och char(200) om det finns dynamisk
# kolla upp SQLinjection bibliotek
# om en URL i previousSearches är mer än 2 dagar gammal vid ny select -> ta bort, gör en trigger
# ändra whitelist till INSERT OR REPLACE ist för bara insert alla rader.

# Hur skall DB initializeras
# hur skall den tas bort??

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

    def __del__(self):
        self.conn.close()

    def delDB(self):
        sql_str = "DROP SCHEMA IF EXISTS URLanalyzer CASCADE;"
        self.cursor.execute(sql_str)
        self.conn.commit()


    def initDB(self):
        sql_str = "CREATE SCHEMA IF NOT EXISTS URLanalyzer;"
        self.cursor.execute(sql_str)
        sql_str = "CREATE TABLE IF NOT EXISTS URLanalyzer.whitelist (ID 	SERIAL 	PRIMARY KEY, URL TEXT);"
        self.cursor.execute(sql_str)
        sql_str = "CREATE TABLE IF NOT EXISTS URLanalyzer.previousSearches (ID 	SERIAL 	PRIMARY KEY,searchDate DATE DEFAULT CURRENT_DATE,URL TEXT,report TEXT,fishy BOOLEAN);"
        self.cursor.execute(sql_str)
        sql_str = """CREATE OR REPLACE FUNCTION oldSearchesFunc()
          RETURNS TRIGGER
          LANGUAGE PLPGSQL
          AS
        $$
        BEGIN
        	delete from urlanalyzer.previoussearches
        	where extract(day from CURRENT_DATE)- extract( day from searchDate) > 3;
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
	where extract(day from CURRENT_DATE)- extract( day from searchDate) > 3;
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

    def init_createWhitelist(self):
        sql_str = "select count(*) from URLanalyzer.whitelist;"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone()[0] != 0: # Whitelist already exist
            return
        else: #white list doesnt exist:
            dataFolder = Path("..\\src\\DB\\")
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
        # if self.URLinfo.subDomain != None and self.URLinfo.subDomain != "www.": # www.login.bth.se
        #     url = self.URLinfo.subDomain +"."+ self.URLinfo.domain +"."+ self.URLinfo.topDomain
        # else: # bth.se
        #     url = self.URLinfo.domain +"."+ self.URLinfo.topDomain
        # if url.startswith("www."):
        #     url = url[4:]
        url = self.URLinfo.domain +"."+ self.URLinfo.topDomain
        sql_str = f"select * from URLanalyzer.whitelist where url LIKE '%{url}%';"
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

    def insertIntopreviousSearches(self, url, report, fishy):
        """
            This function inserts a url into the database
            There is a trigger in the database that deletes url searches older than 3 days after insert
            input: URL, and its report
        """
        sql_str = f"INSERT INTO URLanalyzer.previousSearches (URL, report, fishy) VALUES ('{url}', '{report}', {fishy});"
        self.cursor.execute(sql_str)
        self.conn.commit()



    def test(self):
        # sql_str = "select * from URLanalyzer.whitelist"
        # self.cursor.execute(sql_str)
        # sql_str = "INSERT INTO URLanalyzer.previousSearches (URL, report) VALUES ('youtube.com', 'balls');"
        # self.cursor.execute(sql_str)
        sql_str = "select * from URLanalyzer.previousSearches;"
        self.cursor.execute(sql_str)
        for i in self.cursor.fetchall():
            print(i)


def testium():
    DBtester = DBhandler()
    # DBtester.init_createWhitelist()
    # DBtester.checkURLinWhitelist("svt.se")
    # DBtester.checkURLinWhitelist("medium.com")
    # DBtester.checkURLinWhitelist("medium.com/1231231 ta in subdomain+domain+topdomain")
    if DBtester.checkURLinpreviousSearches("svt.se"):
        print(DBtester.fetchPreviousSearchReport("svt.se"))
    # DBtester.test()

# testium()
