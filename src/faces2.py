import numpy as np 
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
	#capture frame by frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
	for (x, y, w, h) in faces:
		print(x, y, w, h)
		roi_gray = gray[y: y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		# recognise? options are deep learned model (keras, tensorflow, pytorch), other models (sklearn). These guys are going to do a demo with keras latr



		img_item = "my-image.png"
		cv2.imwrite(img_item, roi_color)

		color = (147, 20, 255) #BGR 
		stroke = 2 # thickness
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break  

# When everything done, release the capture
cap.release()
cv2.destroyALlWindows()