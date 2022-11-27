import src.algorithmManager as am
from flask import Flask, flash, render_template, request, Blueprint
import validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HakunaMatataMasualaYoteYatatatuliwa'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=['GET', 'POST'])
def CheckURL():
    try:
        URLinput = str(request.form['URL_input'])
        if validators.domain(URLinput) == True or validators.url(URLinput) == True:
            algorithmEngine = am.algorithmManager(URLinput) #algorithm object
            output = "fishy?:" + str(algorithmEngine.run()) #fishy or not fishy boolean
            output += "<br> evaluation points:" + str(algorithmEngine.points)
            output += algorithmEngine.createOutputString()
            flash(output)
        else:
            flash("Please enter a valid URL")
    except Exception:
        flash("Something is broken in the backend")
    return render_template("index.html")
