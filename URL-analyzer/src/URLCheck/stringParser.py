import re
from url_parser import get_url #pip install url-parser
import src.URLCheck.URLinfo as URLinfo
class stringParser():
    """
        The stringParser Class has one function in it
        It's job is to parse the url and resolve information from it

        future: define a function that santize input here?
    """

    def __init__(self, URLinfo: "URLinfo"):
        self.URLinfo = URLinfo

    def UrlResolver(self):
        """
            This function extracts information from URL string
            info about ex: protocol, subdomain, domain etc
        """
        try:
            parse = get_url(self.URLinfo.url)
        except Exception:
            self.URLinfo.errors.append(f"Error during STRING parsing. Couldnt recognise URL format.")
            return self.URLinfo
        self.URLinfo.www = parse.www
        self.URLinfo.protocol = parse.protocol
        self.URLinfo.subDomain = parse.sub_domain
        self.URLinfo.domain = parse.domain
        self.URLinfo.topDomain = parse.top_domain
        self.URLinfo.dir = parse.dir
        self.URLinfo.file = parse.file
        self.URLinfo.path = parse.path
        self.URLinfo.fragment = parse.fragment
        return self.URLinfo

    def UnicodeCheker(self):
        for i in self.URLinfo.domain:
            try:
                if(int(ord(i)) < 128 and int(ord(i)) > 0 ):    #Allow ascii table 128
                    pass
            except ValueError:
                return True
        return False

    def port_specified(self):
        if re.search(':[0-9]{1,5}$', self.URLinfo.topDomain):
            return True
        return False
