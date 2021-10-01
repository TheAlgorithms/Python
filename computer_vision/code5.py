# import libs

import cv2
import numpy as np

image = cv2.imread("files/flower.jpg")  # 0-> grayscale -1 -> RGB&alpha  1-> BGR or RGB

blank = np.zeros(image.shape, dtype = 'uint8')

cv2.imshow("flower", image)
#cv2.imshow("Blank", blank)

gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
#cv2.imshow("grayscaled", gray)

blurred = cv2.GaussianBlur(gray.copy(), (5,5), cv2.BORDER_DEFAULT)
#cv2.imshow("blurred", blurred)

#edged = cv2.Canny(blurred.copy(), 125, 175)
#cv2.imshow("edged", edged)

ret, thresh = cv2.threshold(blurred.copy(), 125, 175, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{(len(contours))} number of contours detected!!')

conts = cv2.drawContours(blank.copy(), contours, -1, (0,0,255), 1)
cv2.imshow("contours traced", conts)

cv2.waitKey(0)