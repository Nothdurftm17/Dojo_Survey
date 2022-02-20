from flask import render_template,request, redirect, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/afterSubmit')
    return redirect("/")

@app.route('/afterSubmit')
def index2():
    print("heading to a new route, after submit.")
    return render_template("second.html", dojo = Dojo.get_last_survey(), name = session['name'],location = session['location'], language = session['language'], comment = session['comment'])