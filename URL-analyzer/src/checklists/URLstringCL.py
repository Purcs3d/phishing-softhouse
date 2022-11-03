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
        self.report = []
        self.URLinfo = URLinfo

    def runEvaluation(self):
        """
            Run through all checks by calling on their functions
        """
        self.protocolCheck()
        self.checkSpecialChar()
        self.checkSpecialKeywords()
        self.checkTopDomain()
        self.checkUrlLength()
        return self.points

    def protocolCheck(self): #Emils function
        if self.URLinfo.protocol == "http":
            self.points += 20
            self.report.append("The website is using HTTP")
            #self.reportGeneration.append("The website is using HTTP") kan fixa senare

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
            self.report.append(f"The URL violated the following special characters: {charViolated}")


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
            self.report.append(f"The URL contained the following bad keywords: {keywordViolated}")

    def checkTopDomain(self):
        """
            Checks if top domain is considered phishy
        """
        if self.URLinfo.topDomain in config.BAD_TOPDOMAINS:
            self.points += 15
            self.report.append(f"The URL contained the following bad topdomain: {self.URLinfo.topDomain}")


    def checkUrlLength(self):
        """
            Check if the subdomain + domain + topdomain length is considered phishy
            In other words, it does not check the length of the url path
        """
        if self.URLinfo.subDomain == None:
            urlLength = len(self.URLinfo.domain + self.URLinfo.topDomain)
        else:
            urlLength = len(str(self.URLinfo.subDomain or "") + self.URLinfo.domain + self.URLinfo.topDomain)
        if  urlLength > config.BAD_URL_LENGTH:
            self.points += 20
            self.report.append(f"The URL had a phishy length with {urlLength} letters")
