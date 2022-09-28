import src.URLCheck.URLinfo as URLinfo
import src.checklists.DatabaseComparisonCL as DatabaseComparisonCL
import src.checklists.HTMLdataCL as HTMLdataCL
import src.checklists.URLstringCL as URLstringCL

class algorithmManager:
    def __init__(self, url):
        self.url = url
        self.points = 0
        self.URLinfoObj = URLinfo.URLinfo(url)
        self.URLinfoObj.collectInfo()
        #self.pointPhishingLimit = 20
        # self.rapportGeneration = [] #maybe dictionary is better idk
        #self.URLinfoObj.UrlResolver(self.url)

    def run(self):
        """
            Run through the algorithm with the URL
            it first evaluates the URL
            then makes decision if the website is fishy/not fishy
            input: self, output: boolean
        """
        self.runEvaluations() # collect total points
        if self.points > 100:
            return True
        else:
            return False

    def runEvaluations(self):
        """
            This function sends in the URLinfo to all checklists which runs evaluations on the different
            information from the URL info that we have fetched.
            The checklists then returns the points that they have collected after evaluation
            and algorithmManager adds them all together in self.points
            Then run(self) makes the evaluation if the URL is fishy or not.

            future: if we should be able to generate rapport then these objects will not only
            return their collected points but also which attributes they checked etc
        """

        # create checklists
        URLstringCLobj = URLstringCL.URLstringCL(self.URLinfoObj)
        HTMLdataCLobj = HTMLdataCL.HTMLdataCL(self.URLinfoObj)
        DatabaseComparisonCLobj = DatabaseComparisonCL.DatabaseComparisonCL(self.URLinfoObj)

        #run their seperate evaluations
        self.points += URLstringCLobj.runEvaluation()
        self.points += HTMLdataCLobj.runEvaluation()
        self.points += DatabaseComparisonCLobj.runEvaluation()


    # def runEvalAlgo(self):
    #     """Example of how to add attributes to the evalutation algorithm"""
    #     # if badExtention == True:
    #     #     self.points += 10
    #     #     self.rapportGeneration.append("The URL has a untrusted extention")
    #     print(self.URLinfoObj.infoList[0])
    #     if self.URLinfoObj.infoList[0] == "HTTP":
    #         self.points += 30
    #         self.rapportGeneration.append("The website is using HTTP")
    #     if self.points > self.pointPhishingLimit:
    #         return True
    #     else:
    #         return False


    def printMsg(self):
        print(f"Hello world this object is handeling the url: {self.url}")
