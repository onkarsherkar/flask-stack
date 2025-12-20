from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello Flask</h1>"


@app.route("/home", methods=["GET"])
def home():
    return "<h2>Home</h2>"


@app.route("/json")
def json():
    return {"mykey": "json value!", "mylist": [1, 2, 3, 4]}
