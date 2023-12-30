#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, url_for, render_template
from markupsafe import escape
from models import *
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def list_state():
    """display state list"""
    states = storage.all(State)
    states_list = sorted(states.values(),key=lambda state: state.name)
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def close_down(e):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
