"""
@author: Totte Hansen, DVADS20h

Checklist and tests associated with SSL/TSL attributes
"""

from src.server_check import SSL_resolve
import config as conf
import ssl
import whois
from datetime import datetime, timezone


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
        empty_cert_points = 100
        empty_cert_report = "SSL/TSL certificate returned with empty attributes"

        # check if cert dict is empty
        if len(self.cert.cert) == 0:
            self.report.append(empty_cert_report)
            self.points += empty_cert_points
            # return handshake did not return properly
            return False

        return True


    def check_version(self): #* auhtor: Totte Hansen *#
        outdated_ver_points = 20
        outdated_report = "The website uses a depricated SSL/TSL version (<3)"

        no_cert_points = 30
        no_cert_report = "The website lacks TSL/SSL ensurance"

        # no license could be fetched from site
        if self.cert == None:
            self.points += no_cert_points
            self.report.append(no_cert_report)

        version = self.cert["version"]
        if version >= conf.MIN_CERT_VER:
            self.points += outdated_ver_points
            self.report.append(outdated_report)

    def check_licenser(self):
        """
        Check who the licenser is, and if its same as host
        """
        self_license_points = 25
        self_license_report = "The certificate is self issued"

        # fetch site registered owner
        site_org = whois.whois(self.cert.sane_url).org
        # fetch cert issuer corporation
        issuer = self.cert.cert["issuer"][1][0][1]


    def check_cert_age(self): #TODO
        """
        Check if the license is extemrely young (old certs are seen as more likely legitimate)
        """
        one_day_points = 75
        one_day_report = "The license age is less than a day"

        one_week_points = 50
        one_week_report = "The license age is less than a week"

        one_month_points = 25
        one_month_report = "The license age is less than a month"

        # get age
        # cert_age = self.cert.cert[]
        
        #TODO find cert issue time method
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
            self.report.append("Returned certificate does not support the given URL")
            self.points += address_points


    def check_domain_time(self): #TODO
        """
        Check how long the current owner has owned the cert (short owner age, phishy)
        #TODO find cert issue time method
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
        cert_timeout_points = 50
        cert_after_report   = "The certificate is out of date, therefore invalid"
        cert_before_report  = "The certificate is not allowed to be userd yet, therefore invalid"

        # get the delta of the "NOT BEFORE"
        current_time = datetime.now(timezone.utc)

        before_delta = current_time - self.cert.cert["notBefore"]
        # if 


        after_delta = self.cert.cert["notAfter"]
        
    
    
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
