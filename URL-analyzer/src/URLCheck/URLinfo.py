import src.URLCheck.DNSresolver as DNSresolver
import src.URLCheck.HTMLparser as HTMLparser
import src.URLCheck.stringParser as stringParser


class URLinfo():
    """
        This class acts as a struct and holds all information we have about the URL

        It collects all information about the URL via the collectInfo() function

        if you want to add something:
        ex:
        self.favicon : Boolean = False
        Then under HTMLparser.py:
        if websiteData["favicon"] != None:
            self.URLinfo.favicon = True
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
        self.favicon : Boolean = None
        self.errors : List = [] # the error messages collected during information gathering

    def getDNSinfo(self):
        """ update URLinfo object with DNS information"""
        urlDNSresolver = DNSresolver.DNSresolver(self)
        self = urlDNSresolver.resolve()

    def getURLstringInfo(self):
        """ update URLinfo object with URLstring information """
        URLstringParser = stringParser.stringParser(self)
        self = URLstringParser.UrlResolver()

    def getHTMLinfo(self):
        """ update URLinfo object with HTML attribute information """
        urlHTMLparser = HTMLparser.HTMLparser(self)
        self = urlHTMLparser.parse()

    def collectInfo(self):
        """Extract all kind of information we can get from the URL """
        self.getDNSinfo()
        self.getURLstringInfo()
        self.getHTMLinfo()

    def generateReport(self):
        """
            This function adds all variablenames and their values in a report
            ex report = ['country: Sweden', 'region: Blekinge']
        """
        report = []
        for a, v in self.__dict__.items():
            report.append(a + ": " + str(v))
        return report
