
class DNSdataCL():
    """
        This checklist will evalute the values that have been fetched from the DNS
        ex:
        1.
        def domainNameCreationDateCheck(self):
             if URLinfo.domaincreation == "2 days ago"
                    self.points += 30

        2. add call to function in runEvaluation
    """
    def __init__(self,URLinfo ) -> None:
        self.URLinfo = URLinfo
        self.points = 0
        self.report = []

    def runEvaluation(self):
        self.evaluateDomainCreation()
        return self.points

    def evaluateDomainCreation(self):
        """
            Evaluates the domain creation date,
             • if its less than 20 days old -> very likely phishy
             • if its less than 365 days old -> probably phishy
        """
        if self.URLinfo.active == None: # if domain age request failed
            return
        timestr = str(self.URLinfo.active)
        self.URLinfo.daysActive = ""
        for i in timestr:
            if(i == ' '):
                break
            else:
                self.URLinfo.daysActive+=i
        if(int(self.URLinfo.daysActive) < 20):
            self.report.append("This domain is younger then 20 days")
            self.points +=  100
            return
        elif(int(self.URLinfo.daysActive) < 365):
            self.report.append("This domain is younger than a year")
            self.points += 50
            return
        elif(int(self.URLinfo.daysActive) < 730):
            self.report.append("This domain is younger than 2 years old")
            self.points += 20
            return
