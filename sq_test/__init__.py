from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(conf_env: str):
    app = Flask(__name__)
    app.config.from_object(config(conf_env))

    from sq_test.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    db.init_app(app)

    return app
