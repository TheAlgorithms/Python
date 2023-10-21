import math
import os

import numpy as np

PIXEL_MAX = 255.0


def peak_signal_to_noise_ratio(original: np.ndarray, contrast: np.ndarray) -> float:
    """
    Calculate peak signal to noise ratio (PSNR) between two images.
    >>> import numpy as np
    >>> a = np.array([[0, 0], [255, 255]])
    >>> b = np.array([[0, 0], [255, 255]])
    >>> peak_signal_to_noise_ratio(a, b)
    inf
    >>> c = np.array([[0, 0], [254, 254]])
    >>> round(peak_signal_to_noise_ratio(a, c), 2)
    48.13
    """
    mse = np.mean((original - contrast) ** 2)

    if mse == 0:
        return 100

    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def read_image(image_path: str) -> np.ndarray:
    """Read image from file."""
    with open(image_path, "rb") as f:
        height = int.from_bytes(f.read(2), byteorder="big")
        width = int.from_bytes(f.read(2), byteorder="big")
        image = np.empty((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                b = f.read(1)[0]
                g = f.read(1)[0]
                r = f.read(1)[0]
                image[i, j] = [r, g, b]
    return image


def main():
    """Main function."""
    dir_path = os.path.dirname(os.path.realpath(__file__))

    original = read_image(os.path.join(dir_path, "image_data/original_image.png"))
    contrast = read_image(os.path.join(dir_path, "image_data/compressed_image.png"))

    original2 = read_image(os.path.join(dir_path, "image_data/PSNR-example-base.png"))
    contrast2 = read_image(
        os.path.join(dir_path, "image_data/PSNR-example-comp-10.jpg")
    )

    print("-- First Test --")
    print(f"PSNR value is {peak_signal_to_noise_ratio(original, contrast)} dB")

    print("\n-- Second Test --")
    print(f"PSNR value is {peak_signal_to_noise_ratio(original2, contrast2)} dB")


if __name__ == "__main__":
    main()
