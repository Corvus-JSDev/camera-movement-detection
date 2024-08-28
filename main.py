from pprint import pp
import cv2 as cv  # Note: cv2 uses BGR instead of RGB
import time

video = cv.VideoCapture(0)
time.sleep(1)  # Wait 1 second for the camera to load

"""
check, frame = video.read()

print(check)  # This will check if the camera as turned on
pp(frame)  # This will print the BGR value of the frame

# Note: Just capturing a single frame will likely return a black screen as the camera itself doesn't have time to turn on

# Grabbing multiple frames
check1, frame1 = video.read()
check2, frame2 = video.read()
check3, frame3 = video.read()
check4, frame4 = video.read()
check5, frame5 = video.read()

print(check1, check2, check3, check4, check5)

print("Printing frame values")

print("Frame 1")
pp(frame1)
print("Frame 2")
pp(frame2)
print("Frame 3")
pp(frame3)
print("Frame 4")
pp(frame4)
print("Frame 5")
pp(frame5)
"""

while True:
	check, frame = video.read()
	gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Convert the original frame to grayscale
	gray_frame_gau = cv.GaussianBlur(gray_frame, (21, 21), 0)  # Add some blur to remove detail and make it easier on the system

	cv.imshow("My Video", gray_frame_gau)

	# Quit if the q key is pressed
	key = cv.waitKey(1)
	if key == ord("q"):
		break


# clean up resources associated with video capture, preventing resource leaks
video.release()
