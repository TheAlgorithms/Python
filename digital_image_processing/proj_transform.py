# import necessary libraries
import cv2
import numpy as np

# read the image using opencv
img_input = cv2.imread("./image_data/lena.jpg")

# set the width and height of the output image in px
# width, height = 718, 718

height = img_input.shape[0]
width = img_input.shape[1]

# set the initial coordinates of the four points
pts1 = np.float32([[0, height], [width, height], [width, 0], [0, 0]])

# set the final coordinates of the four points
pts2 = np.float32([[142, 142], [362, 32], [418, 358], [127, 461]])

# get the projective transformation matrix
trns_matrix = cv2.getPerspectiveTransform(pts1, pts2)


# apply the projective transformation
img_output = cv2.warpPerspective(img_input, trns_matrix, (width, height))

# display the original and the final image
cv2.imshow("Original Image", img_input)
cv2.imshow("Final Image", img_output)

# end the program on pressing some key
cv2.waitKey(0)
cv2.destroyAllWindows()
