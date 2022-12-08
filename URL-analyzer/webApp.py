import src.algorithmManager as am
from flask import Flask, flash, render_template, request, Blueprint

app = Flask(__name__)   
app.config['SECRET_KEY'] = 'HakunaMatataMasualaYoteYatatatuliwa'  

__author__ = "Totte Hansen, Rasmus Andersen"

@app.route("/") #home page
def index():    #home page
    return render_template("index.html")    #home page

@app.route("/check", methods=['GET', 'POST'])
def CheckURL(): 
    try:
        URLinput = str(request.form['URL_input'])

        # return early if empty
        if URLinput.strip() == "":
            empty_url_str = "No URL was given"
            print(empty_url_str)
            return render_template("index.html", output = empty_url_str)
            

        AMObj = am.algorithmManager(URLinput) 
        AMObj.run()
        AMObj.runEvaluations()

        # format output so HTML parsable
        output = AMObj.createOutputString()

    except Exception as e:  #if error
        flash(f"Error: {e}")    #flash error
        raise(e)

    return render_template("index.html", output = output) #render template

def format_report(algo):
    """
    Format report dictionary into HTML table
    """
    ...
