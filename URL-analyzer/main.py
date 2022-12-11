#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import src.algorithmManager as am
import src.algorithmManager as am
from  webApp import app
from sys import argv

#! PLEASE STOP USING MULTIPROCESS WHEN NOT NEEDED!!! IT HAS BUGS !#

def main():
    if argv[1] == "help":
        print("Arguments:\n")
        print(f"Run as webUI: server")
        print(f"")

        # sys.exit(1)
        #! Use return for a pythonic and clean exit (avoid sys when possible)
        return

    else:
        arg1 = argv[1]

        # run as Flask webUI
        if arg1 == "server" or arg1 == None:
            app.run()
            # Process(target=app.run()).start()

        # run as terminal UI 
        elif arg1 == "terminal":
            URL = ""

            while URL != "q":
                try:
                    URL = input('\nEnter q to Quit:\n\
                                 ````````````````\n\
                                 Enter your URL: ')

                    algorithmEngine = am.algorithmManager(URL) #algorithm object

                    output  = "\nFishy?:" + str(algorithmEngine.run()) #fishy or not fishy boolean
                    output += "\nEvaluation points:" + str(algorithmEngine.points)
                    outputDict = algorithmEngine.createOutputString()
                    
                    for i in outputDict:
                        print(i, outputDict[i])

                except Exception as e:
                    print(f"Error: {e}")

        else:
            print("Please don't, just use these two options:")
            print(f"Usage1:  python {argv[0]} server")
            print(f"Usage2:  python {argv[0]} terminal\n")

if __name__ == '__main__':
    main()