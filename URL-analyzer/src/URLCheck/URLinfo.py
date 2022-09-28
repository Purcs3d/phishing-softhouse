from dataclasses import dataclass
from urllib.parse import urlparse
import socket
import requests

'''
The URLinfo dataclass works like a struct in C-like languegues.
It stroes and holds the given data.

The Parser Class has one function in it
It's job is to parse the url and resolve infomration from it
'''

@dataclass
class URLinfo:
    protocol: str
    urlName: str
    path: str
    params: str
    query: str
    fragment: str
    ip: str
    city: str
    country: str
    region: str

class Parser:
    def __init__(self) -> None:
        self.infoList = []

    def UrlResolver(self, url):
        parse = urlparse(url)
        #print(parse)
        urlName = parse.netloc # t ex www.google.com
        protocol = parse.scheme # HTTP eller HTTPS
        path = parse.path # t ex /auth/login
        params = parse.params # No longer used, always empty
        query = parse.query # everything after ? in the url before the #
        fragment = parse.fragment # evrything after # in the back of the url
        try:
            ip = socket.gethostbyname(urlName)
        except socket.error:
            print('Ip address could not be found from hostname')
            return False
        data = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        #print(data)
        country = data['country_name']
        city = data['city']
        region = data['state']
        info = URLinfo(protocol, urlName, path, params, query, fragment, ip, city, country, region)

        self.infoList.append(info)



#p = Parser()
#p.UrlParser(input("Inpute the url here:"))
