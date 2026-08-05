from PIL import Image


def change_brightness(img: Image, level: float) -> Image:
    """
    Change the brightness of a PIL Image to a given level.

    Args:
        img: PIL Image to adjust
        level: Brightness level adjustment (-255.0 to 255.0)
               Negative values darken, positive values brighten

    Returns:
        New PIL Image with adjusted brightness

    Raises:
        ValueError: If level is not in range [-255.0, 255.0]

    >>> from PIL import Image
    >>> import numpy as np
    >>> img = Image.new('RGB', (2, 2), color=(100, 100, 100))
    >>> bright = change_brightness(img, 50)
    >>> px = bright.load()
    >>> px[0, 0]
    (150, 150, 150)
    >>> dark = change_brightness(img, -50)
    >>> px_dark = dark.load()
    >>> px_dark[0, 0]
    (50, 50, 50)
    >>> change_brightness(img, 300)
    Traceback (most recent call last):
        ...
    ValueError: level must be between -255.0 (black) and 255.0 (white)
    """

    def brightness(c: int) -> float:
        """
        Fundamental Transformation/Operation that'll be performed on
        every bit.
        """
        return 128 + level + (c - 128)

    if not -255.0 <= level <= 255.0:
        raise ValueError("level must be between -255.0 (black) and 255.0 (white)")
    return img.point(brightness)


if __name__ == "__main__":
    # Load image
    with Image.open("image_data/lena.jpg") as img:
        # Change brightness to 100
        brigt_img = change_brightness(img, 100)
        brigt_img.save("image_data/lena_brightness.png", format="png")
