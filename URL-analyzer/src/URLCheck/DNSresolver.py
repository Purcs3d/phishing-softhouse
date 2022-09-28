import socket
import requests

class DNSresolver():
    """
        This class will resolve information about
        ip
        country
        city
    """

    def __init__(self, URLinfo):
        self.URLinfo = URLinfo
        self.data = None

    def parse(self):
        try:
            ip = socket.gethostbyname(urlName)
        except socket.error:
            print('Ip address could not be found from hostname')
            return False
        self.URLinfo.data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        self.URLinfo.country = data['country_name']
        self.URLinfo.city = data['city']
        self.URLinfo.region = data['state']
