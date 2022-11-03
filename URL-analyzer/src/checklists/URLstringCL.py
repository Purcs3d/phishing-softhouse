import src.config as config
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
        self.checkSpecialChar()
        self.checkSpecialKeywords()
        return self.points

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
        badCharacters = config.BAD_CHARACTERS
        for char in badCharacters:
            if char in url:
                violatedSpecialChar = True
                charViolated.append(char)

        if violatedSpecialChar:
            self.points += 30
            self.rapport.append(f"The URL violated the following special characters: {charViolated}")


    def checkSpecialKeywords(self): #Emils function
        """
        This function works by using a badKeywords list, the keywords in the list is often used in the URL of phishing sites and
        checking if the entered URL contains these bad keywords or any permutations of them, ex adm1n, fr33 or l0gin.
        """
        violatedSpecialKeyword = False
        keywordViolated = []

        badKeywords = config.BAD_KEYWORDS
        replacmentCharacters = config.REPLACEMENT_CHARACTERS

        #Creates all of the permutations of bad keywords
        permutationsOfBadKeywords = []
        for keyword in badKeywords:
            keywords = []
            keywords.append(keyword)

            i = 0
            while i < len(keyword):
                for currentKeyword in keywords:
                    chr = currentKeyword[i]
                    if chr in replacmentCharacters:
                        newKeyword = currentKeyword[0:i] + replacmentCharacters[chr] + currentKeyword[i+1:]
                        keywords.append(newKeyword)

                i += 1

            permutationsOfBadKeywords.extend(keywords)

        url = self.URLinfo.url.split(".")[1]
        for keyword in permutationsOfBadKeywords:
            if url.find(keyword) != -1:
                violatedSpecialKeyword = True
                keywordViolated.append(keyword)

        if violatedSpecialKeyword:
            self.points += 80
            self.rapport.append(f"The URL contained the following bad keywords: {keywordViolated}")
