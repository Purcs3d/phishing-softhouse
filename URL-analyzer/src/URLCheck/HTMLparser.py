from requests_html import HTMLSession

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

    def parse(self): #Lukas function
        """
            This function get information from the HTML on the website

            input: URLinfo object, output: updated URLinfo object
        """
        session = HTMLSession()
        request = session.get(self.URLinfo.url)
        print(dir(request.html))
        # print(request.html.raw_html)
        links = request.html.find("link")
        # print(dir(request.html.element("link")))
        # print(request.html.element("link").show)
        for link in links:
            if "favicon.ico" in link.attrs["href"]: #might be buggy on some website
                self.URLinfo.favicon = True
        return self.URLinfo


        # try:
        #     requestInfo = http.request('GET', self.URLinfo.url) # fetch http data
        # except Exception as e:
        #     self.URLinfo.errors.append(e)
        #     return self.URLinfo
