
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV

    lower_red = np.array([80, 150, 180])
    upper_red = np.array([150, 250, 255])

    # Threshold the HSV image to get only blue colors

    mask = cv2.inRange(hsv, lower_red, upper_red)
  
    

    # Bitwise-AND mask and original image

    res = cv2.bitwise_and(frame , frame, mask = mask)
    #kernel = np.array((15,15),np.float32)/225
    #smoothed = cv2.filter2D(res,-1,kernel)
    
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask, kernel , iterations = 1)

    cv2.imshow('frame', frame)
    cv2.imshow('erosion', erosion)
    cv2.imshow('res', res)
      
    ##cv2.imshow('smoothed', smoothed)
    

    k = cv2.waitKey(4) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

#this is code for printing all flag as if now we know only two i.e
#cv2.COLOR_BGR2GRAY
#cv2.COLOR_BGR2HSV
'''
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

print(flags)
'''

