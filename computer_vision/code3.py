# importing libraries

import cv2
import numpy as np
import time

def resizeFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dims = (width, height)

    return(cv2.resize(frame, dims, interpolation=cv2.INTER_AREA))

#image = cv2.imread("files/flower.jpg")
#cv2.imshow("original", image)
#resized = resizeFrame(image.copy(), scale=0.50)
#cv2.imshow("resized", resized)
#cv2.waitKey(0)

video = cv2.VideoCapture("files/demo.mp4")

while(video.isOpened()):
    ret, image = video.read()
    fps = int(video.get(cv2.CAP_PROP_FPS))
    resized = resizeFrame(image, scale=0.50)
    if ret:
        time.sleep(1/fps)
        cv2.imshow("original video feed output", image)
        cv2.imshow("Resized video feed output", resized)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break

video.release()
cv2.destroyAllWindows()

