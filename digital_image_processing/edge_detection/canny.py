import cv2
import numpy as np
from digital_image_processing.filters.convolve import img_convolve
from digital_image_processing.filters.sobel_filter import sobel_filter

"""
doctests:
>>> gen_gaussian_kernel(9, sigma=1.4)
array([[3.23914970e-05, 1.93177651e-04, 6.91677937e-04, 1.48686709e-03,
        1.91894072e-03, 1.48686709e-03, 6.91677937e-04, 1.93177651e-04,
        3.23914970e-05],
        [1.93177651e-04, 1.15208027e-03, 4.12505538e-03, 8.86743491e-03,
        1.14442522e-02, 8.86743491e-03, 4.12505538e-03, 1.15208027e-03,
        1.93177651e-04],
        [6.91677937e-04, 4.12505538e-03, 1.47698752e-02, 3.17500967e-02,
        4.09764623e-02, 3.17500967e-02, 1.47698752e-02, 4.12505538e-03,
        6.91677937e-04],
        [1.48686709e-03, 8.86743491e-03, 3.17500967e-02, 6.82516694e-02,
        8.80851478e-02, 6.82516694e-02, 3.17500967e-02, 8.86743491e-03,
        1.48686709e-03],
        [1.91894072e-03, 1.14442522e-02, 4.09764623e-02, 8.80851478e-02,
        1.13682102e-01, 8.80851478e-02, 4.09764623e-02, 1.14442522e-02,
        1.91894072e-03],
        [1.48686709e-03, 8.86743491e-03, 3.17500967e-02, 6.82516694e-02,
        8.80851478e-02, 6.82516694e-02, 3.17500967e-02, 8.86743491e-03,
        1.48686709e-03],
        [6.91677937e-04, 4.12505538e-03, 1.47698752e-02, 3.17500967e-02,
        4.09764623e-02, 3.17500967e-02, 1.47698752e-02, 4.12505538e-03,
        6.91677937e-04],
        [1.93177651e-04, 1.15208027e-03, 4.12505538e-03, 8.86743491e-03,
        1.14442522e-02, 8.86743491e-03, 4.12505538e-03, 1.15208027e-03,
        1.93177651e-04],
        [3.23914970e-05, 1.93177651e-04, 6.91677937e-04, 1.48686709e-03,
        1.91894072e-03, 1.48686709e-03, 6.91677937e-04, 1.93177651e-04,
        3.23914970e-05]])
"""

PI = 180

def gen_gaussian_kernel(k_size, sigma):
    center = k_size // 2
    x, y = np.mgrid[0 - center:k_size - center, 0 - center:k_size - center]
    g = 1 / (2 * np.pi * sigma) * np.exp(-(np.square(x) + np.square(y)) / (2 * np.square(sigma)))
    return g


def canny(image, threshold_low=15, threshold_high=30, weak=128, strong=255):
    image_row, image_col = image.shape[0], image.shape[1]
    # gaussian_filter
    gaussian_out = img_convolve(image, gen_gaussian_kernel(9, sigma=1.4))
    # get the gradient and degree by sobel_filter
    sobel_grad, sobel_theta = sobel_filter(gaussian_out)
    gradient_direction = np.rad2deg(sobel_theta)
    gradient_direction += PI

    dst = np.zeros((image_row, image_col))

    """
    Non-maximum suppression. If the edge strength of the current pixel is the largest compared to the other pixels 
    in the mask with the same direction, the value will be preserved. Otherwise, the value will be suppressed. 
    """
    for row in range(1, image_row - 1):
        for col in range(1, image_col - 1):
            direction = gradient_direction[row, col]

            if (
                0 <= direction < 22.5
                    or 15 * PI / 8 <= direction <= 2 * PI
                    or 7 * PI / 8 <= direction <= 9 * PI / 8
            ):
                W = sobel_grad[row, col - 1]
                E = sobel_grad[row, col + 1]
                if sobel_grad[row, col] >= W and sobel_grad[row, col] >= E:
                    dst[row, col] = sobel_grad[row, col]

            elif (PI / 8 <= direction < 3 * PI / 8) or (9 * PI / 8 <= direction < 11 * PI / 8):
                SW = sobel_grad[row + 1, col - 1]
                NE = sobel_grad[row - 1, col + 1]
                if sobel_grad[row, col] >= SW and sobel_grad[row, col] >= NE:
                    dst[row, col] = sobel_grad[row, col]

            elif (3 * PI / 8 <= direction < 5 * PI / 8) or (11 * PI / 8 <= direction < 13 * PI / 8):
                N = sobel_grad[row - 1, col]
                S = sobel_grad[row + 1, col]
                if sobel_grad[row, col] >= N and sobel_grad[row, col] >= S:
                    dst[row, col] = sobel_grad[row, col]

            elif (5 * PI / 8 <= direction < 7 * PI / 8) or (13 * PI / 8 <= direction < 15 * PI / 8):
                NW = sobel_grad[row - 1, col - 1]
                SE = sobel_grad[row + 1, col + 1]
                if sobel_grad[row, col] >= NW and sobel_grad[row, col] >= SE:
                    dst[row, col] = sobel_grad[row, col]

            """
            High-Low threshold detection. If an edge pixel’s gradient value is higher than the high threshold
            value, it is marked as a strong edge pixel. If an edge pixel’s gradient value is smaller than the high
            threshold value and larger than the low threshold value, it is marked as a weak edge pixel. If an edge
            pixel's value is smaller than the low threshold value, it will be suppressed.
            """
            if dst[row, col] >= threshold_high:
                dst[row, col] = strong
            elif dst[row, col] <= threshold_low:
                dst[row, col] = 0
            else:
                dst[row, col] = weak

    """
    Edge tracking. Usually a weak edge pixel caused from true edges will be connected to a strong edge pixel while
    noise responses are unconnected. As long as there is one strong edge pixel that is involved in its 8-connected
    neighborhood, that weak edge point can be identified as one that should be preserved.
    """
    for row in range(1, image_row):
        for col in range(1, image_col):
            if dst[row, col] == weak:
                if 255 in (
                        dst[row, col + 1],
                        dst[row, col - 1],
                        dst[row - 1, col],
                        dst[row + 1, col],
                        dst[row - 1, col - 1],
                        dst[row + 1, col - 1],
                        dst[row - 1, col + 1],
                        dst[row + 1, col + 1],
                ):
                    dst[row, col] = strong
                else:
                    dst[row, col] = 0

    return dst


if __name__ == '__main__':
    # read original image in gray mode
    lena = cv2.imread(r'../image_data/lena.jpg', 0)
    # canny edge detection
    canny_dst = canny(lena)
    cv2.imshow('canny', canny_dst)
    cv2.waitKey(0)
