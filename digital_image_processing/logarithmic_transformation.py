"""
Logarithmic(Log) Transformation of an image is a type of gray level image
transformations which replaces all pixel values in the original image
with its logarithmic values.

The formula is:

S =  255 * (log(input_image_pixel_value + 1) / log(1 + max_input_image_pixel_value))

The script is inspired from
* https://www.geeksforgeeks.org/log-transformation-of-an-image-using-python-and-opencv

"""

import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey


def logarithmic_transformation(image: np.array) -> np.array:
    # Transforming pixel values
    image_log = (np.log(image + 1) / np.log(1 + np.max(image))) * 255

    # Using dtype = np.uint8 to convert float value to int
    image_log = np.array(image_log, dtype=np.uint8)

    return image_log


if __name__ == "__main__":
    # Read pixel values of original image
    image = imread("image_data/lena.jpg")

    # Apply log transformation
    image_log_transform = logarithmic_transformation(image)

    # Show Transformed Image
    imshow("Log transform of original image", image_log_transform)
    waitKey(0)
    destroyAllWindows()
