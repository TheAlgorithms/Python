import cv2
import numpy


cap = cv2.VideoCapture('background.mp4')
back = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame = cap.read()
    background = back.apply(frame)

    cv2.imshow('frame',frame)
    cv2.imshow('back', background)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cv2.release()
cv2.destroyAllWindows()
    

