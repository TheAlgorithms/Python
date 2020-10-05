from cv2 import cv2
import numpy as np
from skimage.feature import local_binary_pattern as lbp

def resize(frame):
    img = cv2.resize(frame, (800, 800))
    return img

def normalize(arr):
    range_ = arr.max() - arr.min()
    arr = arr / range_
    return arr

def pattern(img, radius=3, points=8):
    # Params
    n_points = points * radius
    img = normalize(img)
    img1 = lbp(img, radius, n_points)
    img1 = normalize(img1)
    original_image = resize(img)
    lbp_image = resize(img1)
    stack = np.hstack([original_image, lbp_image])
    return stack

if __name__ == "__main__":
    # read original image in gray mode
    lena = cv2.imread("./lena.jpg")
    # color BGR --> Gray
    gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
    stack = pattern(gray)
    cv2.imshow("Local Binary Pattern", stack)
    cv2.waitKey(0)
