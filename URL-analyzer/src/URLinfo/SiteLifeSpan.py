import whois
import datetime as dt

def fetchAge(url):
    w = whois.whois(url)
    expires = w.expiration_date
    registed = w.creation_date
    update = w.updated_date
    dateNow = dt.datetime.now()
    print(dateNow)
    active =  dateNow -registed
    print(f"This site have been active for {active} \n was created {registed} \n was updated {update} \n will expire in {expires}")
