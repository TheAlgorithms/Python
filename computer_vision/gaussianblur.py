"""
Gaussian Blur applied for blurring an image
More information on:
https://en.wikipedia.org/wiki/Gaussian_blur"""

import numpy as np
import cv2

def gaussianblur(size, img, sigma = 1):

    size = int(size) // 2
    X, Y = np.mgrid[-size:size + 1, -size:size + 1]
    constant = 1 / (2.0 * np.pi * sigma ** 2)
    guassian = np.exp(-((X ** 2 + Y ** 2) / (2.0 * sigma ** 2))) * constant
    blurred = cv2.filter2D(gray, -1, guassian)
    return blurred

if __name__ == "__main__":

    img = cv2.imread(r'path_to_image')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = gaussianblur(4, gray, 1.3)
    cv2.imshow('Blurred Image', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
