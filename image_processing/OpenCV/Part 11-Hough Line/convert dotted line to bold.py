import numpy as np
import cv2
import math

gray = cv2.imread('road.jpg')
edges = cv2.Canny(gray,50,150,apertureSize = 3)
##cv2.imwrite('edges-50-150.jpg',edges)
##minLineLength=50
##lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=40)
##
##a,b,c = lines.shape
##for i in range(a):
##    cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
##    cv2.imwrite('houghlines5.jpg',gray)
##

lines = cv2.HoughLines(edges, 1, np.pi / 180, 150, None, 10, 10)
    
if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(gray, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
cv2.imwrite('houghlines5.jpg',gray)
