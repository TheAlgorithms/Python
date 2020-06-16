from PIL import Image

def change_brightness(img: Image, level: float) -> Image:
    """
    Change the brightness of a PIL Image to a given level.
    """
    factor = (259 + (level + 255)) / (255 + (259 - level))

    def brightness(c: int) -> float:
        """
        Fundamental Transformation/Operation that'll be performed on
        every bit.
        """
        return 128 + factor * (c - 128)

    return img.point(brightness)

if __name__ == "__main__":
    # Load image
    with Image.open("image_data/lena.jpg") as img:
        # Change brightness to 170
        brigt_img = change_brightness(img, 170)
        brigt_img.save("image_data/lena_high_contrast.png", format="png")
