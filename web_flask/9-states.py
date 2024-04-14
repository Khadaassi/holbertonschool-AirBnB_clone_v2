#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_ls_noID():
    """ Displays a HTML page with a list of all State objects """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Displays a HTML page with State """
    states = storage.all(State)
    state_id = "State." + id if id else None
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close_session(self):
    """ Closes the session after each request """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
