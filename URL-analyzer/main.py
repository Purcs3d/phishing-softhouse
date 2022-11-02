#!/usr/bin/env python
# -*- coding: utf-8 -*-
import src.algorithmManager as am


def main():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdsdgtrbfgbrdfsdf'

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/check", methods=['GET', 'POST'])
    def CheckURL():
        URLinput = str(request.form['URL_input'])
        flash(func(URLinput))
        return render_template("index.html")
    app.run(debug=True)




    #Website
    URLstring = "svt.se"

    #URL-analyzing
    ex = am.algorithmManager(URLstring) #create object
    ex.printMsg()
    #am.getURLinfo() #create the URL


    # #URL-analyzing
    # print("_"*20)
    # print("Information fetched:\n")
    # ex = am.algorithmManager(URLstring)
    # print("\n" + "_"*20,"\n" + "Is website fishy?",ex.run())


if __name__ == '__main__':
    main()
