from flask import Flask
from api.initializer import initialize


initialize()
app = Flask(__name__)

from api import routes
