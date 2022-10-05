import numpy as np
import cv2

# TODO: creating black image
# 1st argument is list 2nd one is data type
img = np.zeros([512, 512, 3], np.uint8)  # in list 1st argument is height, 2nd one is breadth and 3rd one is 3
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Phaham', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()