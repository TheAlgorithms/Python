import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0)
#gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('image')
cv2.createTrackbar('lh','image',0,255,nothing)
cv2.createTrackbar('uh','image',0,255,nothing)
cv2.createTrackbar('ls','image',0,255,nothing)
cv2.createTrackbar('us','image',0,255,nothing)
cv2.createTrackbar('lv','image',0,255,nothing)
cv2.createTrackbar('uv','image',0,255,nothing)



cv2.setTrackbarPos('lh','image',0)
cv2.setTrackbarPos('uh','image',58)
cv2.setTrackbarPos('ls','image',45)
cv2.setTrackbarPos('us','image',255)
cv2.setTrackbarPos('lv','image',54)
cv2.setTrackbarPos('uv','image',168)




while 1:
    
    _,img=cap.read()
    #img=cv2.imread('tri.jpeg')
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('lh','image')
    uh=cv2.getTrackbarPos('uh','image')
    ls=cv2.getTrackbarPos('ls','image')
    us=cv2.getTrackbarPos('us','image')
    lv=cv2.getTrackbarPos('lv','image')
    uv=cv2.getTrackbarPos('uv','image')
    
   
    


    l_r=np.array([lh,ls,lv])
    u_r=np.array([uh,us,uv])

    mask = cv2.inRange(hsv,l_r,u_r)
    res=cv2.bitwise_and(img,img,mask=mask) 
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('hsv',hsv)
    ret,thresh = cv2.threshold(mask,127,255,0)
    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img,contours,-1,(0,255,0),1)
    cv2.imshow('',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
