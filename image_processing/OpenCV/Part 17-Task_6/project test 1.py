import cv2
import numpy as np
j=0
k=0

def nothing(x):
    pass

def colorPick(event,x,y,flag,para):
    if event == cv2.EVENT_LBUTTONDOWN :
        pix=hsv[y,x]

        cv2.setTrackbarPos('lh','tb',pix[0]-10)
        cv2.setTrackbarPos('uh','tb',pix[0]+10)
        cv2.setTrackbarPos('ls','tb',pix[1]-30)
        cv2.setTrackbarPos('us','tb',pix[1]+30)
        cv2.setTrackbarPos('lv','tb',pix[2]-50)
        cv2.setTrackbarPos('uv','tb',pix[2]+50)
    
cap = cv2.VideoCapture('ball2.mp4')

cv2.namedWindow('tb')
cv2.createTrackbar('lh','tb',155,180,nothing)
cv2.createTrackbar('uh','tb',175,180,nothing)
cv2.createTrackbar('ls','tb',121,255,nothing)
cv2.createTrackbar('us','tb',181,255,nothing)
cv2.createTrackbar('lv','tb',129,255,nothing)
cv2.createTrackbar('uv','tb',229,255,nothing)

cv2.namedWindow('image')
black = np.zeros((720,1280,3), np.uint8)

while 1:
    j=j+1
    k = k+1
    _,frame=cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.setMouseCallback('image',colorPick)
    
    lh=cv2.getTrackbarPos('lh','tb')
    uh=cv2.getTrackbarPos('uh','tb')
    ls=cv2.getTrackbarPos('ls','tb')
    us=cv2.getTrackbarPos('us','tb')
    lv=cv2.getTrackbarPos('lv','tb')
    uv=cv2.getTrackbarPos('uv','tb')

    l=np.array([lh,ls,lv])
    u=np.array([uh,us,uv])

    mask = cv2.inRange(hsv,l,u)
    kernal = np.ones((5,5), np.uint8)
    dilate=cv2.dilate(mask,kernal,1)
    
    _,contour,_=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contour,0,(0,0,255),3)

    

    

    for i in contour:
        area= cv2.contourArea(i)
        if area>5000:
            x,y,w,h = cv2.boundingRect(i)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,120,255),2)
            cv2.circle(black ,(int((x+x+w)/2),int((y+y+h)/2)),3,(0,255,0),-1)

            cv2.putText(frame,"color1 detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
##    if j==1:
##        dilute2=dilate
##    if j>2:                        
##        dilute2=dilate+dilute2

        cv2.imshow('image',frame)
        #cv2.imshow('dilute',dilate)

    if k == 1:
        black2 = black
    if k>2:
        black = black2 + black
        cv2.imshow('black',black)

    if cv2.waitKey(1) & 0xFF == 27 :
        break

cap.release()    
cv2.destroyAllWindows()

