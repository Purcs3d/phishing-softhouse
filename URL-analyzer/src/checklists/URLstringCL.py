class URLstringCL():
    """
        This checklist will evalute the values that have been fetched from the URL string input
        ex:
        input("pizzaslice.45:93")
        runEvaluation("pizzaslice.45:93")
        output(50 points to gryffindor) #very fishy
    """

    def __init__(self, URLinfo = None):
        self.points = 0
        self.URLinfo = URLinfo

    def runEvaluation(self):
        return self.points
