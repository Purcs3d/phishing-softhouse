
import whois
import datetime as dt



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
    elif(int(daysActive) > 365):
        print("This site is over a year old")

