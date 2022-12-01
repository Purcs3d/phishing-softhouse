#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import src.algorithmManager as am
import sys
import src.algorithmManager as am
import validators
from  webApp import app
from multiprocessing import Process

def main():
    if len(sys.argv)<2 or len(sys.argv)>2:
        print("\nUse these two options:")
        print(f"Usage1:  python {sys.argv[0]} server")
        print(f"Usage2:  python {sys.argv[0]} terminal\n")
        sys.exit(1)
    else:
        arg1 = sys.argv[1]
        if arg1 == "server" and len(sys.argv) == 2:
            Process(target=app.run()).start()
        elif arg1 == "terminal" and len(sys.argv) == 2:
            URL = ""
            while URL != "q":
                try:
                    URL = input('\nEnter q to Quit:\n````````````````\nEnter your URL: ')
                    if validators.domain(URL) == True or validators.url(URL) == True:
                        algorithmEngine = am.algorithmManager(URL) #algorithm object
                        output = "\nFishy?:" + str(algorithmEngine.run()) #fishy or not fishy boolean
                        output += "\nEvaluation points:" + str(algorithmEngine.points)
                        output += algorithmEngine.createOutputString()
                        finalOutput = output.replace("<br>", "\n" )
                        print(finalOutput)
                    else:
                        print("The URL input is not valid\n")
                except Exception as e:
                    print(f"Error: {e}")
        else:
            print("\nPlease don't, just use these two options:")
            print(f"Usage1:  python {sys.argv[0]} server")
            print(f"Usage2:  python {sys.argv[0]} terminal\n")
        sys.exit(1)

if __name__ == '__main__':
    main()


# from  webApp import app
# from waitress import serve

# def main():

#     if len(sys.argv)<3 or len(sys.argv)>3:
#         print("Fatal: argument amount invalid.")
#         print(f"Usage:  py {sys.argv[0]} server run/close")
#         sys.exit(1)
#     else:
#         arg1 = sys.argv[1]
#         arg2 = sys.argv[2]
#         if arg1 == "server" and arg2 == "run":
#             serve(app, host='0.0.0.0', port=5000, threads=8)
#             app.run(debug=True) 

#         if arg1 == "server" and arg2 == "close":
#             app.close()


# if __name__ == '__main__':
#     main()

#########################################
# nohup python main.py > log.txt 2>&1 &
# pm2 start main.py --interpreter python3
# forever start -c python main.py

#########################################
########    Test Links           ########
#########################################
    
# Valid Links 
# https://www.google.com/
# www.google.com
# google.com

# Internal Server Error 500
# https://log1nkarlskronahem.se/kontakt/