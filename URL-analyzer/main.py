#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import src.algorithmManager as am
import sys
import src.algorithmManager as am
from  webApp import app
from multiprocessing import Process

def main():
    # if len(sys.argv)<2 or len(sys.argv)>2:
    #     print("\nUse these two options:")
    #     print(f"Usage1:  python {sys.argv[0]} server")
    #     print(f"Usage2:  python {sys.argv[0]} terminal\n")

    #     sys.exit(1)

    # else:
    #     arg1 = sys.argv[1]

    #     if arg1 == "server" and len(sys.argv) == 2:
            Process(target=app.run()).start()

        # elif arg1 == "terminal" and len(sys.argv) == 2:
        #     URL = ""

        #     while URL != "q":
        #         try:
        #             URL = input('\nEnter q to Quit:\n\
        #                          ````````````````\n\
        #                          Enter your URL: ')

        #             algorithmEngine = am.algorithmManager(URL) #algorithm object

        #             output  = "\nFishy?:" + str(algorithmEngine.run()) #fishy or not fishy boolean
        #             output += "\nEvaluation points:" + str(algorithmEngine.points)
        #             outputDict = algorithmEngine.createOutputString()
                    
        #             for i in outputDict:
        #                 print(i, outputDict[i])

        #         except Exception as e:
        #             print(f"Error: {e}")

        # else:
        #     print("Please don't, just use these two options:")
        #     print(f"Usage1:  python {sys.argv[0]} server")
        #     print(f"Usage2:  python {sys.argv[0]} terminal\n")

        # sys.exit(1)

if __name__ == '__main__':
    main()