"""
Configurations of global- easy to change- variables 
"""

""" Web configurations """
HOST = '127.0.0.0' # aka localhost
PORT = '5000' # aka localhost:5000

""" DB configurations """
DB ="URLanalyzer"
DB_USERNAME ='postgres'
DB_PASSWORD ='root'
DB_HOST ='localhost'
DB_PORT = '5432'

""" Checklist constants """
#Add bad domain keywords to this list:
BAD_KEYWORDS = ["admin", "login", "free", "update", "security", "billing", "check", "notify", "google", "manager", "parcel",
                "collect", "signin", "facebook", "linkedin", "connect", "tor", "node", "apple", "paypal"]

#Add bad subdomain keywords to this list:
BAD_SUBDOMAINS = ["softhouse", "google", "facebook", "linkedin", "instagram", "update", "information", "storage", "service",
                  "safe", "reporting", "publish", "parcel", "postnord", "logistics", "collect", "free", "robux", "connect", "node", "apple", "paypal"]

# This dict generates decides the bad permutations from badKeywords:
REPLACEMENT_CHARACTERS = {"e": "3", "o": "0", "i": "1", "a": "@", "l": "1"}

#Add badCharacters to this list:
BAD_CHARACTERS = [ "$", "#", "£", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "=", "!", "@" ]

# bad topdomains!
# bl.a. hämtat från:
# https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links/output/domains/INACTIVE/list
# https://www.statista.com/statistics/1256788/phishing-sites-tlds/
BAD_TOPDOMAINS = ["ru", "cn", "ml", "su", "xyz", "icu", "top"]

#Too long URL!
BAD_URL_LENGTH = 25 #length does not regard pathlength. only subdomain+domain+topdomain.

""" SSL/TSL """

BAD_CERT_VERSIONS = ["SSL1.0", "SSL2.0", "SSL3.0", "TLSv1.0", "TLSv1.1", "TLSv1.2"]
# list of whitelisted SSL/TSL license versions
MIN_CERT_VER = 2 #? TLSv1.2 is permitted some bigger sites still use it
# whitelisted "safe" hashing algorithms used on the cert
WHITE_CRT_HASH = []
# minimum age a license should be without being triggered as phishy (in days)
MIN_CRT_AGE = 30
# Some dodgy country codes, https://www.digicert.com/kb/ssl-certificate-country-codes.htm
BAD_CERT_COUNTRYCODES = ["AF", "LY", "RU"]
