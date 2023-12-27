#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, url_for, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_page():
    """display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """displays text"""
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_t(text='is cool'):
    """displays text"""
    text = text.replace("_", " ")
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays number if int"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
