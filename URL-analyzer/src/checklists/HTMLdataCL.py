class HTMLdataCL():
    """
        This checklist will evalute the values that have been fetched from the URL string input
        ex:
        1.
        def protocolCheck(self):
             if self.URLinfo.protocl == "HTTP":
                     self.points += 30
                     #self.rapportGeneration.append("The website is using HTTP")
        2. add call to function in runEvaluation
    """

    def __init__(self, URLinfo = None):
        self.points = 0
        self.URLinfo = URLinfo

    def runEvaluation(self):
        return self.points
