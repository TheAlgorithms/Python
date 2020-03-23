import cv2
import numpy as np
# for image ( we can also do with image )
##img = cv2.imread('dog.png')
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    retval , boo = cv2.threshold(grayscale,200,255,cv2.THRESH_BINARY_INV)
    retval , boo1 = cv2.threshold(grayscale,200,255,cv2.THRESH_BINARY)
    retval , boo2 = cv2.threshold(grayscale,200,255,cv2.THRESH_TRUNC)
    retval , boo3 = cv2.threshold(grayscale,200,255,cv2.THRESH_TOZERO)
    retval , boo4 = cv2.threshold(grayscale,200,255,cv2.THRESH_TOZERO_INV)

    ##cv2.imshow('frame1',boo1)
    ##cv2.imshow('frame2',boo2)
    ##cv2.imshow('frame3',boo3)
    ##cv2.imshow('frame4',boo4)
    cv2.imshow('frame',boo)
    cv2.imshow('grayscale',grayscale)

    k = cv2.waitKey(0) & 0xFF
    if k ==27:
        break
    
# we can also use this 

#cv2.THRESH_BINARY_INV
#cv2.THRESH_TRUNC
#cv2.THRESH_TOZERO
#cv2.THRESH_TOZERO_INV

##cv2.imshow('frame',img)
cv2.destroyAllWindows()

cap.release()

   

  


