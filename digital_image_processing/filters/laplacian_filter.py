# @Author  : ojas-wani
# @File    : laplacian_filter.py
# @Date    : 10/04/2023

from cv2 import (
    BORDER_DEFAULT,
    CV_64F,
    COLOR_BGR2GRAY,
    cvtColor,
    filter2D,
    imread,
    imshow,
    waitKey,
)
from gaussian_filter import gaussian_filter
import numpy as np


def my_laplacian(ksize: int, src: np.ndarray) -> np.ndarray:
    """
    :param src: the source image, which should be a grayscale or color image.
    :param ksize: the size of the kernel used to compute the Laplacian filter,
                  which can be 1, 3, 5 or 7.

    """

    # Create a Laplacian kernel matrix according to the ksize
    if ksize == 1:
        kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    elif ksize == 3:
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    elif ksize == 5:
        kernel = np.array(
            [
                [0, 0, -1, 0, 0],
                [0, -1, -2, -1, 0],
                [-1, -2, 16, -2, -1],
                [0, -1, -2, -1, 0],
                [0, 0, -1, 0, 0],
            ]
        )
    elif ksize == 7:
        kernel = np.array(
            [
                [0, 0, 0, -1, 0, 0, 0],
                [0, 0, -2, -3, -2, 0, 0],
                [0, -2, -7, -10, -7, -2, 0],
                [-1, -3, -10, 68, -10, -3, -1],
                [0, -2, -7, -10, -7, -2, 0],
                [0, 0, -2, -3, -2, 0, 0],
                [0, 0, 0, -1, 0, 0, 0],
            ]
        )

    # Apply the Laplacian kernel using convolution
    laplacian_result = filter2D(
        src, CV_64F, kernel, 0, borderType=BORDER_DEFAULT, anchor=(0, 0)
    )

    return laplacian_result


if __name__ == "__main__":
    # read original image
    img = imread(r"digital_image_processing/image_data/lena.jpg")

    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # Applying gaussian filter
    blur_image = gaussian_filter(gray, 3, sigma=1)

    # Apply multiple Kernel to detect edges
    laplacian_image = my_laplacian(ksize=3, src=blur_image)

    imshow("Original image", img)
    imshow("Deteced edges using laplacian filter", laplacian_image)

    waitKey(0)
