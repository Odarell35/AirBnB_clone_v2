#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, url_for, render_template
from models.state import State
from models import storage
app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def list_state():
    """display state list"""
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda state: state.name)
    return render_template('states_list.html', states_list=states_list)


@app.route('/states/<id>', strict_slashes=False)
def detail_state(id):
  """diplays state by id"""
  if id is not none:
    states = storage.all(State).values()
    for state in states:
      if state.id == id:
        cities = sorted(states.cities, key=lambda x: x.name)
        return render_template('9-states.html', states=state, cities=cities, mode='id')
      else:
        return render_template('9-states.html', states=state, cities=cities, mode='none')
  else:
    return render_template('9-states.html', states=state, cities=cities, mode='none)


@app.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
