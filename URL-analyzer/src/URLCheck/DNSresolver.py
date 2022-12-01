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
            self.URLinfo.ip = socket.gethostbyname(self.URLinfo.domain + "." + self.URLinfo.topDomain) #temporär lösning
            self.fetchDNSdata()
            self.fetchAge(self.URLinfo.url)
        except TypeError:
            self.URLinfo.errors.append(f"Error during DNS resolving: DNS creation info not found.")
        except requests.exceptions.RequestException:
            self.URLinfo.errors.append(f"Error during DNS resolving: Failed request to server")
        except Exception:
            self.URLinfo.errors.append(f"Error during DNS resolving, connection failed")
            return self.URLinfo
        return self.URLinfo

    def fetchDNSdata(self):
        """
            fetch DNS data including geolocation and IP address
        """
        data = requests.get(f"https://geolocation-db.com/json/{self.URLinfo.ip}&position=true").json()
        if "IPv4" in data.keys():
            self.URLinfo.ip = data["IPv4"]
        if "IPv6" in data.keys():
            self.URLinfo.ip = data["IPv6"]
        self.URLinfo.country = data['country_name']
        self.URLinfo.city = data['city']
        self.URLinfo.region = data['state']

    def fetchAge(self, url):
        """
            Fetches information about domain creation date and domain age
        """
        w = whois.whois(url)
        self.URLinfo.expires = w.expiration_date
        self.URLinfo.registered = w.creation_date
        self.URLinfo.update = w.updated_date
        dateNow = dt.datetime.now()
        if type(self.URLinfo.registered) == list: #if multiple registration dates -> pick latest
            self.URLinfo.active =  dateNow - self.URLinfo.registered[0]
        else:
            self.URLinfo.active =  dateNow - self.URLinfo.registered
