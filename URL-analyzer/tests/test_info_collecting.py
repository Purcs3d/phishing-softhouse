import pytest
import src.URLCheck.URLinfo as urlinfo
import src.URLCheck.stringParser as stringparser
import src.URLCheck.HTMLparser as htmlparser
import src.URLCheck.DNSresolver as dnsresolver

"""
    This is a testing file for all kinds of info collecting on the URL
    run:
    pytest -s
    in this file's directory to run tests, or:
    pytest -s test_info_collecting.py::test_HTMLparser
    for testing individual tests.
"""

@pytest.fixture
def URLinfoObj():
    """
        This function just always returns a URLinfo object to skip redundant code
    """
    return urlinfo.URLinfo("http://scanme.nmap.org/")
@pytest.fixture
def URLstringParser(URLinfoObj):
    return stringparser.stringParser(URLinfoObj)
@pytest.fixture
def urlDNSresolver(URLinfoObj):
        return dnsresolver.DNSresolver(URLinfoObj)
@pytest.fixture
def urlHTMLparser(URLinfoObj):
        return htmlparser.HTMLparser(URLinfoObj)

def test_stringParser(URLstringParser):
    print("Testing subdomain and path info")
    URLstringParser.URLinfo.url = "https://cloud.timeedit.net/bth/web/sched1/file.html"
    URLinfoObj = URLstringParser.UrlResolver()
    assert URLinfoObj.subDomain == "cloud"
    assert URLinfoObj.domain == "timeedit"
    assert URLinfoObj.topDomain == "net"
    assert URLinfoObj.path == "/bth/web/sched1/file.html"
    assert URLinfoObj.dir == "/bth/web/sched1/"
    assert URLinfoObj.file == "file.html"

def test_DNSresolver(urlDNSresolver, URLstringParser):
    print("Testing DNS resolving info on gp.se")
    URLstringParser.URLinfo.url = "gp.se"
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlDNSresolver.resolve()
    assert URLinfoObj.country == "Sweden"
    assert URLinfoObj.city == "Mölnlycke"
    assert URLinfoObj.region == "Västra Götaland"
    # assert URLinfoObj.domainAge == "13 years" etc


def test_HTMLparser(urlHTMLparser, URLstringParser):
    print("Testing Favicon info on karlskronahem.se (False atm)")
    URLstringParser.URLinfo.url = "karlskronahem.se"
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlHTMLparser.parse()
    assert URLinfoObj.favicon == False

#integration test
def test_URLinfoCollecting(URLinfoObj, urlDNSresolver, urlHTMLparser, URLstringParser):
    print("Testing integration test with URL: http://scanme.nmap.org/")
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlDNSresolver.resolve()
    URLinfoObj = urlHTMLparser.parse()
    assert URLinfoObj.subDomain == "scanme"
    assert URLinfoObj.domain == "nmap"
    assert URLinfoObj.topDomain == "org"
    assert URLinfoObj.country == "United States"
    assert URLinfoObj.city == "Fremont"
    assert URLinfoObj.region == "California"
    assert URLinfoObj.favicon == True
