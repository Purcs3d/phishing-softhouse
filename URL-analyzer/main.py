#!/usr/bin/env python
# -*- coding: utf-8 -*-

import src.algorithmManager as am
from  webApp import app
from sys import argv

#! PLEASE STOP USING MULTIPROCESS WHEN NOT NEEDED!!! IT HAS BUGS !#

def main():
    # run as Flask webUI
    if len(argv) < 2 or argv[1] == "server":
        app.run()
        # Process(target=app.run()).start()

    # run as terminal UI
    elif len(argv) > 0 and argv[1] == "terminal":
        URL = ""

        while URL != "q":
            try:
                URL = input('\nEnter q to Quit:\
                             \n````````````````\
                             \nEnter your URL: ')

                algorithmEngine = am.algorithmManager(URL) #algorithm object

                outputDict = algorithmEngine.createOutputString()
                if type(outputDict) == str:
                    print(outputDict)
                else:
                    for i in outputDict:
                        print(i, outputDict[i])

            except Exception as e:
                print(f"Error: {e}")

    else:
        print("Arguments:\n")
        print(f"Run as webUI: server")
        print(f"")

        # sys.exit(1)
        #! Use return for a pythonic and clean exit (avoid sys when possible)
        return

if __name__ == '__main__':
    main()
