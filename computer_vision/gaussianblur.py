"""
Gaussian Blur applied for blurring an image
More information on:
https://en.wikipedia.org/wiki/Gaussian_blur
"""

import cv2
import numpy as np


def gaussian_blur(size, img, sigma=1):

    size = int(size) // 2
    x1, y1 = np.mgrid[-size : size + 1, -size : size + 1]
    constant = 1 / (2.0 * np.pi * sigma ** 2)
    gaussian = np.exp(-((x1 ** 2 + y1 ** 2) / (2.0 * sigma ** 2))) * constant
    blurred = cv2.filter2D(img, -1, gaussian)
    return blurred


if __name__ == "__main__":

    image = cv2.imread(r"path_to_image")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = gaussian_blur(4, gray_image, 1.3)
    cv2.imshow("Blurred Image", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
