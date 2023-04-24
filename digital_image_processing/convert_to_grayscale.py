"""
    Implemented an algorithm using opencv to convert a colored image into its grayscale
"""
from cv2 import destroyAllWindows, imread, imshow, waitKey
import numpy as np
import doctest


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    # getting number of pixels in the image
    pixel_h, pixel_v = img.shape[0], img.shape[1]

    # converting each pixel's color to its grayscale
    for i in range(pixel_h):
        for j in range(pixel_v):
            luminance = (
                0.299 * img[i][j][2] + 0.587 * img[i][j][1] + 0.114 * img[i][j][0]
            )
            img[i][j] = (luminance, luminance, luminance)

    return img


if __name__ == "__main__":
    # read original image
    img = imread("image_data/lena.jpg", 1)

    # convert to its grayscale
    neg = convert_to_grayscale(img)

    # show result image
    imshow("grayscale of original image", img)
    waitKey(0)
    destroyAllWindows()
    doctest.testmod()
