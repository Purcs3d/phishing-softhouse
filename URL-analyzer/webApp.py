import src.algorithmManager as am
from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HakunaMatataMasualaYoteYatatatuliwa'

__author__ = "Totte Hansen, Rasmus Andersen, Mohammad"

#home page
@app.route("/")
def index() -> None:
    """
    Renders the fontpage according to index without parameters
    """
    return render_template("index.html")

# page after URL input
@app.route("/check", methods=['GET', 'POST'])
def CheckURL():
    """
    Runs algoritm manager and formats the terun value to be rendered on index
    """
    try:
        URLinput = str(request.form['URL_input'])

        # return early if empty
        if URLinput.strip() == "":
            empty_url_str = "No URL was given"
            print(empty_url_str)
            return render_template("index.html", output = empty_url_str)

        # check URL against algomanager
        AMObj = am.algorithmManager(URLinput)
        AMObj.run()

        # format algomanager output
        outputDict = AMObj.createOutputString()
        PendingDeprecationWarning
    except Exception as e:
        # return error string
        flash(f"Error: {e}")
        raise(e)

    from pprint import pprint
    pprint(outputDict)

    return render_template("index.html", output = outputDict) #render template

def format_report(algo):
    """
    Format report dictionary into HTML table
    """
    ...
