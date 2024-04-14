#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays a HTML page with a list of all State objects """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Returns a list of cities by states """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(self):
    """ Closes the session after each request """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
