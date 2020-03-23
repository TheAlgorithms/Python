import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import imutils

# frame read
frame = cv2.imread('the-bill.jpg')

# resize
frame = cv2.resize(frame , (600,600))

# grayscale
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

# remove noise
blur = cv2.GaussianBlur(gray,(5,5),0)

# otsu thresh (bimodel thresold)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# get structuring element

horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,25))
print('horizontal kernel : {}'.format(horizontal_kernel))
print('vertical kernel : {}'.format(vertical_kernel))

# opening (erosion followed by dilation)

horizontal_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
vertical_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)

# contours apply on detected lines
# First one is source image, second is contour retrieval mode, third is contour approximation method

cnts = cv2.findContours(horizontal_lines ,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
cntsv = cv2.findContours(vertical_lines ,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

# find contours
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cntsv = cntsv[0] if len(cntsv) == 2 else cntsv[1]

for c in cnts:
    cv2.drawContours(frame, [c], -1, (255,255,255), 2)
for c in cntsv:
    cv2.drawContours(frame, [c], -1, (255,255,255), 2)

# repair image as neccesary info is removed during horizontal and vertical line removal
repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6))
repair_vkernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6,1))
result1 = 255 - cv2.morphologyEx(255 - frame, cv2.MORPH_CLOSE, repair_kernel+repair_vkernel, iterations=1)

# imshow  

cv2.imshow('thresh', thresh)
cv2.imshow('horizontal_lines', horizontal_lines)
cv2.imshow('vertical_lines', vertical_lines)
cv2.imshow('frame', frame)
cv2.imshow('result1', result1)

# grayscale

gray1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
thresh1 = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23, 30)
canny = imutils.auto_canny(thresh1)

output = cv2.bitwise_not(canny)
kernel = np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

dilation = cv2.dilate(canny,kernel,iterations = 1)
cv2.imwrite('output.jpg', dilation)

contour,hierachy=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#contour = contour[0] if len(contour) == 2 else contour[1]

for i in contour:
    area= cv2.contourArea(i)
    if area>20:
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,120,255),2)
        

cv2.imshow('output' ,output)
cv2.imshow('dilate' ,dilation)
cv2.imshow('opening' ,opening)
cv2.imshow('original_frame' ,frame)
cv2.imshow('canny' ,canny)
cv2.imshow('thresh1' ,thresh1)


# destroy all window
cv2.waitKey(0)
cv2.destroyAllWindows()


















