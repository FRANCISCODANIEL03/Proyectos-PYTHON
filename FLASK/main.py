from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hola/<user>")
def hola(user):
    return render_template("hola.html", nombre=user)
app.run()