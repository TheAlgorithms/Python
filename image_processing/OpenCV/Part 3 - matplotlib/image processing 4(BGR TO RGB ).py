import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('model3.jpg',-1)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img2)
plt.show()

cv2.imshow('Hritik bgr',img)
cv2,imshow('Hritik rgb',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img,cmap= 'red',interpolation = 'bicubic')
plt.plot([50,200],[100,500],'c',linewidth = 10)
plt.show()

