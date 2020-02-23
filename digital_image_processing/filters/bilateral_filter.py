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


def vec_gaussian(img: np.ndarray, var: float) -> np.ndarray:
    # For applying gaussian function for each element in matrix.
    sigma = math.sqrt(var)
    cons = 1 / (sigma * math.sqrt(2 * math.pi))
    fImg = cons * np.exp(-((img / sigma) ** 2) * 0.5)
    return fImg


def getSlice(img: np.ndarray, x: int, y: int, N: int) -> np.ndarray:
    return img[x - N // 2 : x + N // 2 + 1, y - N // 2 : y + N // 2 + 1]


def getGaussKernel(N: int, varS: float) -> np.ndarray:
    # Creates a gaussian kernel of given dimension.
    arr = np.zeros((N, N))
    for i in range(0, N):
        for j in range(0, N):
            arr[i, j] = math.sqrt(abs(i - N // 2) ** 2 + abs(j - N // 2) ** 2)
    arr = vec_gaussian(arr, varS)
    return arr


def bilateral_filter(img: np.ndarray, varS: float, varI: float, N: int) -> np.ndarray:
    img2 = np.zeros(img.shape)
    gaussKer = getGaussKernel(N, varS)
    sizeX, sizeY = img.shape
    for i in range(N // 2, sizeX - N // 2):
        for j in range(N // 2, sizeY - N // 2):

            imgS = getSlice(img, i, j, N)
            imgI = imgS - imgS[N // 2, N // 2]
            imgIG = vec_gaussian(imgI, varI)
            weights = np.multiply(gaussKer, imgIG)
            vals = np.multiply(imgS, weights)
            val = np.sum(vals) / np.sum(weights)
            img2[i, j] = val
    return img2


if __name__ == "__main__":
    filename = "../image_data/lena.jpg"
    varS = 1.0
    varI = 1.0
    N = 5
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    if len(sys.argv) >= 3:
        varS = float(sys.argv[2])
    if len(sys.argv) >= 4:
        varI = float(sys.argv[3])
    if len(sys.argv) >= 5:
        N = int(sys.argv[4])
        N = N + abs(N % 2 - 1)

    img = cv2.imread(filename, 0)
    cv2.imshow("input image", img)

    out = img / 255
    out = out.astype("float32")
    out = bilateral_filter(out, varS, varI, N)
    out = out * 255
    out = np.uint8(out)
    cv2.imshow("output image", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
