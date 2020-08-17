#Building a website with flask
#Import Flask clas from flask lib
#Import render_template method from flask lib
from flask import Flask

application = Flask(__name__)

@application.route('/home_1')
def home_1():
    return "Webiste content goes here!"

@application.route('/about_1')
def about_1():
    return "About website content goes here!"

if __name__ == '__main__':
    application.run(debug = True)