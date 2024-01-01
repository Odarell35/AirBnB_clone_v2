#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, url_for, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """docs"""
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda state: state.name)
    amenities = storage.all(Amenity)
    amenity_list = sorted(amenities.values(), key=lambda amenity: amenity.name)
    places = storage.all(Place)
    place_list = sorted(places.values(), key=lambda place: place.name)
    return render_template("100-hbnb.html", states_list=states_list,
                           amenities_list=amenities_list,
                           places_list=places_list)


@app.teardown_appcontext
def close(self):
    """close the session """
    storage.close()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
