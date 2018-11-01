"""
	Peak signal-to-noise ratio - PSNR - https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
	1º Method: https://tutorials.techonical.com/how-to-calculate-psnr-value-of-two-images-using-python/
	2º Method: Incorrect ????
"""

import math

import cv2
import numpy as np

# This method is the really work as expected, but however I want to preserve the other method (psnr2) 
def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR


def Representational(r, g, b):
    # Formula to determine brightness of RGB color
    return (0.299*r+0.287*g+0.114*b)


def calculate(img):
    b, g, r = cv2.split(img)
    return Representational(r, g, b)

# The 1º Method really works better 
def psnr2(original, contrast):
    # Getting image height and width
    height, width = original.shape[:2]

    # Calculate the RGB Proportion for each Image and get the difference.
    originalPixelAt = calculate(original)
    compressedPixelAt = calculate(contrast)

    diff = originalPixelAt - compressedPixelAt

    # Calculate the error
    error = np.sum(np.abs(diff) ** 2) / (height * width)

    # MSR = error_sum/(height*width)
    PSNR = -(10*math.log10(error/(255*255)))
    return format(PSNR)


def main():

    # Loading images (original image and compressed image)
    original = cv2.imread('original_image.png')
    contrast = cv2.imread('compressed_image.png', 1)

    original2 = cv2.imread('PSNR-example-base.png')
    contrast2 = cv2.imread('PSNR-example-comp-10.jpg', 1)

    # Value expected: 29.73dB
    print("-- First Test --")
    print(f"1º Method: \n PSNR value is {psnr(original, contrast)} dB")
    print(f"2º Method: \n PSNR value is {psnr2(original, contrast)} dB \n")
    
    # # Value expected: 31.53dB (Wikipedia Example)
    print("-- Second Test --")
    print(f"1º Method: \n PSNR value is {psnr(original2, contrast2)} dB")
    print(f"2º Method: \n PSNR value is {psnr2(original2, contrast2)} dB")


if __name__ == '__main__':
    main()
