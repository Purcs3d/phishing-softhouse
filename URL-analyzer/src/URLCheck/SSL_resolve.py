""" 
Handles TSL/SSL related tasks, such as fethcing, checking, and testing of URLs
"""

import errno
import socket
import ssl
from urllib import request
from requests import get as r_get

#! debug libs
from json import dumps

__author__  = "Totte Hansen, DVADS20h"
__version__ = "init"
__license__ = "None"

class SSLChecker(): # @auth: Totte Hansen

    def fetchDomain():
        """
        Takes implied domain URLs and returns it as the full domain requested 
        by server
        """
        ...
    

    def fetchSSL(self):
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

    def updateSSL():
        ...
    def runSSLTests():
        ...


    def pPrint(self, indent = 2):
        return(dumps(self.__dict__, indent=indent))
        # print(self.__dict__)

    def __init__(self, url : str) -> None:
        self.url = url

#* ===-==-=== *#
def checkExist(addr:str):
    # check if domain exists
        exists = True
        
        try:
            addr = socket.gethostbyname(addr)

        # probe for errorno -2
        except socket.gaierror as err:
            # if socket is unreachable (`[Errno -2] Name or service not known`)
            if err.errno == -2:
                exists = False
        
        # raise undefiend error
        except Exception as err:
            raise err
    
        return exists


# sslObj  = SSLChecker("google.com")
# sslObj  = SSLChecker("http://ninjaflex.com/")
# print(sslObj.fetchSSL())


# r = r_get("http://google.com")
# print(r.url)
# # print(dumps(ssl.__dict__, indent=2))