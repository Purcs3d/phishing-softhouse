# https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application#step-1-creating-the-postgresql-database-and-user
import psycopg2

# att göra: kolla upp lösenord, och char(200) om det finns dynamisk
# kolla upp SQLinjection bibliotek
# om en URL i previousSearches är mer än 2 dagar gammal vid ny select -> ta bort, gör en trigger

class DBhandler():
    """
        This class will handle all requests to a database.
    """
    def __init__(self, URLinfo = None):
        self.conn = psycopg2.connect(
           database="URLanalyzer",
            user='postgres',
            password='root',
            host='localhost',
            port= '5432'
        )
        self.URLinfo = URLinfo
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def initDB(self):
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
	report TEXT
);


CREATE TABLE IF NOT EXISTS URLanalyzer.test (
	ID 	SERIAL 	PRIMARY KEY
);
select * from URLanalyzer.test;
select count(*) from urlanalyzer.test; -- if empy table -> 0
drop table URLanalyzer.test;

select * from urlanalyzer.previoussearches;

select * from urlanalyzer.previoussearches;

insert into urlanalyzer.previoussearches(URL, report)
VALUES ('youtube.com', 'report');

-- for each new insert, remove searches older than 3 days
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
after insert on urlanalyzer.previoussearches
EXECUTE PROCEDURE oldSearchesFunc();

drop function oldSearchesFunc;
drop trigger removeOldSearches;

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
        if self.cursor.fetchone()[0] != 0:
            print("Whitelist already exist")
            return
        else:
            with open("whitelist.txt") as file:
                for line in file:
                    sql_str = f"INSERT INTO URLanalyzer.whitelist (URL) VALUES ('{line.rstrip()}');"
                    self.cursor.execute(sql_str)
                self.conn.commit()

    def checkURLinWhitelist(self, url):
        """
            Checks if URL exist in whitelist
            input: URL, output: if it exist(True) or not (False)
        """
        sql_str = f"select * from URLanalyzer.whitelist where url LIKE '%{url}%';"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone() == None:
            print(f"Url not found in whitelist: {url}")
            return False
        else:
            return True

    def checkURLinpreviousSearches(self, url):
        """
            Checks if URL exist in previousSearches table
            input: URL, output: if it exist(True) or not (False)
        """
        sql_str = f"select * from URLanalyzer.previousSearches where url = '{url}';"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone() == None:
            print(f"Url not found in previousSearches: {url}")
            return False
        else:
            return True
    def fetchPreviousSearchReport(self, url):
        """
            Fetches report from a url found in previousSearches table.
            ! Used in combination with the function checkURLinpreviousSearches !
            input: URL, output: report of previously searched URL
        """
        sql_str = f"select report from URLanalyzer.previousSearches where url = '{url}';"
        self.cursor.execute(sql_str)
        return self.cursor.fetchone()[0]

    def insertIntopreviousSearches(self, url, report):
        """
            This function inserts a url into the database
            There is a trigger in the database that deletes url searches older than 3 days after insert
            input: URL, and its report
        """
        sql_str = f"INSERT INTO URLanalyzer.previousSearches (URL, report) VALUES ('{url}', '{report}');"
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

testium()
