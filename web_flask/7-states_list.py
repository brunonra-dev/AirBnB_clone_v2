#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tear_db(exception):
    """Closing DB"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """/states_list

    Returns:
        html: html template states list
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)