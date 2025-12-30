from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime)


@app.route("/")
def index():
    return render_template("index.html", page_name="index", page_no=1)


@app.route("/home", methods=["GET"])
def home():
    return render_template(
        "home.html",
        number=5,
        data=[
            {"SUN": 1},
            {"MON": 2},
            {"TUE": 3},
            {"WED": 4},
            {"THU": 5},
            {"FRI": 6},
            {"SAT": 7},
        ],
    )


@app.route("/json")
def json():
    return {"mykey": "json value!", "mylist": [1, 2, 3, 4]}


@app.route("/dynamic", defaults={"user_input": "default"})
@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    return f"<h2>The usered eneter text:{user_input} </h2>"


@app.route("/query")
def query():
    first = request.args.get("first")
    second = request.args.get("second")
    return f"<h1>The query string contains: {first} and {second}</h1>"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        return f"<h1>User input: {user_input}</h1>"
    return (
        '<form method="post">'
        '<input type="text" name="user_input" />'
        '<input type="submit" />'
        "</form>"
    )


@app.route("/jsondata")
def jsondata():
    json_data = request.get_json()
    # api_input = json
    return {"api_data": json_data}


@app.route("/error")
def error():
    a = 1 / 0
    return "error"


def insert_data():
    from datetime import datetime

    new_user = User(name="Tom", date_joined=datetime.now())
    db.session.add(new_user)
    db.session.commit()


def update_first_user():
    user = User.query.first()
    user.name = "Flask User"
    db.session.commit()
