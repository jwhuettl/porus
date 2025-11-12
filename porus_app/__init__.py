from flask import Flask
import os
from dotenv import load_dotenv
from porus_app.api import alert


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.register_blueprint(alert.blueprint)

    app.config.from_mapping(
      SECRET_KEY = os.environ.get('SECRET_KEY')
    )

    return app
