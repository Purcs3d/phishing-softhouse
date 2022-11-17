# https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application#step-1-creating-the-postgresql-database-and-user
import psycopg2

class DBhandler():
    """
        This class will handle all requests to a database.
    """
    def __init__(self):
        self.conn = psycopg2.connect(
           database="URLanalyzer",
            user='postgres',
            password='root',
            host='localhost',
            port= '5432'
        )
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

-- SELECT * FROM URLanalyzer.whitelist;
-- INSERT INTO URLanalyzer.whitelist (URL)
-- VALUES ('youtube.com');
-- DROP SCHEMA IF EXISTS URL_analyzer CASCADE;
        """

    def test(self):
        sql_str = "select * from URLanalyzer.whitelist"
        self.cursor.execute(sql_str)
        # sql_str = "INSERT INTO URLanalyzer.previousSearches (URL, report) VALUES ('youtube.com', 'balls');"
        # self.cursor.execute(sql_str)
        sql_str = "select * from URLanalyzer.previousSearches"
        self.cursor.execute(sql_str)
        for i in self.cursor.fetchall():
            print(i)


def testium():
    DBtester = DBhandler()
    DBtester.test()

testium()
