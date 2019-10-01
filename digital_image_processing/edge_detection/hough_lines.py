import cv2
import numpy as np

img = cv2.imread('src.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,100,200,apertureSize = 5)

minLineLength = 0
maxLineGap = 19
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(255,255,255),2)

cv2.imshow('hough',img)
cv2.waitKey(0)