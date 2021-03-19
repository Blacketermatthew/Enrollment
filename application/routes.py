from application import app
from flask import render_template


# Decorators for functions
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
