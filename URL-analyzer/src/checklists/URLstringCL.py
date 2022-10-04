class URLstringCL():
    """
        This checklist will evalute the values that have been fetched from the URL string input
        ex:
        1.
        def protocolCheck(self):
             if self.URLinfo.protocol == "HTTP":
                     self.points += 30
        2. add call to function in runEvaluation
    """

    def __init__(self, URLinfo = None):
        self.points = 0
        self.rapport = []
        self.URLinfo = URLinfo

    def runEvaluation(self):
        """
            Run through all checks by calling on their functions
        """
        self.protocolCheck()
        self.isdomaininrrussia()
        return self.points

    def isdomaininrrussia(self):
        if self.URLinfo.urlName == ".ru":
            self.points += 10

    def protocolCheck(self): #emils function
        if self.URLinfo.protocol == "http":
            self.points += 30
            self.rapport.append("The website is using HTTP")
            #self.rapportGeneration.append("The website is using HTTP") kan fixa senare
