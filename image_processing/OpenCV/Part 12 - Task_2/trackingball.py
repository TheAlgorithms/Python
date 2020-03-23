import cv2
import numpy as np
i=0

cap = cv2.VideoCapture('object.mp4')
cap.set(3,640);
cap.set(4,480);
def mouse_event(event, x,y,flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (event)
        pixel = hsv[y,x]

        cv2.setTrackbarPos('lowh','trackbar',pixel[0] - 10)
        cv2.setTrackbarPos('highh','trackbar',pixel[0] + 10)
        cv2.setTrackbarPos('lows','trackbar',pixel[1] - 20)
        cv2.setTrackbarPos('highs','trackbar',pixel[1] + 20)
        cv2.setTrackbarPos('lowv','trackbar',pixel[2] - 50)
        cv2.setTrackbarPos('highv','trackbar',pixel[2] + 50)

def callback(x):
        pass

cv2.namedWindow('trackbar')
cv2.namedWindow('imag')

cv2.createTrackbar('lowh','trackbar',0,180,callback)
cv2.createTrackbar('highh','trackbar',0,180,callback)
cv2.createTrackbar('lows','trackbar',0,255,callback)
cv2.createTrackbar('highs','trackbar',0,255,callback)
cv2.createTrackbar('lowv','trackbar',0,255,callback)
cv2.createTrackbar('highv','trackbar',0,255,callback)

while 1:
    i=i+1
    _,img=cap.read()
    cv2.setMouseCallback('imag',mouse_event)
    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lowh=cv2.getTrackbarPos('lowh', 'trackbar')
    highh=cv2.getTrackbarPos('highh', 'trackbar')
    lows=cv2.getTrackbarPos('lows', 'trackbar')
    highs=cv2.getTrackbarPos('highs', 'trackbar')
    lowv=cv2.getTrackbarPos('lowv', 'trackbar')
    highv=cv2.getTrackbarPos('highv', 'trackbar')

    lowred=np.array([lowh,lows,lowv])
    highred=np.array([highh,highs,highv])

    mask= cv2.inRange (hsv,lowred,highred)
    
    kernel = np.ones((5,5),np.uint8)
    dilate = cv2.dilate(mask, kernel, iterations = 1)
    trackimg=np.zeros((480,640,3), np.uint8)
    

    (_,contours,_)=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(0,0,255),3)
    
    
    for i in contours:
                    area = cv2.contourArea(i)
                    if(area>500):
                            x,y,w,h = cv2.boundingRect(i)
                            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                            cv2.putText(img,"color1 detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
                            centerx=x+w/2
                            centery=y+h/2
                            img=cv2.circle(img, (int(centerx),int(centery)) ,2,(0,0,255),8, 0)
                            trackimg=cv2.circle(trackimg, (int(centerx),int(centery)) ,2,(0,0,255),8, 0)

    cv2.imshow('imag',img)
    cv2.imshow('tracking image',trackimg)
##    cv2.imshow('closin',closing)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
            break                          

cap.release()
cv2.destroyAllWindows()
