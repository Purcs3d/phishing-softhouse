""" Web configurations """
HOST = '127.0.0.0' # aka localhost
PORT = '8000' # aka localhost:8000

""" checklist constants"""
#Add badKeywords to this list:
BAD_KEYWORDS = ["admin", "login", "free", "update", "security", "billing", "check"]

# This dict generates decides the bad permutations from badKeywords:
REPLACEMENT_CHARACTERS = {"e": "3", "o": "0", "i": "1", "a": "@", "l": "1"}

#Add badCharacters to this list:
BAD_CHARACTERS = [ "$", "#", "£", "0", "3", "8", "1", "_", "=", "!", "@" ]

# bad topdomains!
# bl.a. hämtat från:
# https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links/output/domains/INACTIVE/list
# https://www.statista.com/statistics/1256788/phishing-sites-tlds/
BAD_TOPDOMAINS = [".ru", ".cn", ".ml", ".su", ".xyz",".icu", ".top"]
