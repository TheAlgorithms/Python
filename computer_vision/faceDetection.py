#pip install opencv-python

import cv2
#starting camera

#calling classifier
casclf=cv2.CascadeClassifier('facedata.xml')
#here add eye data in casclf2  for detecting eyes 

#loading face data
cap=cv2.VideoCapture(0)
#first camera

        
while cap.isOpened():
    status,frame=cap.read()
    #now we can apply classifier in live frame
    face=casclf.detectMultiScale(frame,1.5,5)  #classifier tuning parameter
    #print(face)
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
        #only face
        facedata=frame[x:x+h, y:y+w]
        cv2.imshow('f',facedata)
    cv2.imshow('face',frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
#cv.destroyWindow('live')  #destroy particular window
cv2.destroyAllWindows()  #destroy all windows

#to close camera
cap.release()
