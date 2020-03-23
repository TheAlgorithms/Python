import cv2
import numpy as np


def nothing(x):
    pass

def colorPick(event,x,y,flag,para):
    if event == cv2.EVENT_LBUTTONDOWN :
        pix=hsv[y,x]


        cv2.setTrackbarPos('lh','tb',pix[0]-10)
        cv2.setTrackbarPos('uh','tb',pix[0]+10)
        cv2.setTrackbarPos('ls','tb',pix[1]-20)
        cv2.setTrackbarPos('us','tb',pix[1]+20)
        cv2.setTrackbarPos('lv','tb',pix[2]-50)
        cv2.setTrackbarPos('uv','tb',pix[2]+50)



        
cap=cv2.VideoCapture(0)
#img=cv2.imread('black.jpeg')
cv2.namedWindow('tb')
cv2.resizeWindow('tb',700,450)
cv2.createTrackbar('lh','tb',0,180,nothing)
cv2.createTrackbar('uh','tb',0,180,nothing)
cv2.createTrackbar('ls','tb',0,255,nothing)
cv2.createTrackbar('us','tb',0,255,nothing)
cv2.createTrackbar('lv','tb',0,255,nothing)
cv2.createTrackbar('uv','tb',0,255,nothing)
cv2.createTrackbar('x1','tb',0,700,nothing)
cv2.createTrackbar('y1','tb',0,700,nothing)
cv2.createTrackbar('x2','tb',0,700,nothing)
cv2.createTrackbar('y2','tb',0,700,nothing)


cv2.namedWindow('image')

cv2.setTrackbarPos('x1','tb',200)
cv2.setTrackbarPos('y1','tb',200)
cv2.setTrackbarPos('x2','tb',400)
cv2.setTrackbarPos('y2','tb',400)
while 1:

    _,frame=cap.read()
    x1=cv2.getTrackbarPos('x1','tb')
    y1=cv2.getTrackbarPos('y1','tb')
    x2=cv2.getTrackbarPos('x2','tb')
    y2=cv2.getTrackbarPos('y2','tb')
    

   
    frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),10)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #img=cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,255),cv2.FILLED)
    #cv2.imshow('filled',img)
        
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
    #erode=cv2.erode(mask,kernal,1)
    dilate=cv2.dilate(mask,kernal,1)
    #_,thresh = cv2.threshold(dilate,127,255,0)
    contour,hierachy=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in contour:
    
        area= cv2.contourArea(i)
        if area>500:
            x,y,w,h = cv2.boundingRect(i)
            if (x>x1 and x<x2) and (y>y1 and y<y2):
                if ((x+w)>x1 and (x+w)<x2) and ((y+h)>y1 and (y+h)<y2):
            
                    img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,120,255),2)
                    cv2.putText(frame,"color1 detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
        
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()    
cv2.destroyAllWindows()
