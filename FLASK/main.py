from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hola/<user>")
def hola(user):
    return render_template("hola.html", nombre=user)

@app.route("/usuarios", methods=["GET"])
def usuarios():
    usuarios = [
        {"id": 1, 
         "username":"yo",
         "email": "user1@gmail.com"},
        {"id": 2, 
         "username":"yo2",
         "email": "user2@gmail.com"}
    ]
    return jsonify(usuarios)
app.run()