import src.URLCheck.DNSresolver as DNSresolver
import src.URLCheck.HTMLparser as HTMLparser
import src.URLCheck.stringParser as stringParser


class URLinfo():
    """
        This class acts as a struct and holds all information we have about the URL
    """
    def __init__(self, url):
        self.url = url
        self.protocol : str  = None
        self.urlName: str = None
        self.path: str = None
        self.params: str = None
        self.query: str = None
        self.fragment: str = None
        self.ip: str = None
        self.city: str = None
        self.country: str = None
        self.region: str = None

    def getDNSinfo(self):
        urlDNSresolver = DNSresolver.DNSresolver(self)
        self = urlDNSresolver.resolve()

    def getURLstringInfo(self):
        URLstringParser = stringParser.stringParser(self)
        self = URLstringParser.UrlResolver()

    def getHTMLinfo(self):
        urlHTMLparser = HTMLparser.HTMLparser(self)
        self = urlHTMLparser.parse()

    def collectInfo(self):
        self.getURLstringInfo()
        self.getDNSinfo()
        self.getHTMLinfo()
        self.printInfo()

    def printInfo(self):
        print("url:",self.url)
        print("protocol:",self.protocol)
        print("urlName:",self.urlName)
        print("path:",self.path)
        print("params:",self.params)
        print("query:",self.query)
        print("fragment:",self.fragment)
        print("ip:",self.ip)
        print("city:",self.city)
        print("country:",self.country)
        print("region:",self.region)
