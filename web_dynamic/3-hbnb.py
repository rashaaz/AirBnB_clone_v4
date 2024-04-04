#!/usr/bin/python3
"""This script initializes a Flask application for a web service
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage.
    """
    storage.close()


@app.route('/3-hbnb/')
def hbnb_filters(the_id=None):
    """Render the HBNB filters.
    """
    st_objs = storage.all('State').values()
    sts = dict([state.name, state] for state in st_objs)
    ams = storage.all('Amenity').values()
    pls = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('3-hbnb.html',
                           sts=sts,
                           ams=ams,
                           pls=pls,
                           users=users, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """Run the application."""
    app.run(host=host, port=port, threaded=True)
