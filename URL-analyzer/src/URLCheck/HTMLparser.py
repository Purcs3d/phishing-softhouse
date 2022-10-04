class HTMLparser:
    """
        This class will resolve information about
        HTML attributes that the website has
        ex add to the parse function:
        if websiteData["favicon"] != None:
            self.URLinfo.favicon = websiteData["favicon"]
    """
    def __init__(self, URLinfo):
        self.URLinfo = URLinfo

    def parse(self):
        return self.URLinfo
