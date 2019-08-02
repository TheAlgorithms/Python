"""
Implementation of image convolve algorithm
"""
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey
from numpy import array, zeros, ravel, pad, dot, uint8
import math


def im2col(image, block_size, row_stride, col_stride, dst_rows, dst_cols):
    """
    :param image: padded image array
    :param block_size: filter shape tuple
    :param row_stride: stride in row channels
    :param col_stride: stride in row channels
    :param dst_rows: the rows of the filtered input image
    :param dst_cols: the cols of the filtered input image
    :return: the reshape array with shape(dst_rows*dst_cols， block_size[1] * block_size[0])
    """

    image_array = zeros((dst_rows * dst_cols, block_size[1] * block_size[0]))
    row = 0
    for i in range(0, dst_rows):
        for j in range(0, dst_cols):
            window = ravel(image[i * row_stride:i * row_stride + block_size[0],
                           j * col_stride:j * col_stride + block_size[1]])
            image_array[row, :] = window
            row += 1

    return image_array


def img_convolve(image, kernel, row_stride=1, col_stride=1):
    """
    :param image:  input image array
    :param kernel: filter kernel array
    :param mode: padding mode, and 'edge' Pads with the edge values of array.
    :param row_stride: stride in row channels
    :param col_stride: stride in row channels
    :return: the filter result

    Example:
    >>> image = array([[1,2,3,4,5],[2,3,4,5,6], [1,2,3,4,5]])
    >>> kernel = array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    >>> img_convolve(image, kernel, 1, 1)
    array([[3., 6., 6., 6., 3.],
           [3., 6., 6., 6., 3.],
           [3., 6., 6., 6., 3.]])

    >>> img_convolve(image, kernel, 2, 1)
    array([[3., 6., 6., 6., 3.],
           [3., 6., 6., 6., 3.]])

    >>> img_convolve(image, kernel, 2, 2)
    array([[3., 6., 3.],
           [3., 6., 3.]])

    >>> kernel_1_3 = array([[-1, 2, -1]])
    >>> img_convolve(image, kernel_1_3, 1, 1)
    array([[-1.,  0.,  0.,  0.,  1.],
           [-1.,  0.,  0.,  0.,  1.],
           [-1.,  0.,  0.,  0.,  1.]])

    >>> kernel_3_1 = array([[-2], [1], [-2]])
    >>> img_convolve(image, kernel_3_1, 1, 1)
    array([[ -5.,  -8., -11., -14., -17.],
           [ -2.,  -5.,  -8., -11., -14.],
           [ -5.,  -8., -11., -14., -17.]])

    >>> kernel_3_1 = array([[-2], [1], [-2]])
    >>> img_convolve(image, kernel_3_1, 2, 1)
    array([[ -5.,  -8., -11., -14., -17.],
           [ -5.,  -8., -11., -14., -17.]])


    >>> kernel_3_1 = array([[-2], [1], [-2]])
    >>> img_convolve(image, kernel_3_1, 2, 2)
    array([[ -5., -11., -17.],
           [ -5., -11., -17.]])
    """

    height, width = image.shape[0], image.shape[1]
    k_size_row, k_size_col = kernel.shape[0], kernel.shape[1]

    # "SAME" convolve mode
    dst_rows = math.ceil(height / row_stride)  # ceil
    dst_cols = math.ceil(width / col_stride)  # ceil

    pad_h = max((dst_rows - 1) * row_stride + k_size_row - height, 0)
    pad_top = pad_h // 2  # floor
    pad_bottom = pad_h - pad_top
    pad_w = max((dst_cols - 1) * col_stride + k_size_col - width, 0)
    pad_left = pad_w // 2  # floor
    pad_right = pad_w - pad_left

    # Pads image with the edge values of array.
    image_tmp = pad(array=image,
                    pad_width=((pad_top, pad_bottom), (pad_left, pad_right)),
                    mode='edge')

    image_array = im2col(image_tmp, (k_size_row, k_size_col), row_stride, col_stride, dst_rows, dst_cols)
    kernel_array = ravel(kernel)
    dst = dot(image_array, kernel_array).reshape(dst_rows, dst_cols)
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
