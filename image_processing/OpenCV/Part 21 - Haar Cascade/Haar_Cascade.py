import cv2
import numpy as np

#-----haar Cascade----#

#approach -> First Find the face and then inside part of it i.e eyes ,nose etc
front_face = cv2.CascadeClassifier('frontface.xml')
eye = cv2.CascadeClassifier('eye.xml')

cap = cv2.VideoCapture(0)
while True:
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = front_face.detectMultiScale(gray)

    #for face w/h = width/height of the rectangle
    for x,y,w,h in faces:

        #form rectangle over an image
        cv2.rectangle(img , (x,y),(x+w,y+h),(255,0,0),2)
        #find the feature matching to face which basically EYEBROW part that is 'white--black' not stop at that point continue finding a NOSE part that is white--black--white
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Face Detected',(w,y+h), font, 1 ,(0,0,255), 2, cv2.LINE_AA)
        #find the region of the interest i.e face
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = img[y:y+h , x:x+w]
        eyes = eye.detectMultiScale(roi_gray)
        #finding eyes inside face
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
        cv2.imshow('img', img)
        cv2.imshow('roi_color',roi_color)
        #cv2.imshow('roi_gray',roi_gray)


        k = cv2.waitKey(10) & 0xff
        if k==27:
            break

cap.release()
cv2.destroyAllWindows()

        
        
