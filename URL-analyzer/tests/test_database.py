import pytest
import src.DB.DBhandler as dbhandler

"""
    This is a testing file for all kinds of evaluation done on URLs
    run:
    pytest -s
    in this file's directory to run all tests, or e.g.:
    pytest -s test_checklists_evaluation.py
    pytest -s test_checklists_evaluation.py::test_string_checklist
    for testing individual tests.
"""

@pytest.fixture
def DBhandlerObj():
    """
        This function just always returns a DBhandler object to skip redundant code
        Called in parameter for the tests functions
    """
    return dbhandler.DBhandler()

def test_selects(DBhandlerObj):
    sql_str = "select * from URLanalyzer.previousSearches;"
    DBhandlerObj.cursor.execute(sql_str)
    for i in DBhandlerObj.cursor.fetchall():
        print(i)
