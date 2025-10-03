"""
Changing contrast with PIL

This algorithm is used in
https://noivce.pythonanywhere.com/ Python web app.

psf/black: True
ruff : True
"""

from PIL import Image


def change_contrast(img: Image, level: int) -> Image:
    """
    Change the contrast of a PIL Image.

    Args:
        img: PIL Image to adjust
        level: Contrast level (-255 to 255)

    Returns:
        New PIL Image with adjusted contrast

    >>> from PIL import Image
    >>> img = Image.new('RGB', (2, 2), color=(128, 128, 128))
    >>> high_contrast = change_contrast(img, 100)
    >>> isinstance(high_contrast, Image.Image)
    True
    >>> low_contrast = change_contrast(img, -50)
    >>> isinstance(low_contrast, Image.Image)
    True
    """
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c: int) -> int:
        """
        Fundamental Transformation/Operation that'll be performed on
        every bit.
        """
        return int(128 + factor * (c - 128))

    return img.point(contrast)


if __name__ == "__main__":
    # Load image
    with Image.open("image_data/lena.jpg") as img:
        # Change contrast to 170
        cont_img = change_contrast(img, 170)
        cont_img.save("image_data/lena_high_contrast.png", format="png")
