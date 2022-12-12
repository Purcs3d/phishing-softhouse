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

@app.route("/about") 
def about():    
    return render_template("about.html")  

# page after URL input

@app.route("/check", methods=['GET', 'POST'])
def CheckURL(): 
    try:
        URLinput = str(request.form['URL_input'])

        if URLinput.strip() == "":
            empty_url_str = "No URL was given"
            print(empty_url_str)
            return render_template("index.html", output = empty_url_str)
            

        AMObj = am.algorithmManager(URLinput) 
        AMObj.run()
        AMObj.runEvaluations()

        # format output so HTML parsable
        outputDict = AMObj.createOutputString()

    except Exception as e:  #if error
        flash(f"Error: {e}")    #flash error
        raise(e)

    return render_template("index1.html", outputDict = outputDict) #render template
