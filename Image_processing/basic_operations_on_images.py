import numpy as np
import cv2

img = cv2.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\messi5.jpg')
img2 = cv2.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\opencv-logo.png')

print(img.shape)  # returns a tuple of number of rows, columns, and channels
print(img.size)  # returns Total number of pixels is accessed
print(img.dtype)  # returns Image datatype is obtained
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# TODO: ROI --> Region Of Interest (A particular region in an image in which you want to work)
ball = img[280:340, 330:390]  # copying ball using its upper and below coordinates to place at another place
img[273:333, 100:160] = ball  # placing ball to another place

# TODO: Adding Two Images ->
# to add images you need to have the images or arrays of same size otherwise there is an error appear
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
# cv2.imshow('image', dst)

# adding images using addWeighted method ->
dst = cv2.addWeighted(img,0.7,img2,0.3,0) # 2nd and 4th arguments are the weights of images, 5th argument is value of gamma(to add any scalar)
cv2.imshow('image', dst)

# cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
