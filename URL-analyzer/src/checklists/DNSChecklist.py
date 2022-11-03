
class DNSChecklist():

    def __init__(self,URLinfo ) -> None:
        self.URLinfo = URLinfo
        self.report = []

    def evaluate(self):
        if self.URLinfo.active == None: # om hemsidan inte existerar.
            return 0
        self.URLinfo.timestr = str(self.URLinfo.active)
        self.URLinfo.daysActive = ""
        for i in self.URLinfo.timestr:
            if(i == ' '):
                break
            else:
                self.URLinfo.daysActive+=i
        if(int(self.URLinfo.daysActive) < 2):
            self.report.append("This domain is younger then two days")
            return 50
        elif(int(self.URLinfo.daysActive) < 10):
            self.report.append("This domain is younger then ten days")
            return 20
        elif(int(self.URLinfo.daysActive) > 365):
            self.report.append("This site is over a year old")
            return 1
