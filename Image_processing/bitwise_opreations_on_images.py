import cv2
import numpy as np

# bitwise Operations very useful when working with masks
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\image_1.jpg")

# TODO: Bitwise OPerations On images -->
# equating sizes of both images ->
img1 = cv2.resize(img1, (312, 312))
img2 = cv2.resize(img2, (312, 312))

# bitAnd = cv2.bitwise_and(img2, img1)  # performs AND operation
# bitOr = cv2.bitwise_or(img2, img1) # performs OR operation
# bitXOr = cv2.bitwise_xor(img1, img2) #performs XOR Operation
bitNot = cv2.bitwise_not(img1) # performs NOT operation (takes single input)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

# cv2.imshow('bitAnd', bitAnd)
# cv2.imshow('bitOr', bitOr)
# cv2.imshow('bitXOr', bitXOr)
cv2.imshow('bitNot', bitNot)
cv2.imshow('bitNot2', bitNot2)


cv2.waitKey(0)
cv2.destroyAllWindows()
