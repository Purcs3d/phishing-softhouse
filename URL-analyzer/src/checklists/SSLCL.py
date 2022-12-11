"""
@author: Totte Hansen, DVADS20h

Checklist and tests associated with SSL/TSL attributes
"""

from src.server_check import SSL_resolve
import src.config as conf
import ssl
import whois
from datetime import datetime, timezone

__author__ = 'Totte Hansen, DVADS20h'

class SSLCL:
    """
    Evalutates phishiness within the SSL/TLS certificates
    """

    def runEvaluation(self): #* auhtor: Totte Hansen *#
        """
        Run through all tests sequentially using function calls
        """
        if not self.check_version():
            return self.points

        if not self.check_handshake() :
            return self.points

        if self.check_incomplete_cert():
            return self.points

        self.check_licenser()
        self.check_cert_age()
        self.check_cert_match()
        self.check_time_valid()
        self.check_cert_origin()

        return self.points


    def check_incomplete_cert(self):
        if self.URLinfo.certIncomplete == True:
            self.points += 50
            self.report.append("Websites certificate information was incomplete")
            return True

        return False

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
        outdated_ver_points = 50
        outdated_report_tls = "The website uses a depricated SSL/TSL version (less than TSLv1.3)"
        outdated_report = "The website uses a depricated SSL/TSL version (less than version 3)"

        no_cert_points = 80
        no_cert_report = "The website lacks TSL/SSL ensurance"

        # no license could be fetched from site
        if self.cert.cert == None:
            self.points += no_cert_points
            self.report.append(no_cert_report)
            return False

        version = self.cert.cert["version"]
        if version <= conf.MIN_CERT_VER:
            self.points += outdated_ver_points
            self.report.append(outdated_report)

        if self.URLinfo.TLSversion in conf.BAD_CERT_VERSIONS:
            self.points += outdated_ver_points
            self.report.append(outdated_report_tls)
        return True


    def check_licenser(self): #TODO add phishy licensers
        """
        Check who the licenser is, and if its same as host
        """
        self_license_points = 25
        self_license_report = "The certificate is self issued"

        # error med URL STORAGE.GOOGLEAPIS.COM
        #whois.parser.PywhoisError: No match for "STORAGE.GOOGLEAPIS.COM".
        #>>> Last update of whois database: 2022-12-05T13:01:02Z <<<

        try:
            # fetch site registered owner
            site_org = whois.whois(self.cert.sane_url).org
            # fetch cert issuer corporation
            issuer = self.cert.cert["issuer"][1][0][1] #organisationName

            if site_org == issuer:
                self.points += self_license_points
                self.report.append(self_license_report)
        except Exception:
            self.points += self_license_points
            self.report.append("Information about websites registered issuer and owner was not found")


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



    def check_cert_match(self) -> None:
        """
        Check if the cert hostaddress matches the input address
        """
        address_points = 50

        # test if the returned cert supports the URL
        try:
            ssl.match_hostname(self.cert.cert, self.cert.sane_url)

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
        issuer = self.cert.cert["issuer"][0][0][1] #countryName
        if issuer in conf.BAD_CERT_COUNTRYCODES:
            self.points += 30
            self.report.append(f"SSL Certificate created in the country with countrycode: {issuer}")


    def check_time_valid(self):
        """
        Check if the cert is valid between the "NOT before" and "NOT after" dates,
        and check if the cert has been revoked
        """
        cert_timeout_points = 50
        cert_after_report   = "The certificate is out of date, therefore invalid"
        cert_before_report  = "The certificate is not allowed to be userd yet, therefore invalid"

        # get the delta of the "NOT BEFORE"
        current_time = datetime.utcnow()

        # convert from datetime str to utc datetime
        notAfter_datetime = ssl.cert_time_to_seconds(self.cert.cert["notAfter"])
        notAfter_datetime = datetime.utcfromtimestamp(notAfter_datetime)

        # test cert not too old
        if current_time > notAfter_datetime:
            self.points += cert_timeout_points
            self.report.append(cert_after_report)

        # convert from datetime str to utc datetime
        notBefore_datetime = ssl.cert_time_to_seconds(self.cert.cert["notBefore"])
        notBefore_datetime = datetime.utcfromtimestamp(notBefore_datetime)

        # test cert is not too "young"
        if current_time < notBefore_datetime:
            self.points += cert_timeout_points
            self.report.append(cert_before_report)


    def check_encrypt(self): #TODO find method for fetching encrypt method
        """
        Check if the certificate uses a hard-to-spoof hashing algorithm (e.g. SHA256)
        """
        ...


    def __init__(self, url, URLinfo):
        self.points = 0
        self.report = []
        self.URLinfo = URLinfo
        self.url = url
        self.cert = SSL_resolve.ssl_parser(url, URLinfo)
