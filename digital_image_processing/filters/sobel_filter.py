# @Author  : lightXu
# @File    : sobel_filter.py
# @Time    : 2019/7/8 0008 下午 16:26
import numpy as np
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey
from digital_image_processing.filters.convolve import img_convolve


def sobel_filter(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    dst_x = img_convolve(image, kernel_x)
    dst_y = img_convolve(image, kernel_y)
    dst = np.sqrt((np.square(dst_x)) + (np.square(dst_y))).astype(np.uint8)
    degree = np.arctan2(dst_y, dst_x)
    return dst, degree


if __name__ == '__main__':
    # read original image
    img = imread('../image_data/lena.jpg')
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    sobel, d = sobel_filter(gray)

    # show result images
    imshow('sobel filter', sobel)
    imshow('sobel degree', d)
    waitKey(0)
