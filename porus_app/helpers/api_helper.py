import requests
import json
import os
import sys

api_url = os.environ.get('API_URL')

# will be extended for more features
def handle_request(end_point):
  
  response = requests.get(api_url + end_point)


  if (response.status_code < 400):
    # should move data to dict? (response.json might do this)
    data = response.json()
    error = None
  else:
    data = {}
    error_code = response.status_code
    

    # match error codes to message
    # only happens on error
    # most errors should be either server side or downtime
    match (error_code):
      case 400:
        error = dict(code = error_code, msg = 'Bad Request')
      case 401:
        error = dict(code = error_code, msg = 'Unathorized')
      case 403:
        error = dict(code = error_code, msg = 'Forbidden')
      case 404:
        error = dict(code = error_code, msg = 'Not Found')
      case 418:
        error = dict(code = error_code, msg = "I'm a teapot!")
      case 500:
        error = dict(code = error_code, msg = 'Internal Server Error')
      case 501:
        error = dict(code = error_code, msg = 'Not Implemented')
      case 502:
        error = dict(code = error_code, msg = 'Bad Gateway')
      case 503:
        error = dict(code = error_code, msg = 'Service Unavailable')
      case 504:
        error = dict(code = error_code, msg = 'Gateway Timeout')
      case _:
        error = dict(code = error_code, msg = 'Unknown Error. Please Check Error Code.')
  
  return dict(data = data, error = error)


  