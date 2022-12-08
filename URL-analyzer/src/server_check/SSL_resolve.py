"""
Handles TSL/SSL related tasks, such as fethcing, checking, and testing of URLs
"""

import socket
import ssl
import urllib3
from src.URLCheck import url_sanitize

__author__  = "Totte Hansen, DVADS20h"

# checks connection and status of URL server
url_con = urllib3.PoolManager()



class ssl_parser:
    def ssl_sanetize(self, url:str) -> str:
        """
        Append SSL attributes
        """
        self.sane_url = url_sanitize.rm_scheme(url)

        if not url_sanitize.siteValid(self.sane_url):
            self.URLinfo.errors.append("Error during SSL resolving, could not fetch server info")
            return None
        else:
            return self.sane_url

    def sanitize_url(self, url:str) -> None:
        self.sane_url = self.URLinfo.domain + "." + self.URLinfo.topDomain

    def fetch_ssl(self) -> str: #* @auth: Totte Hansen
        """
        Fetches socket encryption version, if one is present.
        If socket is encrypted is determined by URL scheme.
        """

        self.sanitize_url(self.sane_url)
        if not self.sane_url:
            self.URLinfo.errors.append(f"Site {self.sane_url} is invalid or closed")
            return None

        hostname = self.sane_url
        context = ssl.create_default_context()
        try:
            # open socket using https port 443
            with socket.create_connection((hostname, 443), timeout=8) as sock:
                # fetch sock version
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    try:
                        self.URLinfo.TLSversion = ssock.version()
                        return ssock.getpeercert()

                    except Exception as err:
                        self.URLinfo.errors.append("Error during SSL resolving, Couldnt get cert info")
                        return None

        except Exception as err:
            if "EOF" in str(err):
                self.URLinfo.certIncomplete = True
            self.URLinfo.errors.append("Error during SSL resolving, Socket connection timed out or was denied")
            return None



    def updateSSL(self) -> None: #* @auth: Totte Hansen
        self.cert = self.fetch_ssl()

    def __init__(self, url : str, URLinfo) -> None: #* @auth: Totte Hansen
        self.original_url = url
        self.URLinfo = URLinfo
        self.sane_url = self.ssl_sanetize(url)
        # self.sane_url = self.URLinfo.domain + "." + self.URLinfo.topDomain
        self.cert = self.fetch_ssl()
