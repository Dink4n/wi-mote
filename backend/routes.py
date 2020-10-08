from backend import app
from backend.controller import handle_keypress
from flask import request


@app.route('/keypress')
def keypress():
    key = request.args.get("key")
    handle_keypress(key)

    return 'Done', 202
