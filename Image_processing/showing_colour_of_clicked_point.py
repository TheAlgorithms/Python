# TODO: Showing colour of the point wherever you click on image in a new window
import numpy as np
import cv2


def click_event(event, x, y, flags, param):  # x and y are coordinates on image where we click using mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolourImage = np.zeros((512, 512, 3), np.uint8)
        mycolourImage[:] = [blue, green, red]
        cv2.imshow('color', mycolourImage)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\lena.jpg')

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
points = []
cv2.waitKey(0)
cv2.destroyAllWindows()
