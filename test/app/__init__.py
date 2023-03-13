from .extensions import db,login_manager
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1a8c97a7764c60af5b2f8bede7953cf9'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'You have to login first before accessing the app'
    login_manager.login_message_category = 'warning'
    return app

app = create_app()

from . import views