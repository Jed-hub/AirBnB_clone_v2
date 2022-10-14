#!/usr/bin/python3
"""script to start a flask app on localhost
"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """Storage.close() closes the sql scoped session or reloads file
            storage.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def conditional_templating(n=None):
    """checking input data using templating"""
    return render_template('7-states_list.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
