from flask import Flask
from wi_mote.initializer import initialize


def main():
    pass


initialize()
app = Flask(__name__)

from wi_mote import routes

app.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    main()
