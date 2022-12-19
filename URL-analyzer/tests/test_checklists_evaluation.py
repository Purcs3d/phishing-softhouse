import pytest
import src.URLCheck.URLinfo as urlinfo
import src.checklists.URLstringCL as URLCL
import src.checklists.HTMLdataCL as HTMLCL
import src.checklists.DNSdataCL as DNSCL
import src.checklists.DatabaseComparisonCL as DBCL

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
def URLinfoObj():
    """
        This function just always returns a URLinfo object to skip redundant code
        Called in parameter for the tests functions
    """
    return urlinfo.URLinfo("http://www.testtest.tes.testtttteerer.long.scanme.l0g1nnmap.ru/")

def test_string_checklist(URLinfoObj):
    print("\nTesting URL string evaluation with dodgy link")
    points = 0
    URLinfoObj.getURLstringInfo()
    URLCLobj = URLCL.URLstringCL(URLinfoObj)
    URLCLobj.numbersInDomain()
    assert points < URLCLobj.points #0,1
    points = URLCLobj.points
    URLCLobj.checkSpecialKeywords()
    assert points < URLCLobj.points #l0g1n
    points = URLCLobj.points
    URLCLobj.checkTopDomain()
    assert points < URLCLobj.points #.ru
    points = URLCLobj.points
    URLCLobj.checkUrlLength()
    assert points < URLCLobj.points #url length > config_BAD_URL_Length
    points = URLCLobj.points
    URLCLobj.checkNumberOfSubdomains()
    assert points < URLCLobj.points # bad number of subdomains
    points = URLCLobj.points


def test_DNS_checklist(URLinfoObj):
    print("\nTesting DNS evaluation")
    points = 0
    URLinfoObj.url = "www.gp.se"
    URLinfoObj.getURLstringInfo() # used to fetch DNS info
    URLinfoObj.getDNSinfo()
    DNSCLobj = DNSCL.DNSdataCL(URLinfoObj)
    assert  points <= DNSCLobj.runEvaluation()

def test_HTML_checklist(URLinfoObj):
    print("\nTesting HTML evaluation")
    points = 0
    URLinfoObj.url = "www.karlskronahem.se"
    URLinfoObj.getURLstringInfo() # used to fetch HTML info
    URLinfoObj.getHTMLinfo()
    HTMLCLobj = HTMLCL.HTMLdataCL(URLinfoObj)
    assert  points <= HTMLCLobj.runEvaluation() #site lacks favicon ATM 2022-12

def test_DB_checklist(URLinfoObj):
    print("\nTesting DB evaluation")
    pass

def test_full_evaluation(URLinfoObj):
    print("\nFull evaluation integration test")
    points = 0
    URLinfoObj.url = "https://ieeexplore-ieee-org.miman.bib.bth.se/Xplore/cookiedetectresponse.jsp"
    URLinfoObj.collectInfo()
    URLCLobj = URLCL.URLstringCL(URLinfoObj)
    DNSCLobj = DNSCL.DNSdataCL(URLinfoObj)
    HTMLCLobj = HTMLCL.HTMLdataCL(URLinfoObj)
    URLCLobj.checkUrlLength()
    assert points < URLCLobj.points #url length > config_BAD_URL_Length
    points = URLCLobj.points
    URLCLobj.checkNumberOfSubdomains()
    assert points < URLCLobj.points # bad number of subdomains
