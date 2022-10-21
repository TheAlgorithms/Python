import cv2 as cv
import numpy as np

def hough_transform(path_to_img):
    img = cv.imread(path_to_img,1)#path to image
    edges = cv.Canny(img,100,200) #canny edge detector to detect images

    edges = cv.Canny(img, 50, 150, apertureSize=3) #canny edge detector
    lines = cv.HoughLines(edges, 1, np.pi / 180, 200) #hough lines

    for line in lines: #iterating lines to find hough lines
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
        x1 = int(x0 + 1000 * (-b))
        # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
        y1 = int(y0 + 1000 * (a))
        # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
        x2 = int(x0 - 1000 * (-b))
        # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
        y2 = int(y0 - 1000 * (a))
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2) #placing lines on original image

    img = cv.resize(img,(600,450))
    return img
