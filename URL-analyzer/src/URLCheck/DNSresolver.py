import socket
import requests
import whois
import datetime as dt

class DNSresolver():
    """
        This class will resolve information about
        ip, country, city, region, maybe port etc
        ex:
        self.URLinfo.dnsdate = dnsDate["date"]
    """

    def __init__(self, URLinfo):
        self.URLinfo = URLinfo
        self.data = None

    def resolve(self):
        try:
            ip = socket.gethostbyname(self.URLinfo.domain + "." + self.URLinfo.topDomain) #temporär lösning
        except Exception as e:
            self.URLinfo.errors.append(f"Error during DNS resolving: {e}")
            return self.URLinfo
        data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        self.URLinfo.data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        if "IPv4" in data.keys():
            self.URLinfo.ip = data["IPv4"]
        if "IPv6" in data.keys():
            self.URLinfo.ip = data["IPv6"]
        self.URLinfo.country = data['country_name']
        self.URLinfo.city = data['city']
        self.URLinfo.region = data['state']
        self.fetchAge(self.URLinfo.url)

        return self.URLinfo


    def fetchAge(self, url):
        w = whois.whois(url)
        self.URLinfo.expires = w.expiration_date
        self.URLinfo.registed = w.creation_date
        self.URLinfo.update = w.updated_date
        self.URLinfo.dateNow = dt.datetime.now()
        self.URLinfo.active =  self.URLinfo.dateNow - self.URLinfo.registed
