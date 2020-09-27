from flask import Flask
from backend.initializer import initialize


initialize()
app = Flask(__name__)

from backend import routes
