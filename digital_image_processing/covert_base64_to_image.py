
import base64
import cv2
import numpy as np


def load_base64_2_image(base64_string: str, grayscale: bool = False, color_mode: str = 'rgb',
                        target_size: tuple = None, interpolation: str = 'AREA') -> any:
    """Load Base64 string image to CV2 image format.
    >>>load_base64_2_image(base64_string)
    array([[[82, 79, 75],
        [82, 79, 76],
        [82, 79, 76],
        ...,
        [81, 80, 76],
        [82, 79, 76],
        [82, 79, 76]],

       [[66, 63, 59],
        [60, 57, 54],
        [60, 57, 53],
        ...,
        [61, 56, 54],
        [61, 57, 54],
        [60, 57, 54]],

       [[39, 34, 31],
        [39, 35, 31],
        [39, 35, 32],
        ...,
        [38, 35, 31],
        [39, 35, 31],
        [39, 35, 30]],

       ...,

       [[46, 39, 35],
        [45, 38, 35],
        [44, 40, 35],
        ...,
        [45, 39, 34],
        [44, 39, 34],
        [45, 39, 35]],

       [[45, 39, 34],
        [45, 39, 35],
        [46, 40, 35],
        ...,
        [44, 40, 35],
        [45, 40, 35],
        [44, 39, 36]],

       [[44, 39, 35],
        [45, 39, 35],
        [45, 39, 34],
        ...,
        [46, 38, 35],
        [45, 39, 35],
        [45, 40, 35]]], dtype=uint8)
    Usage:

    ```
    image = load_base64_2_image(base64_string)

    ```

    Args:
      base64_string: base64 of image file
      grayscale:  use `color_mode="grayscale"`.
        color_mode: One of "grayscale", "rgb", "rgba". Default: "rgb".
            The desired image format.
        target_size: Either `None` (default to original size)
            or tuple of ints `(img_height, img_width)`.

        interpalation: "NEAREST","LINEAR","AREA","CUBIC","LANCZOS4"

    Returns:
      A CV2 Image instance.

    Raises:
      ImportError: if CV2 is not available.
      ValueError: if interpolation method is not supported.
      ValueError: if base64 string not image base64 or padding error

    """
    base64_string = str(base64_string)
    color_mode = color_mode.upper()

    inter = {

        "NEAREST": cv2.INTER_NEAREST,
        "AREA": cv2.INTER_AREA,
        "CUBIC": cv2.INTER_CUBIC,
        "LINEAR": cv2.INTER_LINEAR,
        "LANCZOS4": cv2.INTER_LANCZOS4
    }

    try:
        image = base64.b64decode(base64_string.split(',')[1])

        np_image = np.frombuffer(image, dtype=np.uint8)
        image = cv2.imdecode(np_image, flags=1)

    except ValueError:
        raise ValueError("Can't decode base64string to CV2 format.")

    if grayscale:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    try:
        if target_size:
            image = cv2.resize(image, dim=target_size,
                               interpolation=inter[interpolation])
    except ValueError:
        raise ValueError("interpolation error")

    return image
