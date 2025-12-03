
from flask import (
  Blueprint, g, render_template, request
)

from gtfs.realtime import get_alerts

from app.db import get_db

blueprint = Blueprint('alert', __name__, url_prefix='/alerts')

@blueprint.route('/all', methods=('GET'))
def alerts():

  data = get_alerts()

  print(data)
