import cv2
import numpy as np


def nothing(x):
    pass

def colorPick(event,x,y,flag,para):
    if event == cv2.EVENT_LBUTTONDOWN :
        pix=hsv[y,x]
        print(pix)

        cv2.setTrackbarPos('lh','tb',pix[0]-10)
        cv2.setTrackbarPos('uh','tb',pix[0]+10)
        cv2.setTrackbarPos('ls','tb',pix[1]-30)
        cv2.setTrackbarPos('us','tb',pix[1]+30)
        cv2.setTrackbarPos('lv','tb',pix[2]-50)
        cv2.setTrackbarPos('uv','tb',pix[2]+50)



        
cap=cv2.VideoCapture('ball2.mp4')
cv2.namedWindow('tb')
cv2.createTrackbar('lh','tb',0,180,nothing)
cv2.createTrackbar('uh','tb',0,180,nothing)
cv2.createTrackbar('ls','tb',0,255,nothing)
cv2.createTrackbar('us','tb',0,255,nothing)
cv2.createTrackbar('lv','tb',0,255,nothing)
cv2.createTrackbar('uv','tb',0,255,nothing)

cv2.namedWindow('image')

while 1:

    _,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.setMouseCallback('image',colorPick)
    


    lh=cv2.getTrackbarPos('lh','tb')
    uh=cv2.getTrackbarPos('uh','tb')
    ls=cv2.getTrackbarPos('ls','tb')
    us=cv2.getTrackbarPos('us','tb')
    lv=cv2.getTrackbarPos('lv','tb')
    uv=cv2.getTrackbarPos('uv','tb')

    l=np.array([lh,ls,lv])
    u=np.array([uh,us,uv])

    

    mask =cv2.inRange(hsv,l,u)
    #blur=cv2.GaussianBlur(mask,(5,5),0)
    kernal = np.ones((5,5), np.uint8)
    #o=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
    
    dilate=cv2.dilate(mask,kernal,1)
    #_,thresh = cv2.threshold(dilate,127,255,0)
    contour,hierarchy =cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in contour:
        area= cv2.contourArea(i)
        if area>500:
            x,y,w,h = cv2.boundingRect(i)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,120,255),2)
            cv2.putText(frame,"color1 detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
        
    cv2.imshow('image',frame)
    cv2.imshow('mask',dilate)

    if cv2.waitKey(100) & 0xFF == ord('q') :
        break

cap.release()    
cv2.destroyAllWindows()
