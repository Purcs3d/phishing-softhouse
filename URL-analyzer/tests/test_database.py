import pytest
import src.DB.DBhandler as dbhandler
import src.URLCheck.URLinfo as urlinfo

"""
    This is a testing file for all kinds of Database integration problems
    run:
    pytest -s
    in this file's directory to run all tests, or e.g.:
    pytest -s test_database.py
    pytest test_database.py::test_checkPreviousSearchesUpdate -s
    for testing individual tests.
"""

def test_delDB():
    print("\nTesting deleteing the URLanalyzer schema with all tables, function and trigger.")
    URLinfoObj = urlinfo.URLinfo("svt.se")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    DBhandlerObj.delDB()

def test_initDB():
    print("\nTesting creating the database with all tables, function and trigger.")
    URLinfoObj = urlinfo.URLinfo("alskdjdauodiuhwahdksjdjasldksakdas.se")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    DBhandlerObj.initDB()
    assert DBhandlerObj.checkURLinpreviousSearches() == False

def test_selects():
    print("\nTests to see if simple SELECT query works")
    URLinfoObj = urlinfo.URLinfo("http://test.org/")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    sql_str = "select * from URLanalyzer.previousSearches;"
    DBhandlerObj.cursor.execute(sql_str)

def test_checkWhitelist():
    print("\nChecking if URLs exist in whitelist")
    URLinfoObj = urlinfo.URLinfo("http://www.google.se/")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    assert DBhandlerObj.checkURLinWhitelist() == True # "google.se" in whitelist
    URLinfoObj = urlinfo.URLinfo("www.addons.mozilla.org")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    assert DBhandlerObj.checkURLinWhitelist() == True
    URLinfoObj = urlinfo.URLinfo("appleid.apple.com.akadns.net")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    assert DBhandlerObj.checkURLinWhitelist() == True # "google.se" in whitelist


def test_checkPreviousSearches():
    print("\nChecking if URL not exist in previousSearches table")
    URLinfoObj = urlinfo.URLinfo("alskdjdauodiuhwahdksjdjasldksakdas.se")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    assert DBhandlerObj.checkURLinpreviousSearches() == False

def test_checkPreviousSearchesUpdate():
    print("\nChecking if URL not exist in previousSearches table even though old one exist")
    URLinfoObj = urlinfo.URLinfo("https://www.hltv.org/")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    report = "reportie"
    fishy = False
    sql_str = f"INSERT INTO URLanalyzer.previousSearches (searchDate, URL, report, fishy) VALUES ('2022-11-02','{URLinfoObj.url}', '{report}', {fishy});"
    DBhandlerObj.cursor.execute(sql_str)
    DBhandlerObj.conn.commit()
    assert DBhandlerObj.checkURLinpreviousSearches() == False # sätter in den i DB, den är gammal -> ska ej finnas i previous searches
