import src.algorithmManager as am
from flask import Flask, flash, render_template, request, Blueprint

app = Flask(__name__)   
app.config['SECRET_KEY'] = 'HakunaMatataMasualaYoteYatatatuliwa'    

@app.route("/") #home page
def index():    #home page
    return render_template("index.html")    #home page

@app.route("/check", methods=['GET', 'POST'])  #check page 
def CheckURL(): #check page
    try:
        URLinput = str(request.form['URL_input'])   #get URL from form

        algorithmEngine = am.algorithmManager(URLinput) #algorithm object
        fishy = algorithmEngine.run()   #fishy or not fishy boolean

        output = algorithmEngine.createOutputString()   #create output string
        flash(output)   #flash output string

    except Exception as e:  #if error
        flash(f"Error: {e}")    #flash error

    return render_template("index.html")    #render home page
