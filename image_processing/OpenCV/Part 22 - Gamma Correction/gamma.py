import cv2
import numpy as np

def gamma_filter(image , gamma = 1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
	    for i in np.arange(0, 256)]).astype("uint8")
 
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

# read image
frame = cv2.imread('car1.jpg')

for gamma in np.arange(0.0,3.5,0.5):
    if gamma ==1:
        continue

    gamma = gamma if gamma>0 else 0.1
    output = gamma_filter(frame ,gamma)
    cv2.putText(output ,"gamma={}".format(gamma) , (10,30) , cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,120, 255), 2)
    cv2.imshow("images" , np.hstack([frame,output]))
    cv2.waitKey(0)
