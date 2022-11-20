""" 
Handles TSL/SSL related tasks, such as fethcing, checking, and testing of URLs
"""

import socket
import ssl
from termios import ECHOE
import urllib3
from src.URLCheck import url_sanitize

#! debug libs
from pprint import pprint

__author__  = "Totte Hansen, DVADS20h"

# checks connection and status of URL server
url_con = urllib3.PoolManager()

def ssl_sanetize(url:str) -> str:
    """
    Append SSL attributes
    """
    sane_url = url_sanitize.rm_scheme(url)

    if not url_sanitize.siteValid(sane_url):
        assert("SSL could not fetch server")

    return sane_url


class ssl_parse: #* @auth: Totte Hansen
    def sanitize_url(self, url:str) -> None:
        self.sane_url = url_sanitize.rm_scheme(url, True)

    def fetch_ssl(self, excep: bool = False) -> str: #* @auth: Totte Hansen
        """ 
        Fetches socket encryption version, if one is present.
        If socket is encrypted is determined by URL scheme.
        """

        if not url_sanitize.siteValid:
            assert(f"Site {self.sane_url} is invalid or closed")

        hostname = self.sane_url
        context = ssl.create_default_context()
        try:
            # open socket using https port 443
            with socket.create_connection((hostname, 443)) as sock:

                # fetch sock version
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    try:
                        return ssock.version()

                    except Exception as err:
                        if excep:
                            raise err
                        else:
                            return None

        except Exception as err:
            if excep:
                raise err
            else:
                return None



    def updateSSL(self) -> None: #* @auth: Totte Hansen
        ...

    def __init__(self, url : str) -> None: #* @auth: Totte Hansen
        self.original_url = url
        self.sane_url = ssl_sanetize(url)
        self.license = self.fetch_ssl(self.sane_url)
