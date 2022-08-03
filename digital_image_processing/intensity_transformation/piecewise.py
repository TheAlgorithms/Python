import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r"../image_data/lena.jpg", 0)
cv2.imshow('original ', image)

r1 = 100
s1 = 50
r2 = 180
s2 = 200


def pixel_value(img, r1, s1, r2, s2):
    if (0 <= img and img <= r1):
        return (s1/r1)*img
    elif (r1 <= img and img <= r2):
        return ((s2-s1)/(r2-r1)) * (img-r1)+s1
    else:
        return ((255-s2)/(255-r2)) * (img-r2)+s2


picture_value = np.vectorize(pixel_value)

piecewise_value = picture_value(image, r1, s1, r2, s2)
piecewise_value = piecewise_value.astype(np.uint8)
cv2.imshow('const_value', piecewise_value)
cv2.waitKey(0)
