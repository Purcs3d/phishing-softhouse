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

    def run(self):
        """
            Run through the algorithm with the URL
            it first evaluates the URL
            then makes decision if the website is fishy/not fishy
            input: self, output: boolean
        """
        self.runEvaluations() # collect total points
        report = self.URLinfoObj.generateReport() #generate report on ULR
        for info in report: # print all information gathered from URL
            print(info)
        print("Evaluation points:",self.points)
        print(f"This site have been active for {self.URLinfoObj.active} \n Was created {self.URLinfoObj.registed} \n Was updated {self.URLinfoObj.update} \n Will expire in {self.URLinfoObj.expires}")

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
        self.points += URLstringCLobj.containUnicode()
