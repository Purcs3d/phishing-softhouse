import src.URLCheck.URLinfo as URLinfo
import src.checklists.DatabaseComparisonCL as DatabaseComparisonCL
import src.checklists.HTMLdataCL as HTMLdataCL
import src.checklists.URLstringCL as URLstringCL
import src.checklists.DNSdataCL as DNSdataCL
import src.DB.DBhandler as DBhandler
import src.checklists.SSLCL as SSLCL
from src.URLCheck import url_sanitize


class algorithmManager:
    """
        This class manages the URLinfo object and the checklist objects
    """
    def __init__(self, url):
        self.url = url.strip()
        self.points = 0
        self.websiteOnline = True
        self.report = {}
        self.URLinfoObj = URLinfo.URLinfo(url) #create URLinfo object
        self.DBonline = True
        self.URLinWhitelist = False
        self.URLinPreviousSearches = False
        self.fishy = False
        self.check_websiteOnline()


        try:
            self.checkDB() # check if in whitelist/previous searches
        except Exception:
            self.DBonline = False
            self.URLinfoObj.errors.append(f"Database connection failed... evaluation run anyway.")
        if self.URLinWhitelist == False and self.URLinPreviousSearches == False:
            self.URLinfoObj.collectInfo() #make object collect information about url
        self.pointPhishingLimit = 100

    def check_websiteOnline(self):
        if url_sanitize.siteValid(self.url):
            self.websiteOnline = True
        else:
            self.websiteOnline = False
            self.points += 100
        return self.points

    def run(self):
        """
            Run through the algorithm with the URL
            it first evaluates the URL
            then makes decision if the website is fishy/not fishy
            input: self, output: boolean
        """
        # check if in DB
        if self.websiteOnline == False:
            return True
        if self.URLinWhitelist == True:
            return False #if in whitelist it is not fishy
        if self.URLinPreviousSearches == True:
            return self.DBhandlerObj.fetchPreviousSearchPhishiness() # previous phisiness result

        # otherwise do regular run
        self.runEvaluations() # collect total points and gather reports
        self.report["URLreport"] = self.URLinfoObj.generateReport() #information on URL
        self.report["errors"] = self.URLinfoObj.errors #errors during information gathering

        #fishy ?
        if self.points >= self.pointPhishingLimit:
            self.fishy = True
        else:
            self.fishy = False

        # send url to history of searches table
        if self.DBonline == True:
            reportStr = self.createOutputString()
            self.DBhandlerObj.insertIntopreviousSearches(self.URLinfoObj.url, reportStr, self.fishy)
        return self.fishy

    def runEvaluations(self):
        """
            This function sends in the URLinfo to all checklists which runs evaluations on the different
            information from the URL that we have fetched.
            The checklists then returns the points that they have collected after evaluation
            and algorithmManager adds them all together in self.points
            Then run(self) makes the evaluation if the URL is fishy or not.

            input: self, output: update on self.points
        """

        # create checklists
        URLstringCLobj          = URLstringCL.URLstringCL(self.URLinfoObj)
        HTMLdataCLobj           = HTMLdataCL.HTMLdataCL(self.URLinfoObj)
        DatabaseComparisonCLobj = DatabaseComparisonCL.DatabaseComparisonCL(self.URLinfoObj)
        DNSChecklistObj = DNSdataCL.DNSdataCL(self.URLinfoObj)
        SSLCLObj              = SSLCL.SSLCL(self.url, self.URLinfoObj)


        #run their seperate evaluations
        self.points += URLstringCLobj.runEvaluation()
        self.points += HTMLdataCLobj.runEvaluation()
        self.points += DatabaseComparisonCLobj.runEvaluation()
        self.points += DNSChecklistObj.runEvaluation()
        self.points += SSLCLObj.runEvaluation()

        #gather their seperate reports
        self.report["URLstringCL"]          = URLstringCLobj.report
        self.report["HTMLdataCL"]           = HTMLdataCLobj.report
        self.report["DNSdataCL"]            = DNSChecklistObj.report
        self.report["DatabaseComparisonCL"] = DatabaseComparisonCLobj.report
        self.report["SSLCL"]                = SSLCLObj.report


    def createOutputString(self):
        if self.URLinWhitelist == True:
            reportDict['whiteList'] ={"URL in exist whitelist and is not phishy."}
            return reportDict

        if self.URLinPreviousSearches == True:
            reportDict['recent'] = {"URL recently searched; fetched report:"}
            reportDict['recent'] = {self.DBhandlerObj.fetchPreviousSearchReport()}
            return reportDict
        reportDict = {}
        reportDict[""]
        
        reportDict["Phishy"].append(self.fishy)
        reportDict["Points"].append(self.points)
        if(len(self.report["URLstringCL"]) > 0):
            reportDict["URL string information"].append(self.report["URLstringCL"])
        
        if(len(self.report["HTMLdataCL"]) > 0):
            reportDict["HTML data information"].append(self.report["HTMLdataCL"])
        
        if(len(self.report["DNSdataCL"]) > 0):
            reportDict["DNS data information"].append(self.report["DNSdataCL"])
        
        if(len(self.report["DatabaseComparisonCL"]) > 0):
            reportDict["Database comparison information"].append(self.report["DatabaseComparisonCL"])
        
        if(len(self.report["SSLCL"]) > 0):
            reportDict["SSL information"].append(self.report["SSLCL"])
        
        if(len(self.report["errors"]) > 0):
            reportDict["Errors"].append(self.report["errors"])
        return reportDict




        # outputDict = {}
        # outputDict["fishy"] = self.fishy
        # outputDict["points"] = self.points
        # if(len(self.report["URLstringCL"]) > 0):
        #     for message in self.report["URLstringCL"]:
        #         outputDict["URLstringCL"] = message
        # if(len(self.report["HTMLdataCL"]) > 0):
        #     for message in self.report["HTMLdataCL"]:
        #         outputDict["HTMLdataCL"] = message
        # if(len(self.report["DNSdataCL"]) > 0):
        #     for message in self.report["DNSdataCL"]:
        #         outputDict["DNSdataCL"] = message
        # if(len(self.report["DatabaseComparisonCL"]) > 0):
        #     for message in self.report["DatabaseComparisonCL"]:
        #         outputDict["DatabaseComparisonCL"] = message
        # if(len(self.report["URLreport"]) > 0):
        #     for message in self.report["URLreport"]:
        #         outputDict["URLreport"] = message
        # if(len(self.report["errors"]) > 0):
        #     for message in self.report["errors"]:
        #         outputDict["errors"] = message  

        return reportDict

    def checkDB(self):
        """
            check if URL in whitelist of previous searches
        """
        self.URLinfoObj.getURLstringInfo()
        self.DBhandlerObj = DBhandler.DBhandler(self.URLinfoObj)
        self.URLinWhitelist = self.DBhandlerObj.checkURLinWhitelist()
        self.URLinPreviousSearches = self.DBhandlerObj.checkURLinpreviousSearches()

    def printFormat(self):
        """
            self.report is a dictionary that holds information about
                • checklist reports
                • URL info
                • errors
            This function prints the dictionary items.
        """
        # print checklist info and evaluation
        print("-" * 20,"\nReport and output:")
        for message in self.report["URLstringCL"]:
            print(message)
        for message in self.report["HTMLdataCL"]:
            print(message)
        for message in self.report["DNSdataCL"]:
            print(message)
        for message in self.report["DatabaseComparisonCL"]:
            print(message)
        print("Evaluation points:",self.points)

        # print info gathered
        print("\n\n", "-" * 20,"\nInfo gathered from URL:")
        for info in self.report["URLreport"]: # print all information gathered from URL
            print(info)
        #print(f"This site have been active for {self.URLinfoObj.active} \n Was created {self.URLinfoObj.registed} \n Was updated {self.URLinfoObj.update} \n Will expire in {self.URLinfoObj.expires}")

        #print errors
        print("\n", "-" * 20,"\nErrors:")
        for error in self.report["errors"]:
            print(error)
