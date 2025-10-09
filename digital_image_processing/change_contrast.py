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
    Function to change contrast
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
