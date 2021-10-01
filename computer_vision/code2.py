# import libraries

import numpy as np
import cv2

image = np.zeros((700,700,3), dtype='uint8')

#cv2.imshow("blank image", image)

"""Rectangle"""
rect = cv2.rectangle(image.copy(), (50,150), (600,600), (0,255,0), thickness=-1)
cv2.imshow("Rectangle", rect)

"""circle"""
circle = cv2.circle(image.copy(), (image.shape[1]//2, image.shape[0]//2), 100, (255, 255,0), thickness=4)
cv2.imshow("Cicle", circle)

"""Line"""
line = cv2.line(image.copy(), (650,200), (100,550), (255,0,255), thickness=5)
cv2.imshow("line", line)

"""Text"""
text = cv2.putText(image.copy(), "Hello from OpenCV!", (50,350), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,255), 2)
cv2.imshow("Text display",text)


cv2.waitKey(0)