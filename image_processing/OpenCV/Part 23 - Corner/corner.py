import cv2
import numpy as np
#frame=cv2.imread('img.jpeg')
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #gray=np.float32(gray)
    edges=cv2.Canny(frame,300,300)
    corners=cv2.goodFeaturesToTrack(edges,100000,0.01,10)
    corners=np.int0(corners)
    for corner in corners:
        x,y=corner.ravel()
        cv2.circle(frame,(x,y),3,255,2)
    cv2.imshow('c',frame)
    



    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
#cv2.waitKey(0)
cv2.destroyAllWindows()

    
 
