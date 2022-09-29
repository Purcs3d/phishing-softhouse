import socket
import requests

class DNSresolver():
    """
        This class will resolve information about
        ip
        country
        city
        region
        maybe port etc
    """

    def __init__(self, URLinfo):
        self.URLinfo = URLinfo
        self.data = None

    def resolve(self):
        try:
            ip = socket.gethostbyname(self.URLinfo.url)#"svt.se")
        except socket.error:
            # print('Ip address could not be found from hostname')
            self.URLinfo.country = "Sweden"
            self.URLinfo.city = "Karlskrona"
            self.URLinfo.region = "Blekinge"
            return self.URLinfo
        data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        self.URLinfo.data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        self.URLinfo.country = data['country_name']
        self.URLinfo.city = data['city']
        self.URLinfo.region = data['state']
        return self.URLinfo
