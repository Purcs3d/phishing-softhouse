#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import "src/algorithmManager.py"
import src.algorithmManager as am


def main():
    #Website
    URLstring = "info.cern.ch"

    #URL-analyzing
    ex = am.algorithmManager(URLstring) #create object
    print(ex.runEvalAlgo())
    #am.getURLinfo() #create the URL




if __name__ == '__main__':
    main()
