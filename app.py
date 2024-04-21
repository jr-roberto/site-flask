from flask import Flask
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
