class DatabaseComparisonCL():
    """
        This checklist will evalute the values that have been fetched from the URL string input
        ex:
        1.
        def whitelistCheck(self):
             if self.URLinfo.url in whitelistedDataBase:
                     self.points -= 30
        2. add call to function in runEvaluation
    """

    def __init__(self, URLinfo = None):
        self.points = 0
        self.URLinfo = URLinfo

    def runEvaluation(self):
        """
            Run through all checks by calling on their functions
        """
        return self.points
