from backend import app
from backend.controller import handle_keypress
from flask import request


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
