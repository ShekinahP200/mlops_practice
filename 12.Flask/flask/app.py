from flask import Flask
##wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this flask course.This should be an amazing course!"

@app.route("/index")
def index():
    return "Welcome to index page "

if __name__ == "__main__":
    app.run(debug = True)
