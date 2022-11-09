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
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    print("Conclusion, fishy?",am.algorithmManager(URLinput).run())
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    output = output.replace('\n', '<br>')
    flash(output)
    return render_template("index.html")

