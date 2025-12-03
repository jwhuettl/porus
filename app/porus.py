import os
import dotenv

from flask import Flask

def create_app():

  app = Flask(os.environ.get("APP_NAME"), instance_relative_config=True)

  app.config.from_mapping(
    SECRET_KEY=os.environ.get("SECRET_KEY")
    DATABASE=os.environ.get("DATABASE")
  )

  # mkdir (we will use instance as tmp)
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  return app