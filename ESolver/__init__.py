from flask import Flask
from flask_login import login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5c9127e660582dd234b4e8c09c5bc3c1'
    app.config['MESSAGE_FLASHING_OPTIONS'] = {'duration': 5} # set flash duration for 5 seconds
    return app


app = create_app()

from ESolver import routes