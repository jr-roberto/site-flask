from flask import Flask, jsonify
from flask import render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app=app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cad_produto")
def cad_produto():
    return render_template("cad_produto.html")

@app.route("/data")
def data():
    return jsonify([{"coluna1":1,"coluna2":"Dados 1"},{"coluna1":3,"coluna2":"Dados 3"}])
