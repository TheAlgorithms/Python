from PIL import Image

"""
Mean thresholding algorithm for image processing
https://en.wikipedia.org/wiki/Thresholding_(image_processing)
"""


def mean_threshold(image: Image) -> Image:
    """
    Apply mean thresholding to a grayscale image.

    Converts image to binary: pixels above mean become white (255),
    pixels below mean become black (0).

    Args:
        image: Grayscale PIL Image object

    Returns:
        Thresholded PIL Image (binary)

    >>> from PIL import Image
    >>> import numpy as np
    >>> arr = np.array([[50, 100], [150, 200]], dtype=np.uint8)
    >>> img = Image.fromarray(arr, mode='L')
    >>> result = mean_threshold(img.copy())
    >>> px = result.load()
    >>> px[0, 0]
    0
    >>> px[1, 1]
    255
    """
    height, width = image.size
    mean = 0
    pixels = image.load()
    for i in range(width):
        for j in range(height):
            pixel = pixels[j, i]
            mean += pixel
    mean //= width * height

    for j in range(width):
        for i in range(height):
            pixels[i, j] = 255 if pixels[i, j] > mean else 0
    return image


if __name__ == "__main__":
    image = mean_threshold(Image.open("path_to_image").convert("L"))
    image.save("output_image_path")
