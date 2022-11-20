""" 
Allows for formatting options and sanity checks (such as URL server existance)
in regards to URL
"""

import requests
from url_parser import get_url
from urllib import request
from urlparse import urlparse

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
        else:
            return False

    except Exception as err:
        # Check if server or client error occured (raise error in case of client error)
        return False


def addScheme(url:str, fetch:bool = True) -> str:
    """ 
    Checks if the address holds a
    """
    prot_url = url
    prot = get_url(url).protocol
    if prot == None:
        # add http as "starting point"
        prot_url = 'http://' + url
    
    # fetch server requested scheme (if reachable)
    if fetch and siteValid(prot_url, redir=False):
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

    return prot_url

def rm_scheme(url:str):
    prot = get_url(url).protocol()
    if prot != None:
        return url

    else:
        parsed = urlparse(url)
        scheme = "%s://" % parsed.scheme
        return parsed.geturl().replace(scheme, '', 1)

def getRedir(addr:str) -> str:
    #TODO does not fetch json redirects correctly (such as http://google.com -> https://consent.google.com/ml?continue=https://www.google.com/&gl=SE&m=0&pc=shp&uxe=none&hl=sv&src=1)
    """ 
    Fetches URL after server redirects.
    """
    connection = requests.get(addr)
    return connection.url

URL  = 'ww7.youtube.com'
