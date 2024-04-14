#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask

application = Flask(__name__)


@application.route("/", strict_slashes=False)
def hello():
    """ Returns string when accessing the root route of web server """
    return "Hello HBNB!"


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
