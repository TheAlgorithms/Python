"""
Implementation of Harris Detector

Reference:
C. Harris and M. Stephens, “A Combined Corner and Edge Detector,”
in Proceedings of Alvey Vision Conference 1988, Manchester, 1988, pp. 23.1-23.6.
"""

import cv2 as cv
import numpy as np
from scipy.signal import convolve2d

# Read original image and get gaussian kernel
img = cv.imread('example.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

G = cv.getGaussianKernel(3, 1)

# Begin Harris Detector Computation

I = img_gray.astype('float32')
X = convolve2d(I, [[-1, 0, 1]], mode='same')
Y = convolve2d(I, [[-1], [0], [1]], mode='same')
A = convolve2d(X*X, G, mode='same')
B = convolve2d(Y*Y, G, mode='same')
C = convolve2d(X*Y, G, mode='same')
R = A*B - C*C - 0.04 * (A + B)

# Finished Harris Detector Computation

# Classify all points in R and show corners in image
maxima = np.max(R)
img[R > maxima*0.1] = [255, 0, 0]
cv.imshow('harris_detector', img)
cv.waitKey(0)
