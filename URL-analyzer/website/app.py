
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "asecretkey"

@app.route("/")
def index():
	flash("Enter The URL:")
	return render_template("index.html")

@app.route("/check", methods=['POST'])
def CheckURL():
	flash(str(request.form['URL_input']) + " has been checked")
	return render_template("index.html")
