import cv2
import numpy as np
img = cv2.imread('C:\Users\Hritik Jaiswal\OneDrive\Documents\Git\Magic-of-OpenCV\images and videos\dog.png',0)
while True:
    cv2.imshow('hritik',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
   
