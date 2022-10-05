import numpy as np
import cv2


# filtering all function names and variable names which contains name-> EVENT

# events = [i for i in dir(cv2) if 'EVENT' in i]  # dir->iterating over all the functions variables in cv2(here)
# print(events)

# TODO: creating callback function which invokes for mouse events
def click_event(event, x, y, flags, param):  # x and y are coordinates on image where we click using mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow('image', img)  # here image is window name

    # TODO: printing BGR channels on right click ->
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green)+', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('G:\programming\EYRC#2021\opencv-master\opencv-master\samples\data\lena.jpg')

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
