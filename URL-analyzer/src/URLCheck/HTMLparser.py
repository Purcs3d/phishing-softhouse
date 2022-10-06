import urllib3
from html.parser import HTMLParser

class Webscraper(HTMLParser):
    """
        This class is required when working with the library imported:
        "from html.parser import HTMLParser"
    """
    def __init__(self):
        super().__init__()
        self.dict = {}
        self.links = []
        self.favicon = False

    def handle_starttag(self, tag, attrs):
        self.handle_links(tag, attrs)
        self.handle_favicon(tag, attrs)


    def handle_links(self, tag, attrs):
        """
            fetch hyperlinks from website
        """
        if tag == "a":
           for name,link in attrs:
               if name == "href" and link.startswith("http"):
                   self.links.append(link)

    def handle_favicon(self, tag, attrs):
        """
            fetch external documents
        """
        if tag == "link":
            pass
            # print(attrs)
            # for name, info in attrs:
            #     if name == "rel" and info == "icon":
            #         self.favicon = True





class HTMLparser():
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
        handler = Webscraper()
        http = urllib3.PoolManager()
        r = http.request('GET', self.URLinfo.url)
        # print("status:", r.headers) #X-XSS-Protection
        self.parse_headers(r.headers)
        # print("data:", r.data)
        # str = handler.feed(r.headers)
        handler.feed(r.data.decode())
        print("links on website:", handler.links)
        # print(handler.favicon)
        return self.URLinfo

    def parse_headers(self, headers_dict):
        if headers_dict["X-XSS-Protection"] == 0:
            self.URLinfo.XXS_protection = False
        else:
            self.URLinfo.XXS_protection = True
