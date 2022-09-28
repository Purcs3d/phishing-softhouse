class DatabaseComparisonCL():
    """
        This checklist will evalute the values that have been fetched from the URL string input
        ex:
        input("dinmamma.se")
        runEvaluation("dinmamma.se")
        output(50 points to slytherin) #very fishy
    """

    def __init__(self, URLinfo = None):
        self.points = 0
        self.URLinfo = URLinfo

    def runEvaluation(self):
        return self.points
