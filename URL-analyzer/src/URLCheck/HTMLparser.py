from bs4 import BeautifulSoup, SoupStrainer
import requests

class HTMLparser():
    """
        This class will resolve information about
        HTML attributes that the website has
        ex add to the parse function:
        if websiteData["favicon"] != None:
            self.URLinfo.favicon = True
    """
    def __init__(self, URLinfo):
        self.URLinfo = URLinfo

    def parse(self):
        """
            This function get information from the HTML on the website

            input: URLinfo object, output: updated URLinfo object
        """
        try: #kolla om vi kan få HTML info från websida
            if self.URLinfo.protocol == None:
                response = requests.get("http://" + self.URLinfo.url) #temporär lösning
            else:
                response = requests.get(self.URLinfo.url)
            self.fetchFaviconInfo(response)
        except Exception:
            self.URLinfo.errors.append(f"Error during HTML info collecting, connection failed.")
            return self.URLinfo
        return self.URLinfo

    def fetchFaviconInfo(self, responseInfo):
        """
            Collects info about websites favicon, to my knowledge, favicon info exist in in html tags: link and meta

            input: response info from HTML request, output:
        """
        self.URLinfo.favicon = False # default is False, if function find information about favicon -> True
        extDocs = responseInfo.html.find("link") #find all HTML tags called "link" -> results into a dictionary
        for doc in BeautifulSoup(response, parse_only=SoupStrainer('link')):
            if doc.has_attr('href') or doc.has_attr('rel') or doc.has_attr('id'):
                print(doc)
        # for doc in extDocs:
        #     if "rel" in doc.attrs.keys():
        #         if "icon" in doc.attrs["rel"]:
        #             self.URLinfo.favicon = True
        #     if "href" in doc.attrs.keys():
        #         if "favicon" in doc.attrs["href"] or ".ico" in doc.attrs["href"]:
        #             self.URLinfo.favicon = True
        #     if "id" in doc.attrs.keys():
        #         if "favicon" in doc.attrs["id"] or ".ico" in doc.attrs["id"]:
        #             self.URLinfo.favicon = True
        # extDocs = responseInfo.html.find("meta") #find all HTML tags called "meta" -> results into a dictionary
        # for doc in extDocs:
        #     if "content" in doc.attrs.keys():
        #         if ".ico" in doc.attrs["content"] or "favicon" in doc.attrs["content"]:
        #             self.URLinfo.favicon = True
