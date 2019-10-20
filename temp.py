# import time
# import yaml
# from motion_detector import MotionDetector

# video_file = "videos/new.mp4"
# FRAME_RATE = 25
# result = []

# with open("data/coordinates_1.yml") as data:
# 	points = yaml.load(data, Loader=yaml.FullLoader)
# 	detector = MotionDetector(video_file, points, 0)
# 	detector.detect_motion(result)
# 	print(result)

# import data
# print(data.data())