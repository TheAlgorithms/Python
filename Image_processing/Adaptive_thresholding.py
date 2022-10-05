import cv2 as cv
import numpy as np
# adaptive thresholding is for setting threshold for particular small regions also it's not like global threshold
img = cv.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\sudoku.png',0)
_,th1 = cv.threshold(img, 127,255,cv.THRESH_BINARY)# some part is black and other is fair depends on lightening
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11, 2) # takes mean of neighbourhood, 2nd last argument is block size( decides area of neighbourhood), last argument is value of c
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11, 2)

cv.imshow("Image", img)
# cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)



cv.waitKey(0)
cv.destroyAllWindows()


