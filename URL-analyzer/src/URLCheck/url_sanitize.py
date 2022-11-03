""" 
Allows for formatting options and sanity checks (such as URL server existance)
in regards to URL
"""

import requests

def addScheme(url:str) -> str:
    """ 
    Checks if the address holds a
    """
    ...


def getRedir(addr:str) -> str:
    #TODO does not fetch json redirects correctly (such as http://google.com -> https://consent.google.com/ml?continue=https://www.google.com/&gl=SE&m=0&pc=shp&uxe=none&hl=sv&src=1)
    """ 
    Fetches URL after server redirects.
    """
    connection = requests.get(addr)
    return connection.url


print(getRedir("googl.com"))