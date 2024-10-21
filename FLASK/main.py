from flask import Flask, render_template, jsonify, request

productos = [
    {
        "id": 1,
        "nombre": "manzana",
        "cantidad": 12
    },
    {
        "id": 2,
        "nombre": "pera",
        "cantidad": 20
    }
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("indes.html")

@app.route("/productos", methods=["GET"])
def getproducts():
    return jsonify(productos)

@app.route("/productos", methods=["POST"])
def postproductos():
    nuevoProducto = request.json
    productos.append(nuevoProducto)
    return "Producto agregado correctamente!"

app.run()