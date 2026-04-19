"""
Module for adjusting the brightness of images using PIL.
"""
from PIL import Image


def change_brightness(img: Image.Image, level: float) -> Image.Image:
    """Change the brightness of a PIL Image by the given level.

    Args:
        img: The input PIL Image to modify.
        level: Brightness adjustment level between -255.0 (darker) and
               255.0 (brighter). 0 means no change.

    Returns:
        A new Image with adjusted brightness.

    Raises:
        ValueError: If level is outside the valid range [-255.0, 255.0].

    Examples:
    >>> from PIL import Image
    >>> img = Image.new("RGB", (10, 10), (128, 128, 128))
    >>> bright_img = change_brightness(img, 50)
    >>> bright_img.getpixel((5, 5))  # doctest: +ELLIPSIS
    (178, 178, 178)
    """
    if not -255.0 <= level <= 255.0:
        raise ValueError("level must be between -255.0 (black) and 255.0 (white)")

    def adjust_pixel(c: int) -> int:
        """Adjust a single pixel channel value by the brightness level."""
        return max(0, min(255, c + int(level)))

    return img.point(adjust_pixel)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python change_brightness.py <input_image> <output_image> <level>")
        print("  level: brightness adjustment from -255 to 255")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    level = float(sys.argv[3])

    with Image.open(input_path) as img:
        bright_img = change_brightness(img, level)
        bright_img.save(output_path, format="png")
    print(f"Brightness changed by {level} and saved to {output_path}")
