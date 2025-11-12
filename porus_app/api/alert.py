from flask import Blueprint, flash, g, render_template, url_for

from porus_app.helpers.api_helper import handle_request

import sys


blueprint = Blueprint('alert', __name__, url_prefix='/alerts')

def get_all_alerts():
  
  endpoint = '/alerts/all'
  response = handle_request(endpoint)

  return response

def get_alert(alert_id):

  endpoint = '/alerts/alert/' + alert_id
  response = handle_request(endpoint)

  return response


@blueprint.route("/all", methods=["GET"])
def index():

  all_alerts = get_all_alerts()

  if (all_alerts['error']):
    # flash error message
    error = all_alerts['error']
  else:
    alerts = all_alerts["data"]
    count = len(alerts)


  return render_template('alerts/index.html', alerts=alerts, count=count)


@blueprint.route("/<alert_id>", methods=["GET"])
def alert(alert_id):

  one_alert = get_alert(alert_id)
  
  if (one_alert['error']):
    error = one_alert['error']
  else:
    data = one_alert['data']

  return render_template('alerts/alert.html', alert=data)

