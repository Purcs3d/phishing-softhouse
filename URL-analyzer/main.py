#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import src.algorithmManager as am
import sys
from  webApp import app
from multiprocessing import Process

def main():

    if len(sys.argv)<3 or len(sys.argv)>3:
        print("Fatal: argument amount invalid.")
        print(f"Usage:  py {sys.argv[0]} server run/close")
        sys.exit(1)
    else:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        if arg1 == "server" and arg2 == "run":
            Process(target=app.run()).start()
        if arg1 == "server" and arg2 == "close":
            app.close()


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