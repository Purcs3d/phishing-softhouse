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
        self.checkSpecialChar()
        return self.points

    def isdomaininrrussia(self):
        if self.URLinfo.urlName == ".ru":
            self.points += 10

    def protocolCheck(self): #Emils function
        if self.URLinfo.protocol == "http":
            self.points += 20
            self.rapport.append("The website is using HTTP")
            #self.rapportGeneration.append("The website is using HTTP") kan fixa senare

    def checkSpecialChar(self): #Emils function
        """
        Questions:
        Should the function punish a url more if it has multiple special character violations?
        """
        violatedSpecialChar = False
        charViolated = []
        url = self.URLinfo.url
        badCharacters = [ "$", "#", "£", "0", "3", "8", "1", "_", "=", "!" ]
        for char in badCharacters:
            if char in url:
                violatedSpecialChar = True
                charViolated.append(char)

        if violatedSpecialChar:
            self.points += 30
            self.rapport.append(f"The URL violated the following special characters: {charViolated}")
