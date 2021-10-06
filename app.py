from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "bobbuildsburgers" #doesn't matter just keeps error away

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"]) #Just post works as well
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")