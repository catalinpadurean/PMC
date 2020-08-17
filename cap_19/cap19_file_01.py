#Adding navigation menu

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