
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read an image
#you can simply pass integers 1, 0 or -1 respectively.
img = cv2.imread('model3.jpg',cv2.IMREAD_UNCHANGED)
#you can resize window
cv2.namedWindow('image' , cv2.WINDOW_NORMAL)
#cv2.imshow() to display an image in a window
cv2.imshow('image',img)
# function wait for millisecond any key from keyboard to be 
cv2.waitKey(0)
#simply destroys all the windows we created
cv2.destroyAllWindows()
#Use the function cv2.imwrite() to save an image
cv2.imwrite('basic pr1.png',img)

plt.imshow(img,cmap= 'red',interpolation = 'bicubic')
plt.plot([50,200],[100,500],'c',linewidth = 10)
plt.show()

