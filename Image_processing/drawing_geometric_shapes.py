import numpy as np
import cv2

img = cv2.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\lena.jpg', 1)
# TODO: Drawing line on image->
# here in line first argument is image variable, second and third is starting and ending coordinates , 4th one for color(in BGR format), 5th one for thickness
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
# TODO: To draw a arrowed line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 5)
# TODO: To draw a rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (255, 0, 0),
                    5)  # if we provide -1 in thickness then it will fill the rectangle with given color
# TODO: To draw a circle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)  # 2nd argument is radius here
# TODO: To put some text
# 2nd argument is text 3rd argument is starting coordinates 4th one for font face, 5th one for font size, 6th one for color of font, 7th  one for thickness, 8th one for line type
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Phaham', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
