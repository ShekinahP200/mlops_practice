from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask course</h1></html>"

@app.route("/index", methods=['GET'])
def show_index():
    return render_template("index.html")

@app.route("/about")
def show_about():
    return render_template("about.html")

@app.route("/submit1",methods = ['GET','POST'])
def submit1():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template("form.html")

#variable rule
@app.route("/success/<int:score>")
def success(score):
    res =""
    if score >=50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template("result.html",result = res)
### for jinja template
@app.route("/successres/<int:score>")
def successres(score):
    res =""
    if score >=50:
        res = "Passed"
    else:
        res = "Failed"

    exp = {"score":score,"res":res}
    return render_template("result1.html",results=exp)
### if jinja template
@app.route("/success1/<int:score>")
def success1(score):
    
    return render_template("result.html", result=score)
    
@app.route("/fail/<int:score>")
def fail(score):
    
    return render_template("result.html", result=score)
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        c = float(request.form['C'])  # Corrected to match the form
        maths = float(request.form['maths'])
        datascience = float(request.form['datascience'])

        total_score = (science + maths + c + datascience) / 4
    else:
        return render_template('getresult.html')

        # Redirect to the success route, passing the total_score as a parameter
    return redirect(url_for('successres', score=total_score))



if __name__ == "__main__":
    app.run(debug=True)
