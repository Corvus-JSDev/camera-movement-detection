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

first_frame = None
while True:
	#* Grab the frame from the camera
	check, frame = video.read()

	#* Convert the frame to grayscale and add some blur to make it easier on the system
	gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	gray_frame_blur = cv.GaussianBlur(gray_frame, (11, 11), 0)  # Note: The blur value must be an odd number

	#* Save the first frame for a reference to see what has changed
	if first_frame is None:
		first_frame = gray_frame_blur
	delta_frame = cv.absdiff(first_frame, gray_frame_blur)

	#* Convert to pure black or white
	thresh_frame = cv.threshold(delta_frame, 30, 255, cv.THRESH_BINARY)[1]  # Any value >30 will be pure white, <30 will be pure black
	dil_frame = cv.dilate(thresh_frame, None, iterations=2)

	#* Add a green box around new objects
	contours, check = cv.findContours(dil_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		if not cv.contourArea(contour) < 10_000:
			x, y, w, h = cv.boundingRect(contour)
			cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	#* Show the video
	cv.imshow("My Video", frame)

	# Quit if the q key is pressed
	key = cv.waitKey(1)
	if key == ord("q"):
		break


# clean up resources associated with video capture, preventing resource leaks
video.release()
