# @Author  : ojas-wani
# @File    : laplacian_filter.py
# @Date    : 10/04/2023

import cv2
from cv2 import (
    BORDER_DEFAULT,
    COLOR_BGR2GRAY,
    cvtColor,
    filter2D,
    imshow,
    waitKey,
)

from digital_image_processing.filters.gaussian_filter import gaussian_filter
import numpy as np


def my_laplacian(ksize: int, src: np.ndarray) -> np.ndarray:
    """
    :param src: the source image, which should be a grayscale or color image.
    :param ksize: the size of the kernel used to compute the Laplacian filter,

                  which can be 1, 3, 5, or 7.

    >>> my_laplacian(src=np.array([]), ksize=0)
    Traceback (most recent call last):
        ...
    ValueError: ksize must be in (1, 3, 5, 7)
    """
    kernels = {
        1: np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]),
        3: np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),
        5: np.array(
            [
                [0, 0, -1, 0, 0],
                [0, -1, -2, -1, 0],
                [-1, -2, 16, -2, -1],
                [0, -1, -2, -1, 0],
                [0, 0, -1, 0, 0],
            ]
        ),
        7: np.array(
            [
                [0, 0, 0, -1, 0, 0, 0],
                [0, 0, -2, -3, -2, 0, 0],
                [0, -2, -7, -10, -7, -2, 0],
                [-1, -3, -10, 68, -10, -3, -1],
                [0, -2, -7, -10, -7, -2, 0],
                [0, 0, -2, -3, -2, 0, 0],
                [0, 0, 0, -1, 0, 0, 0],
            ]
        ),
    }
    if ksize not in kernels:
        msg = f"ksize must be in {tuple(kernels)}"
        raise ValueError(msg)

    # Apply the Laplacian kernel using convolution
    return filter2D(
        src, cv2.CV_64F, kernels[ksize], 0, borderType=BORDER_DEFAULT, anchor=(0, 0)
    )


if __name__ == "__main__":
    # read original image
    img = cv2.imread(r"../image_data/lena.jpg")

    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # Applying gaussian filter
    blur_image = gaussian_filter(gray, 3, sigma=1)

    # Apply multiple Kernel to detect edges
    laplacian_image = my_laplacian(ksize=3, src=blur_image)

    imshow("Original image", img)

    imshow("Detected edges using laplacian filter", laplacian_image)

    waitKey(0)
