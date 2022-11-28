import pytest
import src.DB.DBhandler as dbhandler
import src.URLCheck.URLinfo as urlinfo

"""
    This is a testing file for all kinds of Database integration problems
    run:
    pytest -s
    in this file's directory to run all tests, or e.g.:
    pytest -s test_checklists_evaluation.py
    pytest -s test_checklists_evaluation.py::test_string_checklist
    for testing individual tests.

    ! Assumption: Whitelist is initialized !
"""

def test_selects():
    print("Tests to see if simple SELECT query works")
    URLinfoObj = urlinfo.URLinfo("http://test.org/")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    sql_str = "select * from URLanalyzer.previousSearches;"
    DBhandlerObj.cursor.execute(sql_str)

def test_checkWhitelist():
    print("Checking if URLs exist in whitelist")
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
    print("Checking if URL not exist in previousSearches table")
    URLinfoObj = urlinfo.URLinfo("alskdjdauodiuhwahdksjdjasldksakdas.se")
    URLinfoObj.getURLstringInfo()
    DBhandlerObj = dbhandler.DBhandler(URLinfoObj)
    assert DBhandlerObj.checkURLinpreviousSearches() == False
