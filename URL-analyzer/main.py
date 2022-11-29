# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import src.algorithmManager as am
# import io
# import sys
# from flask import Flask, flash, render_template, request



# def func(input):
#     val = am.algorithmManager(input)
#     old_stdout = sys.stdout
#     new_stdout = io.StringIO()
#     sys.stdout = new_stdout
#     print(val.run())
#     output = new_stdout.getvalue()
#     sys.stdout = old_stdout
#     output = output.replace('\n', '<br>')
#     return output


# def main():

#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'asdsdgtrbfgbrdfsdf'

#     @app.route("/")
#     def index():
#         return render_template("index.html")

#     @app.route("/check", methods=['GET', 'POST'])
#     def CheckURL():
#         URLinput = str(request.form['URL_input'])
#         flash(func(URLinput))
#         return render_template("index.html")
#     app.run(debug=True)




#     #Website
#     # if len(sys.argv)<2 or len(sys.argv)>2: #2 arguments only.
#     #     print("Fatal: argument amount invalid.")
#     #     print(f"Usage:  py {sys.argv[0]} URLinput.ex")
#     #     sys.exit(1)
#     # else:
#     #     URLstring = sys.argv[1]


#     # #URL-analyzing
#     # print("_"*20)
#     # print("Information fetched:\n")
#     # ex = am.algorithmManager(URLstring)
#     # print("\n" + "_"*20,"\n" + "Is website fishy?",ex.run())


# if __name__ == '__main__':
#     main()


from src.server_check import SSL_resolve as ssl_lib
from pprint import pprint
from src.checklists.SSLCL import SSL_CL as ssl_cl

addr = "http://facebook.com"

cert_wrap = ssl_lib.ssl_parser(addr)
# cl = ssl_cl(addr)

pprint(cert_wrap.cert)
# print(cert_wrap.check_version())

