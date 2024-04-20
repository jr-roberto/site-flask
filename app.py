from flask import Flask
from flask import render_template, request
import os

app=Flask(__name__)
app.template_folder = os.path.join(os.getcwd(),'templates')
app.static_folder = os.path.join(os.getcwd(),'static')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
