from flask import Blueprint
import requests
import json
import os

blueprint = Blueprint('schedule', __name__)