"""
@author: Totte Hansen, DVADS20h

Checklist and tests associated with SSL/TSL attributes
"""

from src.server_check import ssl_resolve
import config as conf


#TODO report

__author__ = 'Totte Hansen, DVADS20h'

class SSL_CL:
    def run_evaluation(self): #* auhtor: Totte Hansen *#
        """
        Run through all tests sequentially using function calls
        """
        self.check_version

    def check_version(self): #* auhtor: Totte Hansen *#
        point_value_version = 20
        point_value_none = 50

        # no license could be fetched from site
        if self.ssl.license == None:
            self.points += point_value_none
            self.report.append("The website lacks TSL/SSL ensurance")

        elif self.ssl.license not in conf.WHITE_SSL:
            self.points += point_value_version
            self.report.append("The website uses an outdated TSL/SSL license version")


    def __init__(self, url): #* auhtor: Totte Hansen *#
        self.points = 0
        self.report = []

        self.url = url
        self.ssl = ssl_resolve.SSLParse(url)
