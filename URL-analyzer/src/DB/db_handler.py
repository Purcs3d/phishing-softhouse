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
	URL CHAR(200)
);

CREATE TABLE IF NOT EXISTS URLanalyzer.previousSearches (
	ID 	SERIAL 	PRIMARY KEY,
	searchDate DATE DEFAULT CURRENT_DATE,
	URL CHAR(200),
	report CHAR(200)
);


select * from urlanalyzer.previoussearches;

create or replace function checkAge(url char(200), curDate DATE default CURRENT_DATE)
returns bool
as $$
begin
	-- declare:
	declare oldDate DATE;

	Select searchDate
    select
    commit;
end;$$
language plpgsql

-- drop table urlanalyzer.whitelist;
-- truncate table urlanalyzer.whitelist;
-- SELECT * FROM URLanalyzer.whitelist;
-- INSERT INTO URLanalyzer.whitelist (URL)
-- VALUES ('youtube.com');
-- DROP SCHEMA IF EXISTS URLanalyzer CASCADE;
        """

    def init_createWhitelist(self):
        sql_str = "select count(url) from URLanalyzer.whitelist;"
        self.cursor.execute(sql_str)
        print(self.cursor.fetchone())
        # if self.cursor.fetchone()[0] == 0:
            # print("whitelist is empty")
        sql_str = "select count(url) from URLanalyzer.previousSearches;"
        self.cursor.execute(sql_str)
        print(self.cursor.fetchone())
        # if self.cursor.fetchone()[0] == 0:
            # print("previousSearches is empty")
        # with open("whitelist.txt") as file:
        #     for line in file:
        #         sql_str = f"INSERT INTO URLanalyzer.whitelist (URL) VALUES ('{line.rstrip()}');"
        #         self.cursor.execute(sql_str)
        #     self.conn.commit()

    def checkURLinWhitelist(self, url):
        sql_str = f"select * from URLanalyzer.whitelist where url LIKE '%{url}%';"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone() == None:
            print(f"Url not found in whitelist: {url}")

    def checkURLinpreviousSearches(self, url):
        sql_str = f"select * from URLanalyzer.previousSearches where url = '{url}';"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone() == None:
            print(f"Url not found in whitelist: {url}")
            return False
        else:
            return True



    def insertIntopreviousSearches(self, url, report):
        sql_str = f"select * from URLanalyzer.previousSearches where url = '{url}';"
        self.cursor.execute(sql_str)
        if self.cursor.fetchone() == None:
            print(f"Url not found in whitelist: {url}")
        else:
            pass
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
    DBtester.init_createWhitelist()
    DBtester.checkURLinWhitelist("svt.se")
    DBtester.checkURLinWhitelist("medium.com")
    DBtester.checkURLinWhitelist("medium.com/1231231 ta in subdomain+domain+topdomain")
    DBtester.checkURLinpreviousSearches("svt.se")
    DBtester.test()

testium()
