from backend import app
from backend.controller import handle_keypress
from flask import request, render_template


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/keypress')
def keypress():
    key = request.args.get("key")
    status = "ERROR"

    if handle_keypress(key):
        status = "OK"

    return {
        "key": key,
        "status": status
    }
