from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>PRINCIPAL</h1>"

@app.route("/hola")
def hola():
    return "<h1>saludos</h1>"
app.run()