""" Web configurations """
HOST = '127.0.0.0' # aka localhost
PORT = '8000' # aka localhost:8000

""" DB configurations """
DB ="URLanalyzer"
DB_USERNAME ='postgres'
DB_PASSWORD ='root'
DB_HOST ='localhost'
DB_PORT = '5432'

""" Checklist constants """
#Add bad domain keywords to this list:
BAD_KEYWORDS = ["admin", "login", "free", "update", "security", "billing", "check", "notify", "google", "manager", "parcel",
                "collect", "signin", "facebook", "linkedin"]

#Add bad subdomain keywords to this list:
BAD_SUBDOMAINS = ["softhouse", "google", "facebook", "linkedin", "instagram", "update", "information", "storage", "service",
                  "safe", "reporting", "publish", "parcel", "postnord", "logistics", "collect", "free", "robux"]

# This dict generates decides the bad permutations from badKeywords:
REPLACEMENT_CHARACTERS = {"e": "3", "o": "0", "i": "1", "a": "@", "l": "1"}

#Add badCharacters to this list:
BAD_CHARACTERS = [ "$", "#", "£", "0", "3", "8", "1", "_", "=", "!", "@" ]

# bad topdomains!
# bl.a. hämtat från:
# https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links/output/domains/INACTIVE/list
# https://www.statista.com/statistics/1256788/phishing-sites-tlds/
BAD_TOPDOMAINS = ["ru", "cn", "ml", "su", "xyz", "icu", "top"]

#Too long URL!
BAD_URL_LENGTH = 25 #length does not regard pathlength. only subdomain+domain+topdomain.
