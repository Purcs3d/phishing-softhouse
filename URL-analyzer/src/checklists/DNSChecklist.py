
class DNSChecklist():

    def __init__(self,URLinfo ) -> None:
        self.URLinfo = URLinfo

    def evaluate(self):
        self.URLinfo.timestr = str(self.URLinfo.active)
        self.URLinfo.daysActive = ""
        for i in self.URLinfo.timestr:
            if(i == ' '):
                break
            else:
                self.URLinfo.daysActive+=i
        if(int(self.URLinfo.daysActive) < 2):    
            print("This domain is younger then two days")
            return 50
        elif(int(self.URLinfo.daysActive) < 10):
            return 20
        elif(int(self.URLinfo.daysActive) > 365):
            print("This site is over a year old")
            return 1