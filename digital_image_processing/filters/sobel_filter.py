# @Author  : lightXu
# @File    : sobel_filter.py
# @Time    : 2019/7/8 0008 下午 16:26
import numpy as np
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey
from digital_image_processing.filters.convolve import img_convolve


def sobel_filter(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    dst_x = np.abs(img_convolve(image, kernel_x))
    dst_y = np.abs(img_convolve(image, kernel_y))
    # modify the pix within [0, 255]
    dst_x = dst_x * 255/np.max(dst_x)
    dst_y = dst_y * 255/np.max(dst_y)

    dst_xy = np.sqrt((np.square(dst_x)) + (np.square(dst_y)))
    dst_xy = dst_xy * 255/np.max(dst_xy)
    dst = dst_xy.astype(np.uint8)

    theta = np.arctan2(dst_y, dst_x)
    return dst, theta


if __name__ == '__main__':
    # read original image
    img = imread('../image_data/lena.jpg')
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    sobel_grad, sobel_theta = sobel_filter(gray)

    # show result images
    imshow('sobel filter', sobel_grad)
    imshow('sobel theta', sobel_theta)
    waitKey(0)
