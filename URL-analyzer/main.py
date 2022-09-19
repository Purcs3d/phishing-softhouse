#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import "src/algorithmManager.py"
import src.algorithmManager as am


def main():
    #Website
    URLstring = "svt.se"

    #URL-analyzing
    ex = am.algorithmManager(URLstring) #create object
    ex.printMsg()
    #am.getURLinfo() #create the URL




if __name__ == '__main__':
    main()
