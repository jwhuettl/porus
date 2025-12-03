import gtfs.helper

def get_alerts():
  endpoint = '/alerts.pb'

  response = handle_realtime_request(endpoint)

  print(response.header)


def get_trip_updates():
  endpoint = '/tripupdates.pb'


def get_vehicle_positions():
  endpoint = '/vehiclepositions.pb'