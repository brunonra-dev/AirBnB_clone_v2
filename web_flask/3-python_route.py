#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """index

    Returns:
        string: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbhb

    Returns:
        string: HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """/c/<text>

    Args:
        text (string): <text> on route

    Returns:
        string: "C <text>"
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """/python/<text>

    Args:
        text (str, optional): <text>. Defaults to "is cool".

    Returns:
        str: "Python <text>"
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
