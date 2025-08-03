from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hey niggas</h1>"


@app.route("/<name>&&<int:id>")
def get_username(name : str, id : int):
    return f'Username is {escape(name)} and id is {id}' #doing it cozz its a string and preventing url injection attacks