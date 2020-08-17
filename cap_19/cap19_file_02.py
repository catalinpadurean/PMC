"""In this lecture we will add CSS styling to the webpage. Sometimes, when you make a change to the CSS file and reload the webpage, the changes are not shown because the browser uses the previous cached styling. If this happens, open the browser in private (incognito) mode and load the webpage there."""
#Python looks for static files in the static folder
#In HTML the visibile part of the HTML code goes in body part and links go outside of it.
#Import render_template method from flask lib
from flask import Flask, render_template
application = Flask(__name__)
#Pass html template to python web app

@application.route('/')
def home():
    return render_template("home.html")

@application.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    application.run(debug = True)