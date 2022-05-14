#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def intt(n):
    """/number/<int:n>

    Args:
        n (int): <int:n>

    Returns:
        str: "<int:n> is a number"
    """
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    """/number_template/<int:n>

    Args:
        n (int): <int:n>

    Returns:
        html: render html template
    """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """/number_odd_or_even/<int:n>

    Args:
        n (int): <int:n>

    Returns:
        template: html template 6-number_odd_or_even.html
    """
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html",
                               num="{} is even".format(n))
    else:
        return render_template("6-number_odd_or_even.html",
                               num="{} is odd".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
