from url_parser import get_url #pip install url-parser

class stringParser():
    """
        The stringParser Class has one function in it
        It's job is to parse the url and resolve information from it

        future: define a function that santize input here?
    """

    def __init__(self, URLinfo):
        self.URLinfo = URLinfo

    def UrlResolver(self):
        """
            This function extracts information from URL string
            info about ex: protocol, subdomain, domain etc
        """
        try:
            parse = get_url(self.URLinfo.url)
        except Exception as e:
            self.URLinfo.errors.append(f"Error during STRING parsing: {e}")
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
        self.URLinfo.query = parse.query
        return self.URLinfo

    def UnicodeCheker(self):
        for i in self.URLinfo.domain: 
            try:
                if(int(ord(i)) < 128 and int(ord(i)) > 0 ):    #Allow ascii table 128 
                    pass 
            except ValueError:
                return True
        return False