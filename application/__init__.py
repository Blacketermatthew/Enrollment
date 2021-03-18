
from flask import Flask

app = Flask(__name__)

# Decorators for functions
@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello Earth!!</h1>"

