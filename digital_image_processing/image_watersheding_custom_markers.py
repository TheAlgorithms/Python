import cv2
import numpy as np
from matplotlib import cm

# loading the image (kept in the same directory)
img = cv2.imread(r"digital_image_processing/image_data/scenery.jpg")
img_copy = img.copy()

# defining marker image & segmented image
marker_image = np.zeros(img.shape[:2], dtype=np.int32)
segments = np.zeros(img.shape, dtype=np.uint8)

"""
creating function for defining color
"""


def create_rgb(i):
    return np.array(cm.tab10(i)[:3]) * 255


# create color tuple for each  key 0-9
colors = []
for i in range(10):
    colors.append(create_rgb(i))


# variables
n_markers = 10
current_marker = 1
marks_updated = False


# callback function


def mouse_callback(event, x, y, flags, params):
    global marks_updated

    if event == cv2.EVENT_LBUTTONDOWN:
        # write on the marker image
        cv2.circle(marker_image, (x, y), 10, (current_marker), -1)

        # user sees on the image
        cv2.circle(img_copy, (x, y), 10, colors[current_marker], -1)

        marks_updated = True


cv2.namedWindow("Image")

cv2.setMouseCallback("Image", mouse_callback)


while True:
    cv2.imshow("Watershed_Segments", segments)
    cv2.imshow("Image", img_copy)

    k = cv2.waitKey(1)

    # exit when esc pressed
    if k == 27:
        break

    # reset if 'c' is pressed

    elif k == ord("c"):
        img_copy = img.copy()
        marker_image = np.zeros(img.shape[0:2], dtype=np.int32)
        segments = np.zeros(img.shape, dtype=np.uint8)

    # update color choice (if 0-9 any no. is pressed)
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    # update markings
    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(img, marker_image_copy)

        segments = np.zeros(img.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            segments[marker_image_copy == (color_ind)] = colors[color_ind]

        marks_updated = False


cv2.destroyAllWindows()
