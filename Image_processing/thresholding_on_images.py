# thresholding is a segmentation process used to seperate objects from its background

import cv2 as cv
import numpy as  np

img = cv.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\gradient.png',0)

_, thl = cv.threshold(img, 127, 255, cv.THRESH_BINARY)# Binary Thresholding
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)# Gives inverse Of thresh binary
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)# if pixel value lesser than 127 and greater than 255 it remains unchanged
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # whenever pixel value lesser than threshold(here 127) value assigned to pixel is 0 and after 127 all pixel remais same as it is
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # Just Opposite Of THRES TOZERO

cv.imshow("Image", img)
cv.imshow("thl", thl)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)



cv.waitKey(0)
cv.destroyAllWindows()
