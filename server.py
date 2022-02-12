from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key= 'woodridge'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("afterSubmit")

@app.route('/afterSubmit')
def index2():
    print("heading to a new route, after submit.")
    return render_template("second.html", name = session["name"], location = session["location"], language = session["language"], comments = session["comments"])

if __name__ == "__main__":
    app.run(debug=True, port = 5001)
