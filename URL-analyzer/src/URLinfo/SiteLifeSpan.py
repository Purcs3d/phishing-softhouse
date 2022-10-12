import whois

class DomainAge():
    def __init__(self, urlname, ) -> None:
        self.url = urlname
        self.domain
        self.ip
        self.expires
        self.registed
        self.update

    def fetchAge(self):
        w = whois.whois(self.domain)
        self.expires = w.expiration_date
        self.registed = w.creation_date
        self.update = w.updated_date
        print(self.registed, self.expires, self.update )
