"""
Implementation of Bilateral filter

Inputs:
    img: A 2d image with values in between 0 and 1
    varS: variance in space dimension.
    varI: variance in Intensity.
    N: Kernel size(Must be an odd number)
Output:
    img:A 2d zero padded image with values in between 0 and 1
"""

import cv2
import numpy as np
import math
import sys


def vec_gaussian(img: np.ndarray, variance: float) -> np.ndarray:
    # For applying gaussian function for each element in matrix.
    sigma = math.sqrt(variance)
    cons = 1 / (sigma * math.sqrt(2 * math.pi))
    fImg = cons * np.exp(-((img / sigma) ** 2) * 0.5)
    return fImg


def get_slice(img: np.ndarray, x: int, y: int, kernel_size: int) -> np.ndarray:
    return img[
        x - kernel_size // 2 : x + kernel_size // 2 + 1,
        y - kernel_size // 2 : y + kernel_size // 2 + 1,
    ]


def get_gauss_kernel(kernel_size: int, spatial_variance: float) -> np.ndarray:
    # Creates a gaussian kernel of given dimension.
    arr = np.zeros((kernel_size, kernel_size))
    for i in range(0, kernel_size):
        for j in range(0, kernel_size):
            arr[i, j] = math.sqrt(
                abs(i - kernel_size // 2) ** 2 + abs(j - kernel_size // 2) ** 2
            )
    arr = vec_gaussian(arr, spatial_variance)
    return arr


def bilateral_filter(
    img: np.ndarray,
    spatial_variance: float,
    intensity_variance: float,
    kernel_size: int,
) -> np.ndarray:
    img2 = np.zeros(img.shape)
    gaussKer = get_gauss_kernel(kernel_size, spatial_variance)
    sizeX, sizeY = img.shape
    for i in range(kernel_size // 2, sizeX - kernel_size // 2):
        for j in range(kernel_size // 2, sizeY - kernel_size // 2):

            imgS = get_slice(img, i, j, kernel_size)
            imgI = imgS - imgS[kernel_size // 2, kernel_size // 2]
            imgIG = vec_gaussian(imgI, intensity_variance)
            weights = np.multiply(gaussKer, imgIG)
            vals = np.multiply(imgS, weights)
            val = np.sum(vals) / np.sum(weights)
            img2[i, j] = val
    return img2


if __name__ == "__main__":
    filename = "../image_data/lena.jpg"
    spatial_variance = 1.0
    intensity_variance = 1.0
    kernel_size = 5
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    if len(sys.argv) >= 3:
        spatial_variance = float(sys.argv[2])
    if len(sys.argv) >= 4:
        intensity_variance = float(sys.argv[3])
    if len(sys.argv) >= 5:
        kernel_size = int(sys.argv[4])
        kernel_size = kernel_size + abs(kernel_size % 2 - 1)

    img = cv2.imread(filename, 0)
    cv2.imshow("input image", img)

    out = img / 255
    out = out.astype("float32")
    out = bilateral_filter(out, spatial_variance, intensity_variance, kernel_size)
    out = out * 255
    out = np.uint8(out)
    cv2.imshow("output image", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
