import whois
import datetime as dt

def fetchAge(url):
    w = whois.whois(url)
    expires = w.expiration_date
    registed = w.creation_date
    update = w.updated_date
    dateNow = dt.datetime.now()
    active =  dateNow - registed
    print("This site have been active for {active} \n Was created {registed} \n Was updated {update} \n Will expire in {expires}")
    