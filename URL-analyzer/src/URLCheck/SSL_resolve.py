""" 
Handles TSL/SSL related tasks, such as fethcing, checking, and testing of URLs
"""

import socket
import ssl
import requests
import urllib3

#! debug libs
from json import dumps

__author__  = "Totte Hansen, DVADS20h"
__version__ = "init"
__license__ = "None"

class SSLParse: #* @auth: Totte Hansen

    def fetchDomain(): #* @auth: Totte Hansen
        """
        Takes implied domain URLs and returns it as the full domain requested 
        by server
        """
        ...
    

    def fetchSSL(self) -> str: #* @auth: Totte Hansen
        """ 
        Fetches socket encryption version, if one is present.
        If socket is encrypted is determined by URL scheme.
        """

        hostname = self.url
        context = ssl.create_default_context()

        try:
            with socket.create_connection((hostname, 443)) as sock:

                # fetch sock version
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    try:
                        return ssock.version()
                    except Exception as err:
                        return err.__dict__

        except ssl.SSLError:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    try:
                        return ssock.version()
                    except Exception as err:
                        return err.__dict__

        except:
            print("not ssl error")

    def updateSSL() -> None: #* @auth: Totte Hansen
        ...
    def runSSLTests() -> int: #* @auth: Totte Hansen
        ...


    def pPrint(self, indent = 2) -> str: #* @auth: Totte Hansen
        return(dumps(self.__dict__, indent=indent))
        # print(self.__dict__)

    def __init__(self, url : str) -> None: #* @auth: Totte Hansen
        self.url = url


#* ===-==-=== *#


def checkExist(addr:str) -> bool:
    # check if domain exists
        exists = True
        
        try:
            addr = socket.gethostbyname(addr)

        # probe for errorno -2
        except socket.gaierror as err:
            # if socket is unreachable (`[Errno -2] Name or service not known`)
            if err.errno == -2:
                exists = False
            else:
                raise err
        
        # raise undefiend error
        except Exception as err:
            raise err
    
        return exists


def getRedir(addr:str) -> str:
    #TODO does not fetch json redirects correctly (such as http://google.com -> https://consent.google.com/ml?continue=https://www.google.com/&gl=SE&m=0&pc=shp&uxe=none&hl=sv&src=1)
    """ 
    Fetches URL after server redirects.
    Appends scheme, domain prefix, and subdomain to the input address
    """
    connection = requests.get(addr)
    return connection.url


# sslObj  = SSLChecker("google.com")
# sslObj  = SSLChecker("http://ninjaflex.com/")
# print(sslObj.fetchSSL())

# r = r_get("http://google.com")
# print(r.url)
# # print(dumps(ssl.__dict__, indent=2))

addr = "https://google.com"

# print(checkExist(addr))

# redict = getRedir(addr)
# print(checkExist(redict))


http = urllib3.PoolManager()

req = http.request("GET", addr)
print(dumps(req.__dict__))