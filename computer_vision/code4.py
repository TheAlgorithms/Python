# importing libraries

import cv2
import numpy as np

image = cv2.imread("files/flower.jpg")  #files\flower.jpg
cv2.imshow("flower", image)

"""Blur"""
#blurred = cv2.GaussianBlur(image.copy(), (5,5), cv2.BORDER_DEFAULT)
#cv2.imshow("blurred", blurred)

"""edges"""
#canny = cv2.Canny(blurred.copy(), 125, 175)
#cv2.imshow("edged", canny)

"""dilation"""
#dilated = cv2.dilate(canny.copy(), (5,5), iterations= 2)
#cv2.imshow("dilated", dilated)

"""erode"""
#eroded = cv2.erode(dilated.copy(),(5,5), iterations= 2)
#cv2.imshow("eroded", eroded)

"""image cropping"""

cropped = image.copy()[100:400, 200:450]
cv2.imshow("cropped", cropped)



cv2.waitKey(0)