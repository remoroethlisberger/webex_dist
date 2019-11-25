from flask import Flask
from config import BaseConfig
from db import db
from routes.home import home


def create_app():
    app_instance = Flask(__name__, static_url_path='/static')
    app_instance.config.from_object(BaseConfig)
    db.init_app(app_instance)

    # Registering all routes
    app_instance.register_blueprint(home, url_prefix='')

    return app_instance


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0')
