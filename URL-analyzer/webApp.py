import src.algorithmManager as am
from flask import Flask, flash, render_template, request, Blueprint

app = Flask(__name__)   
app.config['SECRET_KEY'] = 'HakunaMatataMasualaYoteYatatatuliwa'  

__author__ = "Totte Hansen, Rasmus Andersen"

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/") #home page
def index():    #home page
    return render_template("index.html")    #home page

@app.route("/check", methods=['GET', 'POST'])
def CheckURL(): 
    try:
        URLinput = str(request.form['URL_input'])

        algorithmEngine = am.algorithmManager(URLinput) 

        output = algorithmEngine.createOutputString()   #create output string
        flash(output)   #flash output string

    except Exception as e:  #if error
        flash(f"Error: {e}")    #flash error

    return render_template("index.html")

def format_report(algo):
    """
    Format report dictionary into HTML table
    """
    ...