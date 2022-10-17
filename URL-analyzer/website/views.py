from flask import Blueprint, flash, render_template, request

views = Blueprint('views', __name__)
# URLinput = 'aa'

@views.route("/")
def index():
	flash("Enter The URL:")
	return render_template("index.html")

@views.route("/check", methods=['POST'])
def CheckURL():
    URLinput = str(request.form['URL_input'])
    flash(URLinput + " has been checked")
    return render_template("index.html"), URLinput
