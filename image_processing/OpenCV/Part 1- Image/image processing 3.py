import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('dog.png',cv2.IMREAD_UNCHANGED)
cv2.namedWindow('image' , cv2.WINDOW_NORMAL)  #use to resize the window
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF

if k == 27:                         # wait for ESC key to exit
    cv2.destroyAllWindows() 
elif k == ord('a'):
    cv2.imwrite('basic pr2', img)     # wait for 'a' key to save and exit 
    cv.destroyALLWindows()

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

print(flags)

##plt.imshow(img, cmap = 'gray', interpolation = ' bicubic')
##plt.xticks([]), plt.yticks([])
##plt.show()

  
