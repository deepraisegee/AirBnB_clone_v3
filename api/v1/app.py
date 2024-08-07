#!/usr/bin/python3
"""Flask Application base module"""

import os

from flask import Flask

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(db):
    """cloose the db"""
    storage.close()


if __name__ == "__main__":
    HOST = os.getenv("HBNB_API_HOST", "0.0.0.0")
    PORT = os.getenv("HBNB_API_PORT", 5000)
    app.run(HOST, PORT, threaded=True)
