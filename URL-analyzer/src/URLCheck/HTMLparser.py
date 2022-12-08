from bs4 import BeautifulSoup
import requests

class HTMLparser():
    """
        This class will resolve information about
        HTML attributes that the website has
        ex add to the parse function:
        if websiteData["favicon"] != None:
            self.URLinfo.favicon = True
    """
    def __init__(self, URLinfo = None):
        self.URLinfo = URLinfo

    def parse(self):
        """
            This function get information from the HTML on the website

            input: URLinfo object, output: updated URLinfo object
        """
        try: #kolla om vi kan få HTML info från websida
            if self.URLinfo.protocol == None:
                response = requests.get("https://" + self.URLinfo.url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects = True, timeout = 3)
            else:
                response = requests.get(self.URLinfo.url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects = True, timeout = 3)
            if response.history:
                for webPage in response.history:
                    self.fetchFaviconInfo(webPage.text)
            while response.next:
                self.fetchFaviconInfo(response.next.text)
            self.fetchFaviconInfo(response.text)
        except Exception as e:
            self.URLinfo.errors.append(f"Error during HTML info collecting, connection failed.")
            return self.URLinfo
        return self.URLinfo

    def fetchFaviconInfo(self, responseInfo):
        """
            Collects info about websites favicon, to my knowledge, favicon info exist in in html tags: link and meta

            input: response info from HTML request, output:
        """
        self.URLinfo.favicon = False # default is False, if function find information about favicon -> True
        extDocs = []
        for doc in BeautifulSoup(responseInfo, "html.parser").find_all('link'):
            if "rel" in doc.attrs.keys():
                if "icon" in doc.attrs["rel"]:
                    self.URLinfo.favicon = True
            if "href" in doc.attrs.keys():
                if "favicon" in doc.attrs["href"] or ".ico" in doc.attrs["href"]:
                    self.URLinfo.favicon = True
            if "id" in doc.attrs.keys():
                if "favicon" in doc.attrs["id"] or ".ico" in doc.attrs["id"]:
                    self.URLinfo.favicon = True
        for doc in BeautifulSoup(responseInfo, "html.parser").find_all("meta"):
            if "content" in doc.attrs.keys():
                if ".ico" in doc.attrs["content"] or "favicon" in doc.attrs["content"]:
                    self.URLinfo.favicon = True
        for doc in BeautifulSoup(responseInfo, "html.parser").find_all("img"):
            if "src" in doc.attrs.keys():
                if ".ico" in doc.attrs["src"] or "favicon" in doc.attrs["src"]:
                    self.URLinfo.favicon = True
