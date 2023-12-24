#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, url_for
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
