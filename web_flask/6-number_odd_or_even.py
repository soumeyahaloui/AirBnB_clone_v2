#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0, port 5000,
and defines routes with strict_slashes=False.
"""

from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route that displays 'C ', followed by the value of the text variable
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route that displays 'Python ', followed by the value of the text variable
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route that displays 'n is a number' only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that displays an HTML page only if n is an integer:
    """
    return render_template('6-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route that displays an HTML page only if n is an integer and
    determines if it's odd or even.
    """
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
