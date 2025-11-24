import numpy as np
from PIL import Image

"""
Otsu thresholding algorithm for image processing
https://en.wikipedia.org/wiki/Otsu%27s_method
"""


def otsu_threshold(image: Image) -> Image:
    """
    Applies Otsu's thresholding method to a grayscale image.

    Parameters:
    image (PIL.Image.Image): A grayscale PIL image object.

    Returns:
    PIL.Image.Image: A binary image after applying Otsu's thresholding.

    Example:
    >>> from PIL import Image
    >>> import numpy as np
    >>> image_array = np.array(
    ...     [[0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255]],
    ...     dtype=np.uint8
    ... )
    >>> image = Image.fromarray(image_array)
    >>> binary_image = otsu_threshold(image)
    >>> np.array(binary_image)
    array([[  0,   0,   0,   0],
           [255, 255, 255, 255],
           [  0,   0,   0,   0],
           [255, 255, 255, 255]], dtype=uint8)
    """
    # Convert the image to numpy array
    pixel_array = np.array(image)

    # Compute histogram
    hist, _ = np.histogram(pixel_array, bins=256, range=(0, 256))

    # Compute between class variance
    total_pixels = pixel_array.size
    current_max, threshold = 0.0, 0  # Ensure current_max is a float
    sum_total, sum_foreground = 0.0, 0.0  # Ensure these are floats
    weight_background, weight_foreground = 0.0, 0.0  # Ensure these are floats

    for i in range(256):
        sum_total += i * hist[i]

    for i in range(256):
        weight_background += hist[i]
        if weight_background == 0:
            continue
        weight_foreground = total_pixels - weight_background
        if weight_foreground == 0:
            break
        sum_foreground += i * hist[i]

        mean_background = sum_foreground / weight_background
        mean_foreground = (sum_total - sum_foreground) / weight_foreground

        between_class_variance = (
            weight_background
            * weight_foreground
            * (mean_background - mean_foreground) ** 2
        )

        if between_class_variance > current_max:
            current_max = between_class_variance
            threshold = i

    # Apply threshold to the image
    binary_image = pixel_array > threshold
    binary_image = binary_image.astype(np.uint8) * 255

    # Convert numpy array back to PIL image
    return Image.fromarray(binary_image)
