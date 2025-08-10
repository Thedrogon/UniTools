from flask import Flask,url_for

from markupsafe import escape

app = Flask(__name__) #object of flask class

@app.route("/")
def hello_world():
    return 'Hey niggas this is Home page'


@app.route("/<name>&&<int:id>")
def get_username(name : str, id : int):
    return f'Username is {escape(name)} and id is {id}' #doing it cozz its a string and preventing url injection attacks

# with app.test_request_context():
#     print(url_for(get_username))
#     print(url_for(hello_world))
