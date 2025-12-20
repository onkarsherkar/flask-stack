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


@app.route("/dynamic", defaults={"user_input": "default"})
@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    return f"<h2>The usered eneter text:{user_input} </h2>"
