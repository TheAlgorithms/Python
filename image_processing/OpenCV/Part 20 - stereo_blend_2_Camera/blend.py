import cv2
import numpy as np

def nothing(x):
    pass

alpha=0.0

cap1=cv2.VideoCapture(0)
cap2=cv2.VideoCapture(1)
cap1.set(3,480)
cap1.set(4,640)
cap2.set(3,480)
cap2.set(4,640)
cv2.namedWindow('alpha')
    
cv2.createTrackbar('a','alpha',0,100,nothing)
cv2.setTrackbarPos('a','alpha',50)

while True:
    _,img1 = cap1.read()
    _,img2 = cap2.read()
    gray1 =cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2 =cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    
    alpha = cv2.getTrackbarPos('a','alpha')
    alpha/=100
    beta = 1.0-alpha
    blend = cv2.addWeighted(gray1,alpha,gray2,beta,0.0)
    blurred = cv2.GaussianBlur(blend, (5, 5), 0)
    ret, thresh = cv2.threshold( blurred, 127, 255, cv2.THRESH_BINARY)

    (_,contours,_)=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(blend,contours,1,(0,0,255),3)
    
    for i in contours:
        area= cv2.contourArea(i)
        
        if(area>50000):
            x,y,w,h = cv2.boundingRect(i)
            rect = cv2.rectangle(blend, (x, y), (x+w, y+h), (255,0,0), 2)
            M = cv2.moments(i)
            if M['m00'] != 0:
                
                
                cy = int(M['m01']/M['m00'])           # (cx, cy) = rect center
                cx = int(M['m10']/M['m00'])
                cv2.circle(blend, (cx, cy), 7, (0, 0, 255), -1)
                
        
                   
            

    cv2.imshow('blend',blend)
    cv2.imshow('thresh',thresh)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
