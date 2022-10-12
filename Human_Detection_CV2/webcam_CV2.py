import numpy as np
import cv2
# note that the video window must be highlighted or selected in advanced to work!
cv2.startWindowThread()
cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read() #it reads the frames of images
    
    cv2.imshow('frame',frame)# it displays the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
       
        
        break

cap.release()
cv2.destroyAllWindows()


cv2.waitKey(1)

#Code Submitted By Prasanna1717 for OpenSourcing