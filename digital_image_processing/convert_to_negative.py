"""
Implemented an algorithm using opencv to convert a colored image into its negative
"""

import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey


def convert_to_negative(img):
    """
    Convert an image to its negative.

    Args:
        img: NumPy array representing the image (BGR format)

    Returns:
        NumPy array with inverted colors

    >>> import numpy as np
    >>> img = np.array([[[100, 150, 200]]], dtype=np.uint8)
    >>> result = convert_to_negative(img.copy())
    >>> result[0][0].tolist()
    [155, 105, 55]
    >>> img2 = np.array([[[0, 0, 0]], [[255, 255, 255]]], dtype=np.uint8)
    >>> neg = convert_to_negative(img2.copy())
    >>> neg[0][0].tolist()
    [255, 255, 255]
    >>> neg[1][0].tolist()
    [0, 0, 0]
    """
    # getting number of pixels in the image
    pixel_h, pixel_v = img.shape[0], img.shape[1]

    # converting each pixel's color to its negative
    for i in range(pixel_h):
        for j in range(pixel_v):
            img[i][j] = [255, 255, 255] - img[i][j]

    return img


if __name__ == "__main__":
    # read original image
    img = imread("image_data/lena.jpg", 1)

    # convert to its negative
    neg = convert_to_negative(img)

    # show result image
    imshow("negative of original image", img)
    waitKey(0)
    destroyAllWindows()
