import cv2
import numpy as np

def nothing(x):
    pass


#img = cv2.imread('img.jpeg',-1)
cap=cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.resizeWindow('image',600,350)


#Creating trackbar
cv2.createTrackbar('lh','image',0,255,nothing)
cv2.createTrackbar('uh','image',0,255,nothing)
cv2.createTrackbar('ls','image',0,255,nothing)
cv2.createTrackbar('us','image',0,255,nothing)
cv2.createTrackbar('lv','image',0,255,nothing)
cv2.createTrackbar('uv','image',0,255,nothing)
#cv2.createTrackbar('switch','image',0,1,nothing)

#set track bar
cv2.setTrackbarPos('lh','image',0)
cv2.setTrackbarPos('uh','image',58)
cv2.setTrackbarPos('ls','image',45)
cv2.setTrackbarPos('us','image',255)
cv2.setTrackbarPos('lv','image',54)
cv2.setTrackbarPos('uv','image',168)


while True:
    _,img=cap.read()

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #while 1 :
    #reading trackbar
    lh=cv2.getTrackbarPos('lh','image')
    uh=cv2.getTrackbarPos('uh','image')
    ls=cv2.getTrackbarPos('ls','image')
    us=cv2.getTrackbarPos('us','image')
    lv=cv2.getTrackbarPos('lv','image')
    uv=cv2.getTrackbarPos('uv','image')
    #switch = cv2.getTrackbarPos('switch','image')

    
    l_r=np.array([lh,ls,lv])
    u_r=np.array([uh,us,uv])

    mask = cv2.inRange(hsv,l_r,u_r)
    res=cv2.bitwise_and(img,img,mask=mask) 



    #blur
    
    k=np.ones((15,15),np.float32)/225
    s= cv2.filter2D(res,-1,k)
    b= cv2.GaussianBlur(res,(15,15),0)
    m= cv2.medianBlur(res,15)
    bb =cv2.bilateralFilter(res , 15 , 75, 75)#useless

    #morphology

    k2= np.ones((5,5) , np.uint8)
    e=cv2.erode(mask,k2,1)
    d=cv2.dilate(mask,k2,1)
    o=cv2.morphologyEx(mask,cv2.MORPH_OPEN,k2)
    c=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,k2)
    oc=cv2.morphologyEx(o,cv2.MORPH_CLOSE,k2)#same as close+open

    
    #output

    #cv2.imshow('img',img)
    #cv2.imshow('mask',mask)
    #cv2.waitKey(1000)
    
    cv2.imshow('res',res)
    #cv2.imshow('blur',s)



    #cv2.imshow('Gblur',b)

    #cv2.imshow('medblur',m)

    #cv2.imshow('bilateralblur',bb)

    #cv2.imshow('erode',e)

    #cv2.imshow('dillate',d)

    #cv2.imshow('openM',o)

    #cv2.imshow('closeM',c)
    #cv2.imshow('OnC_M',oc)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

#cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
