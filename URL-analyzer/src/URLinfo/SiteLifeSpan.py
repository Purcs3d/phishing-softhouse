import whois 
import datetime as dt

def fetchAge(url):
    w = whois.whois(url)
    expires = w.expiration_date
    registed = w.creation_date
    update = w.updated_date
    dateNow = dt.datetime.now()
    active =  dateNow - registed
    print(f"This site have been active for {active} \n Was created {registed} \n Was updated {update} \n Will expire in {expires}")
    return active

def evaluate(time):
    timestr = str(time)
    daysActive = ""
    for i in timestr:
        if(i == ' '):
            break
        else:
            daysActive+=i
    if(int(daysActive) < 2):    
        print("This domain is younger then two days")

