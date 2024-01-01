#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, url_for, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """State, City and Amenity objects must be loaded from DBStorag"""
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda state: state.name)
    amenities = storage.all(Amenity)
    amenity_list = sorted(amenities.values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states_list=states_list, amenity_list=amenity_list)


@app.teardown_appcontext
def close(self):
    """ Method to close the session """
    storage.close()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
