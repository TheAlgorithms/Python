"""
Peak signal-to-noise ratio - PSNR
    https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
Source:
https://tutorials.techonical.com/how-to-calculate-psnr-value-of-two-images-using-python
"""

import math
import os

PIXEL_MAX = 255.0


def peak_signal_to_noise_ratio(original, contrast):
    mse = 0
    height, width, _ = original.shape
    for i in range(height):
        for j in range(width):
            for k in range(3):
                mse += (original[i, j, k] - contrast[i, j, k]) ** 2
    mse /= height * width * 3

    if mse == 0:
        return 100

    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def read_image(image_path):
    with open(image_path, "rb") as f:
        height = int.from_bytes(f.read(2), byteorder="big")
        width = int.from_bytes(f.read(2), byteorder="big")
        image = []
        for _i in range(height):
            row = []
            for _j in range(width):
                b = f.read(1)[0]
                g = f.read(1)[0]
                r = f.read(1)[0]
                row.append([r, g, b])
            image.append(row)
    return image


def main():
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
