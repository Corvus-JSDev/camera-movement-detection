import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import imghdr

load_dotenv()
EMAIL_USR = os.getenv("EMAIL_USR")
EMAIL_PW = os.getenv("EMAIL_PW")

def send_email(img_to_send):
	msg = EmailMessage()
	msg['Subject'] = "Camera_Detection_Test"
	msg.set_content("Motion has been detected")
	msg['From'] = EMAIL_USR
	msg['To'] = EMAIL_USR

	# rb (read binary) is used for reading images
	with open(img_to_send, "rb") as file:
		img_content = file.read()

	msg.add_attachment(img_content, maintype="image", subtype=imghdr.what(None, img_content))

	with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
		gmail.ehlo()
		gmail.starttls()
		gmail.login(EMAIL_USR, EMAIL_PW)
		gmail.sendmail(EMAIL_USR, EMAIL_USR, msg.as_string())

	print(f"{img_to_send} was sent")


if __name__ == "__main__":
	send_email(img_to_send="images/tester-img.png")