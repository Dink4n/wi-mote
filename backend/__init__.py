from flask import Flask
from backend.initializer import initialize


initialize()
app = Flask(__name__, static_folder="../volume-changer/build/static",
            template_folder="../volume-changer/build")

from backend import routes
