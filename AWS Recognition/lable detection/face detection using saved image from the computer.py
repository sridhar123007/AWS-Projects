#face detection
import cv2
import numpy as np

face_classifier=cv2.CascadeClassifier("D:\\haarcascade_frontalface_default.xml")

#reading the image with the help of imread function and converting the image to grey image
img=cv2.imread("D:\\pic.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect the faces from the image using detectMultiScale function
faces=face_classifier.detectMultiScale(gray,1.3,5)

#drawing rectangle boundries for the detected face
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (127,0,255), 2)
    cv2.imshow('Face detection', img)
    #waitKey(0)- when user presses any key the image window will be closed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
