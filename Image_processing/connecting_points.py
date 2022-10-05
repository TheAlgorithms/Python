import numpy as np
import cv2


def click_event(event, x, y, flags, param):  # x and y are coordinates on image where we click using mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)  # joining last and second last element
        cv2.imshow('image', img)


img = np.zeros((512, 512, 3), np.uint8)
# img = cv2.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\lena.jpg')

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
points = []
cv2.waitKey(0)
cv2.destroyAllWindows()
