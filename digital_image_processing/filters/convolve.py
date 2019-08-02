# @Author  : lightXu
# @File    : convolve.py
# @Time    : 2019/7/8 0008 下午 16:13
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey
from numpy import array, zeros, ravel, pad, dot, uint8
import math


def im2col(image, block_size, row_stride, col_stride, dst_rows, dst_cols):

    image_array = zeros((dst_rows * dst_cols, block_size[1] * block_size[0]))
    row = 0
    for i in range(0, dst_rows, row_stride):
        for j in range(0, dst_cols, col_stride):
            window = ravel(image[i:i + block_size[0], j:j + block_size[1]])
            image_array[row, :] = window
            row += 1

    return image_array


def img_convolve(image, kernel, mode='edge', row_stride=1, col_stride=1):
    height, width = image.shape[0], image.shape[1]
    k_size_row, k_size_col = kernel.shape[0], kernel.shape[1]

    # "SAME" convolve mode
    dst_rows = math.ceil(height/row_stride)  # ceil
    dst_cols = math.ceil(width/col_stride)  # ceil

    pad_h = max((dst_rows - 1) * row_stride + k_size_row - height, 0)
    pad_top = pad_h // 2  # floor
    pad_bottom = pad_h - pad_top
    pad_w = max((dst_cols - 1) * col_stride + k_size_col - width, 0)
    pad_left = pad_w // 2  # floor
    pad_right = pad_w - pad_left

    # Pads image with the edge values of array.
    image_tmp = pad(array=image,
                    pad_width=((pad_top, pad_bottom), (pad_left, pad_right)),
                    mode=mode)

    image_array = im2col(image_tmp, (k_size_row, k_size_col), row_stride, col_stride, dst_rows, dst_cols)
    kernel_array = ravel(kernel)
    dst = dot(image_array, kernel_array).reshape(height, width)
    return dst


if __name__ == '__main__':
    # read original image
    img = imread(r'../image_data/lena.jpg')
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)
    # Laplace operator
    Laplace_kernel = array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    out = img_convolve(gray, Laplace_kernel).astype(uint8)
    imshow('Laplacian', out)
    waitKey(0)
