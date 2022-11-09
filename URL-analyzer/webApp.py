import io
import sys
import src.algorithmManager as am
from flask import Flask, flash, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'HakunaMatataMasualaYoteYatatatuliwa'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=['GET', 'POST'])
def CheckURL():
    URLinput = str(request.form['URL_input'])
    algorithmEngine = am.algorithmManager(URLinput) #algorithm object
    output = "fishy?:" + str(algorithmEngine.run()) #fishy or not fishy boolean
    output += "<br> evaluation points:" + str(algorithmEngine.points)
    output += algorithmEngine.createOutputString()
    flash(output)
    return render_template("index.html")
