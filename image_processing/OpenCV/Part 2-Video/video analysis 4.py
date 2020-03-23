
# saving a video in the form of .avi extension
# capture a video and saving each and every frame 

import cv2
import numpy as np

cap = cv2.VideoCapture('mountain.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')  #fourcc is a 4-byte code used to specify the video codec.
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #1.video name 3.frame per sec 4.window size                                                          
    

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,0)
    out.write(frame)
    cv2.imshow('gray',gray)
    cv2.imshow('frame',frame)
    
    

    if cv2.waitKey(2) & 0xFF == ord('m'):  #u can choose any key 
        break
    


cap.release()
out.release() #video capture stop
cv2.destroyAllWindows()

    
    
