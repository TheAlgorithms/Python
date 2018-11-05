"""
	Peak signal-to-noise ratio - PSNR - https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
    Soruce: https://tutorials.techonical.com/how-to-calculate-psnr-value-of-two-images-using-python/
"""

import math

import cv2
import numpy as np

def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR


def main():

    # Loading images (original image and compressed image)
    original = cv2.imread('original_image.png')
    contrast = cv2.imread('compressed_image.png', 1)

    original2 = cv2.imread('PSNR-example-base.png')
    contrast2 = cv2.imread('PSNR-example-comp-10.jpg', 1)

    # Value expected: 29.73dB
    print("-- First Test --")
    print(f"PSNR value is {psnr(original, contrast)} dB")
    
    # # Value expected: 31.53dB (Wikipedia Example)
    print("\n-- Second Test --")
    print(f"PSNR value is {psnr(original2, contrast2)} dB")


if __name__ == '__main__':
    main()
