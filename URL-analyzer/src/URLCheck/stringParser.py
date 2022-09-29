from urllib.parse import urlparse

class stringParser():
    """
        The stringParser Class has one function in it
        It's job is to parse the url and resolve infomration from it
    """

    def __init__(self, URLinfo):
        self.URLinfo = URLinfo

    def UrlResolver(self):
        parse = urlparse(self.URLinfo.url)
        self.URLinfo.urlName = parse.netloc # t ex www.google.com
        self.URLinfo.protocol = parse.scheme # HTTP eller HTTPS
        self.URLinfo.path = parse.path # t ex /auth/login
        self.URLinfo.params = parse.params # No longer used, always empty
        self.URLinfo.query = parse.query # everything after ? in the url before the #
        self.URLinfo.fragment = parse.fragment # evrything after # in the back of the url
        return self.URLinfo
