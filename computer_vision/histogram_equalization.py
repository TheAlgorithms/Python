import cv2
import numpy as np

"""
Histogram Equalization for Image Enhancement
https://en.wikipedia.org/wiki/Histogram_equalization
"""


def hist_equalization(image):
    """
    Returns the histogram equalization image
    :param image: input image
    """
    l_channel, a_channel, b_channel = cv2.split(image)
    histogram = cv2.calcHist([l_channel], [0], None, [256], [0, 256])
    histogram_sum = np.sum(histogram)
    probability_density_function = histogram / histogram_sum
    cumulative_distribution_function = np.cumsum(probability_density_function)
    lookup_table = np.round(cumulative_distribution_function * 255).astype(np.uint8)
    equalized_l = cv2.LUT(l_channel, lookup_table)
    new_image = cv2.merge((equalized_l, a_channel, b_channel))
    new_image = cv2.cvtColor(new_image, cv2.COLOR_LAB2BGR)
    return new_image


if __name__ == "__main__":
    image = cv2.imread("path_to_image")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    new_image = hist_equalization(image)
    cv2.imshow("image", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
