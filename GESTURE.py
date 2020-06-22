import cv2 
import numpy as np 
import math 
from PIL import Image, ImageDraw, ImageFont
# import Tkinter as tk
image = cv2.VideoCapture(0)
while  image.isOpened():
	ret , frame = image.read()
	cv2.rectangle(frame , (100,100) , (300,300) , (0,255,0) ,0)
	cropped_Image = frame[100:300,100:300]
	blur = cv2.GaussianBlur(cropped_Image , (3,3),0)
	hsv = cv2.cvtColor(blur , cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv , np.array([2,0,0]) , np.array([20,255,255]))
	kernel = np.ones((5,5))
	dilation = cv2.dilate(mask , kernel , iterations=1)
	erosion = cv2.erode(dilation , kernel , iterations=1)
	filtered = cv2.GaussianBlur(erosion , (3,3) ,0)
	ret , threshold = cv2.threshold(filtered , 127,255 , 0)
	cv2.imshow("threshold Image" , threshold)
	countours , hirarchy = cv2.findContours(threshold.copy() , cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	try:
		contour = max(countours , key=lambda x:cv2.contourArea(x))
		x,y,w,h = cv2.boundingReact(contour)
		cv2.rectangle(cropped_Image , (x,y) ,(x+w,y+h),(0,0,255),5)
		hull = cv2.convexHull(contour)
		drawing = np.zeros(cropped_Image.shape , np.uint8)
		cv2.drawContours(drawing , [contour] , -1 , (0,255,0),0)
		cv2.drawContours(drawing , [hull] , -1 ,(0,0,255),0)
		hull = cv2.convexHull(contour , returnPoints=False)
		defects = cv2.convexityDefects(contour,hull)
		count_defects = 0
		for i in range (defects.shape[0]):
			s,e,f,d = defects[i,0]
			start = tuple(contour[s][0])
			end = tuple(contour[e][0])
			far = tuple(contour[f][0])
			a=math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1])**2)
			b=math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) **2)
			c=math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) **2)
			angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180)/3.14
			if angle <= 90:
				count_defects = count_defects + 1
				cv2.circle(cropped_Image , far , 1 , [0,0,255],-1)
			cv2.line(cropped_Image , start , end , [0,255,0],2)
		if count_defects == 0:
			cv2.putText(frame , "ONE" ,  (50,50) , cv2.FONT_HERSHEY_SIMPLEX , 2 , (0,0,255) , 2)
		elif count_defects == 1:
			cv2.putText(frame , "TWO" ,  (50,50) , cv2.FONT_HERSHEY_SIMPLEX , 2 , (0,0,255) , 2)
		elif count_defects == 2:
			cv2.putText(frame , "THREE", (50,50) , cv2.FONT_HERSHEY_SIMPLEX , 2 , (0,0,255) , 2)
		elif count_defects == 3:
			cv2.putText(frame , "FOUR" , (50,50) , cv2.FONT_HERSHEY_SIMPLEX , 2 , (0,0,255) , 2)
		elif count_defects == 4:
			cv2.putText(frame , "FIVE" , (50,50) , cv2.FONT_HERSHEY_SIMPLEX , 2 , (0,0,255) , 2)
		else:
			pass
	except:
		pass
	print(frame)	
	cv2.imshow("Gesture" , frame)
	ALL_Images = np.hstack((drawing , cropped_Image))
	cv2.imshow("Contour Image" , ALL_Images)
	if cv2.waitKey(1) == ord ('q'):
		break
image.release()
cv2.destroyAllWindows()		

			

			
			


		

