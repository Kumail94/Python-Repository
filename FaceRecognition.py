import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as pt
from PIL import Image
# import tkinter
# from tkinter import * 
# import os

faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
def faceExtractor(image):
	gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
	face = faceClassifier.detectMultiScale(gray , scaleFactor = 1.3 , minNeighbors=5)
	if face is():
		return None
	for(x,w,y,h) in face:
		print(x,w,y,h)
		croppedImage = image[x:x+w , y:y+h]

	return croppedImage
capture = cv2.VideoCapture(0)
count = 0
while True:
	ret , frame = capture.read()
	print (ret)
	print(frame)
	if faceExtractor(frame) is not None:
		count=count+1
		face = cv2.resize(faceExtractor(frame) , (400,350))
		face = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)
		imagePath = "C:/Users/DR/Documents/Faces/User = " + " Face Sample = " + str(count) + ".jpg"
		cv2.imwrite(imagePath , face)
		cv2.putText(face , str(count) , (30,30) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) ,2)
		cv2.imshow("Face Cropper " , face)
	else:
		print("face not found")
		pass
	if cv2.waitKey(1) == 13 or count == 100:
		break
capture.release()
cv2.destroyAllWindows()	

data_Path = "C:/Users/DR/Documents/Faces/"
onlyfiles = [f for f in listdir(data_Path) if isfile(join(data_Path , f))]

Label , TrainingModel , IDs  = [] , [] , []

for i , files in enumerate(onlyfiles):
	imagePath = data_Path+onlyfiles[i]
	#ssId = str(os.path.split(onlyfiles)[-1].split(' . ')[1])
	images = cv2.imread(imagePath , cv2.IMREAD_GRAYSCALE)
	TrainingModel.append(np.asarray(images , dtype=np.int32))
	Label.append(i)
	#IDs.append(user_id, dtype = np.int32)
Label = np.asarray(Label , dtype=np.int32)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(TrainingModel) , np.asarray(Label))
print('Model Sample Completes')

def faceDetector(image , size = 0.5):
	gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
	face = faceClassifier.detectMultiScale(gray , scaleFactor = 1.3 , minNeighbors = 5)
	if face is ():
		return image,[]
	for (x,w,y,h) in face:
		cv2.rectangle(image , (x,y) , (x+w , y+h) , (0,255,0) , 2)
		roi = image[x:x+w,y:y+h]
		print(roi)
		roi = cv2.resize(roi , (300,300))
	return image,roi
cap = cv2.VideoCapture(0)
Id = 0
while True:
	ret , frame = cap.read()
	img , face = faceDetector(frame)
	try:
		face = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)
		result = model.predict(face)
		if result[1] < 500:
			detector = int(100*(1-(round(result[1]/350 ,2))))
			detector = round(detector , 2)    #100-round(result[1] ,2)
			display_string = " Confidance it is user "+ str(detector) + " %" 
			cv2.putText(img , display_string , (100,120) , cv2.FONT_HERSHEY_COMPLEX,1,(150,255,0) ,3)
		if detector > 75:
			cv2.putText(img , "Unlocked" , (300,350) , cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
			cv2.imshow("Face Recognition" , img)
		else:
			cv2.putText(img , "Locked" , (300,350) , cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,0,0),2)
			cv2.imshow("Face Recognition" , img)
	except:
		cv2.putText(img , "Face Not Found",(305,350),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
		cv2.imshow("Face Recognition" , img)
		pass
	if cv2.waitKey(1) == 13:
		break
cap.release()
cv2.destroyAllWindows()		
		
#root = Tk()

#root.geometry("625x345")
#root.title("Facial Recognition Systems")
#root.minsize(620,344)
#root.maxsize(620,344)
#Label(root , text = "Facial Recognition Attandance Based Systems" , fg="blue" , font="comicsansms 16 bold",pady=15).grid(row=0,column=3)

#ID = Label(root , text ="ID" , font="comicsansms 12 bold")
#Name = Label(root ,text="Name", font="comicsansms 12 bold")
#Button = Button(root,text="Submit")

#ID.grid(row=1 , column =2)
#Name.grid(row=2 , column=2)
#Button.grid(row=1 , column=2 , padx = 25 )

#IdValue   = IntVar()
#NameValue = StringVar()

#IdEntry =   Entry(root , textvariable=IdValue)
#NameEntry = Entry(root,textvariable =NameValue)

#IdEntry.grid(row=1,column=3)
#NameEntry.grid(row=2,column=3)

#Button(text = "Registered",font="comicsansms 8 bold").grid(row = 3 , column=3)
#root.mainloop()
