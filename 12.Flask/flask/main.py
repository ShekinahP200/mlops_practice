from flask import Flask,render_template
##wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to home page</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug = True)
