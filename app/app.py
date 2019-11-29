from flask import Flask
from flask_login import LoginManager

from config import BaseConfig
from db import db as db_instance
from middleware.auth import add_login_manager_functions
from models.Users import User
from routes.api import api
from routes.errors import add_custom_error_pages
from routes.home import home

login_manager = LoginManager()


def run_app():
    app_, db_ = create_app()
    return app_


def create_app():
    app_instance = Flask(__name__, static_url_path='/static')
    app_instance.config.from_object(BaseConfig)
    login_manager.init_app(app_instance)
    add_login_manager_functions(login_manager)

    with app_instance.app_context():
        db_instance.init_app(app_instance)

    # Registering all routes
    app_instance.register_blueprint(home, url_prefix='')
    app_instance.register_blueprint(api, url_prefix='/api')

    # Add custom error pages
    add_custom_error_pages(app_instance)

    return app_instance, db_instance


if __name__ == '__main__':
    app, db = create_app()
    app.run('0.0.0.0')
