"""
@author: Totte Hansen, DVADS20h

Checklist and tests associated with SSL/TSL attributes
"""

from src.server_check import ssl_resolve
import URLCheck

__author__ = 'Totte Hansen, DVADS20h'

class SSL_CL:
    def run_evaluation(self): #* auhtor: Totte Hansen
        """
        Run through all tests sequentially using function calls
        """

    def check_con(self):
        point_value = 50

        if self.ssl.license == None:
            return point_value

    def check_version(self): #* auhtor: Totte Hansen
        point_value = 20

    def __init__(self, url): #* auhtor: Totte Hansen
        self.url = url
        self.ssl = ssl_resolve.SSLParse(url)
