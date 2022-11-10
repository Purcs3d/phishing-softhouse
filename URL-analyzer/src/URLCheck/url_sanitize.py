""" 
Allows for formatting options and sanity checks (such as URL server existance)
in regards to URL
"""

import requests
from url_parser import get_url
from urllib import request

def siteValid(url:str, redir:bool = True) -> bool:
    """
    Checks if a site exists and is reachable
    Requires supplied schema
    """
    url = addScheme(url, redir)

    site_code = 0
    try:
        site_code = request.urlopen(url).getcode()
        print(site_code)

        # check if site response is within OK range
        if 200 <= site_code <= 299:
            return True

    except Exception as err:
        code = err.__dict__['code']
        # Check if server or client error occured (raise error in case of client error)
        if 500 <= code <= 599:
            return False

        else:
            raise err


def addScheme(url:str, fetch:bool = True) -> str:
    """ 
    Checks if the address holds a
    """
    schema = get_url(url).protocol
    if schema == None:
        # add http as "starting point"
        prot_url = 'http://' + url
    
    # fetch server requested scheme (if reachable)
    if fetch:
        try:
            prot_url = getRedir(prot_url)
        
        except:
            # try reachability using 'https' if 'http' fail
            try:
                prot_url = 'https://' + url
                prot_url = getRedir(prot_url)

            # return error in case http types fail
            except Exception as err:
                raise err

    return url


def getRedir(addr:str) -> str:
    #TODO does not fetch json redirects correctly (such as http://google.com -> https://consent.google.com/ml?continue=https://www.google.com/&gl=SE&m=0&pc=shp&uxe=none&hl=sv&src=1)
    """ 
    Fetches URL after server redirects.
    """
    connection = requests.get(addr)
    return connection.url

URL  = 'www.amazon.com'

print(siteValid(URL))