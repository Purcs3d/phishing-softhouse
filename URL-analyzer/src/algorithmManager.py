import src.URLCheck.URLinfo as URLinfo

class algorithmManager:
    def __init__(self, url):
        self.url = url
        self.points = 0
        self.pointPhishingLimit = 20
        self.rapportGeneration = []
        self.URLinfoObj = URLinfo.Parser()
        self.URLinfoObj.UrlResolver(self.url)


        """docstring"""
    def runEvalAlgo(self):

        """Example of how to add attributes to the evalutation algorithm"""
        # if badExtention == True:
        #     self.points += 10
        #     self.rapportGeneration.append("The URL has a untrusted extention")
        print(self.URLinfoObj.infoList[0])
        if self.URLinfoObj.infoList[0] == "HTTP":

            self.points += 30
            self.rapportGeneration.append("The website is using HTTP")

        if self.points > self.pointPhishingLimit:
            return True
        else:
            return False


    def printMsg(self):
        print(f"Hello world this object is handeling the url: {self.url}")
