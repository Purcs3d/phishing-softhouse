import src.URLCheck.URLinfo as URLinfo
import src.checklists.DatabaseComparisonCL as DatabaseComparisonCL
import src.checklists.HTMLdataCL as HTMLdataCL
import src.checklists.URLstringCL as URLstringCL
import src.checklists.DNSChecklist as DNSCL

class algorithmManager:
    """
        This class managing the URLinfo object and the checklist objects
    """
    def __init__(self, url):
        self.url = url
        self.points = 0
        self.URLinfoObj = URLinfo.URLinfo(url) #create URLinfo object
        self.URLinfoObj.collectInfo() #make object collect information about url
        self.pointPhishingLimit = 100
        self.report = {}

    def run(self):
        """
            Run through the algorithm with the URL
            it first evaluates the URL
            then makes decision if the website is fishy/not fishy
            input: self, output: boolean
        """
        self.runEvaluations() # collect total points and gather reports
        self.printFormat() # print reports, URL info and errors
        if self.points > self.pointPhishingLimit:
            return True
        else:
            return False

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
        DNSChecklistObj = DNSCL.DNSChecklist(self.URLinfoObj)

        #run their seperate evaluations
        self.points += URLstringCLobj.runEvaluation()
        self.points += HTMLdataCLobj.runEvaluation()
        self.points += DatabaseComparisonCLobj.runEvaluation()
        self.points += DNSChecklistObj.evaluate()

        #gather their seperate reports
        self.report["URLstringCL"] = URLstringCLobj.report
        self.report["HTMLdataCL"] = HTMLdataCLobj.report
        self.report["DNSChecklist"] = DNSChecklistObj.report
        self.report["DatabaseComparisonCL"] = DatabaseComparisonCLobj.report


    def printFormat(self):
        """
            self.report is a dictionary that holds information about
                • checklist reports
                • URL info
                • errors
        """
        # print checklist info and evaluation
        print("-" * 20,"\nReport and output:")
        for message in self.report["URLstringCL"]:
            print(message)
        for message in self.report["HTMLdataCL"]:
            print(message)
        for message in self.report["DNSChecklist"]:
            print(message)
        for message in self.report["DatabaseComparisonCL"]:
            print(message)
        print("Evaluation points:",self.points)

        # print info gathered
        print("\n\n", "-" * 20,"\nInfo gathered from URL:")
        self.report["URLreport"] = self.URLinfoObj.generateReport() #generate report on URL info
        for info in self.report["URLreport"]: # print all information gathered from URL
            print(info)
        #print(f"This site have been active for {self.URLinfoObj.active} \n Was created {self.URLinfoObj.registed} \n Was updated {self.URLinfoObj.update} \n Will expire in {self.URLinfoObj.expires}")

        #print errors
        print("\n", "-" * 20,"\nErrors:")
        self.report["errors"] = self.URLinfoObj.errors
        for error in self.report["errors"]:
            print(error)
