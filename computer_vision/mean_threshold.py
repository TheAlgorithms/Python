from PIL import Image

"""
Mean thresholding algorithm for image processing
https://en.wikipedia.org/wiki/Thresholding_(image_processing)
"""


def mean_threshold(image: Image.Image) -> Image.Image:
    """
    image: is a grayscale PIL image object
    """
    height, width = image.size
    mean = 0
    pixels = image.load()
    if pixels is None:
        raise ValueError("image does not support pixel access")
    for i in range(width):
        for j in range(height):
            pixel = pixels[j, i]
            assert isinstance(pixel, int | float)  # grayscale images only
            mean += pixel
    mean //= width * height

    for j in range(width):
        for i in range(height):
            pixel = pixels[i, j]
            assert isinstance(pixel, int | float)  # grayscale images only
            pixels[i, j] = 255 if pixel > mean else 0
    return image


if __name__ == "__main__":
    image = mean_threshold(Image.open("path_to_image").convert("L"))
    image.save("output_image_path")
