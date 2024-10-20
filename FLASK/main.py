from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hola")
def hola():
    return "<h1>saludos</h1>"
app.run()