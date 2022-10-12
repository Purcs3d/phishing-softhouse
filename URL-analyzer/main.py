#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import "src/algorithmManager.py"
import src.algorithmManager as am
import src.URLinfo.SiteLifeSpan as sl

def main():
    #Website
    URLstring = "https://www.svt.se"

    #URL-analyzing
    #ex = am.algorithmManager(URLstring) #create object
    #ex.printMsg()
    #am.getURLinfo() #create the URL
    z = sl.fetchAge(URLstring)



if __name__ == '__main__':
    main()
