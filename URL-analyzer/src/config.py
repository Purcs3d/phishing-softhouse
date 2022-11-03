""" Web configurations """
HOST = '127.0.0.0' # aka localhost
PORT = '8000' # aka localhost:8000

#Add badKeywords to this list:
BAD_KEYWORDS = ["admin", "login", "free", "update", "security", "billing", "check"]

# This dict generates decides the bad permutations from badKeywords:
REPLACEMENT_CHARACTERS = {"e": "3", "o": "0", "i": "1", "a": "@", "l": "1"}

#Add badCharacters to this list:
BAD_CHARACTERS = [ "$", "#", "£", "0", "3", "8", "1", "_", "=", "!", "@" ]
