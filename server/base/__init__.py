from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_path='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_path)

    db.init_app(app)
    with app.app_context():
        from base.api import api
        app.register_blueprint(api, url_prefix='/')
        db.create_all()
    return app
