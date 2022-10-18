#!/usr/bin/env python
# -*- coding: utf-8 -*-
import src.algorithmManager as am
from website import create_app

import sys

def main():

    # app = create_app() #kommenterade ut denna medans jag skrev CLI
    # app.run(debug=True)
    #Website
    if len(sys.argv)<2 or len(sys.argv)>2: #2 arguments only.
        print("Fatal: argument amount invalid.")
        print(f"Usage:  py {sys.argv[0]} URLinput.ex")
        sys.exit(1)
    else:
        URLstring = sys.argv[1]


    #URL-analyzing
    print("_"*20)
    print("Information fetched:\n")
    ex = am.algorithmManager(URLstring)
    print("\n" + "_"*20,"\n" + "Is website fishy?",ex.run())


if __name__ == '__main__':
    main()
