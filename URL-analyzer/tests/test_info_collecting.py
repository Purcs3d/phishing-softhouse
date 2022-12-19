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
    pytest -s test_info_collecting.py
    pytest -s test_info_collecting.py::test_HTMLparser
    for testing individual tests.
"""

@pytest.fixture
def URLinfoObj():
    """
        This function just always returns a URLinfo object to skip redundant code
        Called in parameter for the tests functions
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
    print("\nTesting subdomain and path info")
    URLstringParser.URLinfo.url = "https://cloud.timeedit.net/bth/web/sched1/file.html"
    URLinfoObj = URLstringParser.UrlResolver()
    assert URLinfoObj.subDomain == "cloud"
    assert URLinfoObj.domain == "timeedit"
    assert URLinfoObj.topDomain == "net"
    assert URLinfoObj.path == "/bth/web/sched1/file.html"
    assert URLinfoObj.dir == "/bth/web/sched1/"
    assert URLinfoObj.file == "file.html"

def test_DNSresolver(urlDNSresolver, URLstringParser):
    print("\nTesting DNS resolving info on gp.se 2022-12")
    URLstringParser.URLinfo.url = "gp.se"
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlDNSresolver.resolve()
    assert URLinfoObj.country == "Sweden"
    assert URLinfoObj.city == "Mölnlycke"
    assert URLinfoObj.region == "Västra Götaland"
    assert str(URLinfoObj.registered) == "1994-05-31 00:00:00"


def test_HTMLparser(urlHTMLparser, URLstringParser):
    print("\nTesting Favicon info on some websites, done (2022-12)")
    URLstringParser.URLinfo.url = "svt.se"
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlHTMLparser.parse()
    assert URLinfoObj.favicon == True
    URLstringParser.URLinfo.url = "youtube.com"
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlHTMLparser.parse()
    assert URLinfoObj.favicon == True
    URLstringParser.URLinfo.url = "hltv.org" # in <img>
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlHTMLparser.parse()
    assert URLinfoObj.favicon == True
    URLstringParser.URLinfo.url = "https://cert.europa.eu/blog" # user agent mozilla
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlHTMLparser.parse()
    assert URLinfoObj.favicon == True
    URLstringParser.URLinfo.url = "https://archive.ics.uci.edu/ml/index.php" # not favicon atm(2022-12)
    URLinfoObj = URLstringParser.UrlResolver()
    URLinfoObj = urlHTMLparser.parse()
    assert URLinfoObj.favicon == False

#integration test
def test_URLinfoCollecting(URLinfoObj, urlDNSresolver, urlHTMLparser, URLstringParser):
    print("\nTesting integration test with URL: http://scanme.nmap.org/ 2022-12")
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
