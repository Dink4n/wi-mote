from backend import app
from backend.controller import handle_keypress
from flask import request, render_template


@app.route("/")
def index():
    '''
    Serves the index page on /
    '''
    return render_template("index.html")


@app.route("/keypress")
def keypress():
    '''
    Listens on /keypress for key presses.
    '''
    key = request.args.get("key")
    handle_keypress(key)

    return 'Done', 202
