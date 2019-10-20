from flask import Flask
import json
import math
from datetime import datetime
import data
# import yaml
# from motion_detector import MotionDetector

video_file = "videos/new.mp4"

basic = '''{
  "id": 1,
  "size": 8,
  "width": 854,
  "height": 480,
  "boxes": [
  {
    "id": 0,
    "coordinates": [
      [103,258],
      [209,256],
      [178,395],
      [46,395]
    ]
  },
  {
    "id": 1,
    "coordinates": [
      [221,256],
      [325,255],
      [318,388],
      [197,393]
    ]
  },
  {
    "id": 2,
    "coordinates": [
      [339,258],
      [439,255],
      [460,387],
      [339,389]
    ]
  },
  {
    "id": 3,
    "coordinates": [
      [454,256],
      [550,255],
      [584,382],
      [478,387]
    ]
  },
  {
    "id": 4,
    "coordinates": [
      [538,137],
      [443,139],
      [457,81],
      [534,81]
    ]
  },
  {
    "id": 5,
    "coordinates": [
      [370,83],
      [440,81],
      [427,136],
      [347,140]
    ]
  },
  {
    "id": 6,
    "coordinates": [
      [327,141],
      [356,81],
      [286,86],
      [244,141]
    ]
  },
  {
    "id": 7,
    "coordinates": [
      [218,141],
      [263,81],
      [193,80],
      [152,139]
    ]
  }]
}'''

FRAME_RATE = 25
TOTAL_FRAMES = 1250

app = Flask(__name__)
initial_ts = datetime.now()
result = data.data()

@app.route("/")
def hello():
    return "Welcome to Parking Project"

@app.route("/info")
def info():
	result = json.loads(basic)
	return result

@app.route("/status")
def status():
  current_ts = datetime.now()
  td = current_ts - initial_ts
  frames = math.floor(FRAME_RATE * td.total_seconds())
  return {
    'statuses': result[frames % TOTAL_FRAMES]
  }

# with open("data/coordinates_1.yml") as data:
#   points = yaml.load(data, Loader=None)
#   detector = MotionDetector(video_file, points, 0)
#   detector.detect_motion()
