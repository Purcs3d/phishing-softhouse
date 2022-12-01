"""
@author: Totte Hansen, DVADS20h

Checklist and tests associated with SSL/TSL attributes
"""

from src.server_check import SSL_resolve
import config as conf
import ssl


#TODO report

__author__ = 'Totte Hansen, DVADS20h'

class SSL_CL:
    def run_evaluation(self): #* auhtor: Totte Hansen *#
        """
        Run through all tests sequentially using function calls
        """
        # return early in case certificate is empty
        if self.check_handshake == False:
            return

        self.check_version()


    def check_handshake(self) -> bool:
        """
        Check if the cert handshake returned properly. If the cert is empty, great phishiness
        """
        # amount of points to be added in case of empty cert
        empty_points = 100

        # check if cert dict is empty
        if len(self.cert.cert) == 0:
            self.report.append("SSL/TSL certificate returned with empty attributes")
            self.points += empty_points
            # return handshake did not return properly
            return False

        return True


    def check_version(self): #* auhtor: Totte Hansen *#
        point_value_version = 20
        point_value_none = 50

        # no license could be fetched from site
        if self.cert == None:
            self.points += point_value_none
            self.report.append("The website lacks TSL/SSL ensurance")

        version = self.cert["version"]
        if version >= conf.MIN_CERT_VER:
            self.points += point_value_version
            self.report.append("The website uses an outdated TSL/SSL license version (Version {self.cert['version']})")

    def check_licenser(self):
        """
        Check who the licenser is, and if its same as host
        """
        ...

    def check_crt_age(self):
        """
        Check if the license is extemrely young (old certs are seen as more likely legitimate)
        """
        ...

    def check_cert_math(self) -> None:
        """
        Check if the cert hostaddress matches the input address
        """
        address_points = 50

        # test if the returned cert supports the URL
        try:
            ssl.match_hostname(self.cert.cert, self.cert.san)

        # cert does not support the URL
        except ssl.CertificateError:
            self.report.append("The returned certificate does not support the input URL")
            self.points += address_points


    def check_domain_time(self):
        """
        Check how long the current owner has owned the cert (short owner age, phishy)
        """
        ...

    def check_cert_origin(self):
        """
        Check country of origin of the certificate. #TODO check untrusted cert countries
        """
        ...

    def check_valid(self):
        """
        Check if the cert is valid between the "NOT before" and "NOT after" dates, 
        and check if the cert has been revoked
        """
        ...
    
    
    def check_self_signed(self):
        """
        Check if the domain has signed the cert themselves. if they have, phishy
        """
        ...

    def check_encrypt(self):
        """
        Check if the certificate uses a hard-to-spoof hashing algorithm (e.g. SHA256)
        """
        ...


    def __init__(self, url):
        self.points = 0
        self.report = []

        self.url = url
        self.cert = ssl_resolve.SSLParse(url)
