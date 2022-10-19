import socket
import requests

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
            ip = socket.gethostbyname(self.URLinfo.domain + "." + self.URLinfo.topDomain)
        except Exception as e:
            self.URLinfo.errors.append(f"Error during DNS resolving: {e}")
            return self.URLinfo
        data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        self.URLinfo.data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        self.URLinfo.country = data['country_name']
        self.URLinfo.city = data['city']
        self.URLinfo.region = data['state']
        self.URLinfo.ip = data['IPv4']
        return self.URLinfo
