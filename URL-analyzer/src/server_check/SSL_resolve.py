""" 
Handles TSL/SSL related tasks, such as fethcing, checking, and testing of URLs
"""

import socket
import ssl
from termios import ECHOE
import requests
import urllib3

#! debug libs
from pprint import pprint

__author__  = "Totte Hansen, DVADS20h"
__version__ = "init"
__license__ = "None"


# checks connection and status of URL server
url_con = urllib3.PoolManager()

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


    def checkOpen(addr:str) -> dict:
        """ 
        Check if a URL site is open.

        return:
            - dict        - `{"reachable": bool, "status": <in>}`  
            - "reachable" - if site is reachable given the URl
            - "status"    - Exit code, follows HTTP standard. `-2` indicate site could not be reached
        """
        # check if domain exists
        out = {"reachable": True, "status": None}

        # url_stats = None
        # try:
        #     url_stats = url_con.request("GET", addr)
        #     print(url_con.status)

        # # server side error codes
        # except socket.gaierror as err:
        #     # if socket is unreachable (`[Errno -2] Name or service not known`)
        #     if err.errno:
        #         out[] = 
        
        # # raise undefiend error
        # except Exception as err:
        #     raise err

        # return out


    def updateSSL() -> None: #* @auth: Totte Hansen
        ...
    def runSSLTests() -> int: #* @auth: Totte Hansen
        ...

    def __init__(self, url : str, redirectURL:bool = True) -> None: #* @auth: Totte Hansen
        self.url = url

        


#* ===-==-=== *#


def getRedir(addr:str) -> str:
    #TODO does not fetch json redirects correctly (such as http://google.com -> https://consent.google.com/ml?continue=https://www.google.com/&gl=SE&m=0&pc=shp&uxe=none&hl=sv&src=1)
    """ 
    Fetches URL after server redirects.
    """
    connection = requests.get(addr)
    return connection.url


# sslObj  = SSLChecker("google.com")
# sslObj  = SSLChecker("http://ninjaflex.com/")
# print(sslObj.fetchSSL())

# r = r_get("http://google.com")
# print(r.url)
# # print(dumps(ssl.__dict__, indent=2))


addr = "g.com"

# print(socket.gethostbyname(addr))

url_stats = None

try:
    url_stats = url_con.request("GET", addr)
    print(url_stats.status)

# server side error codes
except Exception as err:
    # if socket is unreachable (`[Errno -2] Name or service not known`)
    if "errno" in err.__dict__:
        print("yes :D")

    else:
        print("no :(")

    print(err.reason)

