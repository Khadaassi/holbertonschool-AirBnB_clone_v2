#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask

application = Flask(__name__)


@application.route("/", strict_slashes=False)
def hello():
    """ Returns string when accessing the root route of web server """
    return "Hello HBNB!"


@application.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns string when accessing the /hbnb route of web server """
    return "HBNB"


@application.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Returns string when accessing the /c/<text> route of web server """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
