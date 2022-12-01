from bs4 import BeautifulSoup
import requests
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options

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
                response = requests.get("https://" + self.URLinfo.url) #temporär lösnin
            else:
                response = requests.get(self.URLinfo.url)
            # driver = webdriver.Firefox(executable_path='C:/Users/lukas/Downloads/Assignments/LP_1_H22/grupparbete/geckodriver.exe', log_path='C:/Users/lukas/Downloads/Assignments/LP_1_H22/grupparbete/phishing-softhouse/URL-analyzer/tests/Log/geckodriver.log')
            # driver.get(self.URLinfo.url)
            # response = requests.get(driver.current_url)
            # driver.quit()
            for webPage in response.history:
                self.fetchFaviconInfo(webPage.text)
            self.fetchFaviconInfo(response.text)
        except Exception as e:
            print(e)
            self.URLinfo.errors.append(f"Error during HTML info collecting, connection failed.")
            return self.URLinfo
        return self.URLinfo

    def fetchFaviconInfo(self, responseInfo):
        """
            Collects info about websites favicon, to my knowledge, favicon info exist in in html tags: link and meta

            input: response info from HTML request, output:
        """
        # extDocs = responseInfo.html.find("link") #find all HTML tags called "link" -> results into a dictionary
        self.URLinfo.favicon = False # default is False, if function find information about favicon -> True
        # for link in BeautifulSoup(responseInfo).find_all('a', href=True):
        #         print(link['href'])
        extDocs = []
        for doc in BeautifulSoup(responseInfo, "html.parser").find_all('link', href = True, rel = True):
            if "rel" in doc.attrs.keys():
                if "icon" in doc.attrs["rel"]:
                    self.URLinfo.favicon = True
            if "href" in doc.attrs.keys():
                if "favicon" in doc.attrs["href"] or ".ico" in doc.attrs["href"]:
                    self.URLinfo.favicon = True
            if "id" in doc.attrs.keys():
                if "favicon" in doc.attrs["id"] or ".ico" in doc.attrs["id"]:
                    self.URLinfo.favicon = True
        for doc in BeautifulSoup(responseInfo, "html.parser").find_all("meta", href = True, rel = True):
            if "content" in doc.attrs.keys():
                if ".ico" in doc.attrs["content"] or "favicon" in doc.attrs["content"]:
                    self.URLinfo.favicon = True

# def testium():
#     urlHTMLparser = HTMLparser()
#     urlHTMLparser.parse()
