import algorithmManager

def main():
    #Website
    URLstring = "svt.se"

    #URL-analyzing
    am = algorithmManager(URLstring)
    am.getURLinfo() #create the URL




if __name__ == '__main__':
    main()
