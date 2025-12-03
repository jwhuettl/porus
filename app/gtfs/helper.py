import os, requests
from google.transit import gtfs_realtime_pb2

gtfs_url = os.environ.get("GTFS_URL")

def handle_realtime_request(endpoint):

  feed = gtfs_realtime_pb2.FeedMessage()
  response = requests.get(gtfs_url + endpoint)
  feed.ParseFromString(response.content)

  return feed

