import numpy as np
import cv2
def nothing(x):
    pass
cap= cv2.VideoCapture(0)
cv2.namedWindow('tb')
cv2.createTrackbar('x','tb',0,200,nothing)
cv2.createTrackbar('y','tb',0,200,nothing)

while 1:
    _, frame= cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ksize =5
    #kernel = np.ones((5,5), np.uint8) 


    #filter
    median = cv2.medianBlur(gray,ksize)

    kernel = np.ones((5,5),np.float32)/225
    smoothed = cv2.filter2D(gray,-1,kernel)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('median',median)
    laplacian=cv2.Laplacian(smoothed,cv2.CV_64F)
    #cv2.imshow('laplacian',laplacian )
    x=cv2.getTrackbarPos('x','tb')
    y=cv2.getTrackbarPos('y','tb')
    

    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,5)
    edges=cv2.Canny(median,x,y)

    
    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('canny',edges)
    


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


    

    
