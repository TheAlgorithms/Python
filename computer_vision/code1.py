# importing libraries

import cv2
import time

# create an object which will hold an image number array 

#image = cv2.imread("files/bentley.jpg")
#cv2.imshow("car image", image)
#cv2.waitKey(0)

video = cv2.VideoCapture("files/demo.mp4")

while(video.isOpened()):
    ret, image = video.read()
    fps = int(video.get(cv2.CAP_PROP_FPS))
    if ret:
        time.sleep(1/fps)
        cv2.imshow("video feed output", image)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break

video.release()
cv2.destroyAllWindows()
