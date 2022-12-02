import src.algorithmManager as am
from flask import Flask, flash, render_template, request, Blueprint
import validators

app = Flask(__name__)   
app.config['SECRET_KEY'] = 'HakunaMatataMasualaYoteYatatatuliwa'  

__author__ = "Totte Hansen, Rasmus Andersen"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=['GET', 'POST'])
def CheckURL(): 
    try:
        URLinput = str(request.form['URL_input'])

        algorithmEngine = am.algorithmManager(URLinput) 

        output = algorithmEngine.createOutputString()
        flash(output)

    except Exception as e:
        flash(f"Error: {e}")

    return render_template("index.html")


def format_report(algo):
    """
    Format report dictionary into HTML table
    """
    ...
