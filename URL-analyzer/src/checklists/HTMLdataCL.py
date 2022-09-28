class HTMLdataCL():
    """
        This checklist will evalute the values that have been fetched from the URL string input
        ex:
        input("joemama.net")
        runEvaluation("joemama.net")
        output(50 points to hufflepuff) #very fishy
    """

    def __init__(self, URLinfo = None):
        self.points = 0
        self.URLinfo = URLinfo

    def runEvaluation(self):
        return self.points
