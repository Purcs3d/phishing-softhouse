import src.URLCheck.URLinfo as URLinfo
import src.checklists.DatabaseComparisonCL as DatabaseComparisonCL
import src.checklists.HTMLdataCL as HTMLdataCL
import src.checklists.URLstringCL as URLstringCL
import src.checklists.DNSdataCL as DNSdataCL
import src.DB.DBhandler as DBhandler

class algorithmManager:
    """
        This class manages the URLinfo object and the checklist objects
    """
    def __init__(self, url):
        self.url = url
        self.points = 0
        self.report = {}
        self.URLinfoObj = URLinfo.URLinfo(url) #create URLinfo object
        self.DBonline = True
        self.URLinWhitelist = False
        self.URLinPreviousSearches = False
        self.fishy = False
        try:
            self.checkDB() # check if in whitelist/previous searches
        except Exception as e:
            self.DBonline = False
            self.URLinfoObj.errors.append(f"Database connection failed... evaluation run anyway.")
        self.URLinfoObj.collectInfo() #make object collect information about url
        self.pointPhishingLimit = 100

    def run(self):
        """
            Run through the algorithm with the URL
            it first evaluates the URL
            then makes decision if the website is fishy/not fishy
            input: self, output: boolean
        """
        # check if in DB
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
        URLstringCLobj = URLstringCL.URLstringCL(self.URLinfoObj)
        HTMLdataCLobj = HTMLdataCL.HTMLdataCL(self.URLinfoObj)
        DatabaseComparisonCLobj = DatabaseComparisonCL.DatabaseComparisonCL(self.URLinfoObj)
        DNSChecklistObj = DNSdataCL.DNSdataCL(self.URLinfoObj)


        #run their seperate evaluations
        self.points += URLstringCLobj.runEvaluation()
        self.points += HTMLdataCLobj.runEvaluation()
        self.points += DatabaseComparisonCLobj.runEvaluation()
        self.points += DNSChecklistObj.runEvaluation()

        #gather their seperate reports
        self.report["URLstringCL"] = URLstringCLobj.report
        self.report["HTMLdataCL"] = HTMLdataCLobj.report
        self.report["DNSdataCL"] = DNSChecklistObj.report
        self.report["DatabaseComparisonCL"] = DatabaseComparisonCLobj.report


    def createOutputString(self):
        if self.URLinWhitelist == True:
            outputStr = "URL in exist whitelist and is not phishy."+ "<br>"
            return outputStr
        if self.URLinPreviousSearches == True:
            outputStr = "URL recently searched; fetched report:"+ "<br>"
            outputStr += self.DBhandlerObj.fetchPreviousSearchReport()
            return outputStr
        outputStr = "fishy?:" + str(self.fishy)
        outputStr +=  "<br> evaluation points:" + str(self.points) + "<br>"
        for message in self.report["URLstringCL"]:
            outputStr += message + "<br>"
        outputStr += "<br>"
        for message in self.report["HTMLdataCL"]:
            outputStr += message + "<br>"
        outputStr += "<br>"
        for message in self.report["DNSdataCL"]:
            outputStr += message + "<br>"
        outputStr += "<br>"
        for message in self.report["DatabaseComparisonCL"]:
            outputStr += message + "<br>"
        outputStr += "<br>"
        for message in self.report["URLreport"]:
            outputStr += message + "<br>"
        outputStr += "<br>"
        for message in self.report["errors"]:
            outputStr += message + "<br>"
        outputStr += "<br>"
        return outputStr


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
