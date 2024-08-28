from pprint import pp
import cv2 as cv  # Note: cv2 uses BGR instead of RGB

# Note: Just capturing a single frame will likely return a black screen as the camera itself doesnt have time to turn on
video = cv.VideoCapture(0)
check, frame = video.read()

print(check)  # This will check if the camera as turned on
print(frame)  # This will print the BGR value of the frame

# Grabbing multiple frames
