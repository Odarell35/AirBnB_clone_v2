#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, url_for, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_city_by_state():
    """display city list"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def close_down(e):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
