"""
PyTest's for Digital Image Processing
"""

import numpy as np
from cv2 import COLOR_BGR2GRAY, cvtColor, imread
from numpy import array, uint8
from os import getenv
from PIL import Image

from digital_image_processing import change_contrast as cc
from digital_image_processing import convert_to_negative as cn
from digital_image_processing import sepia as sp
from digital_image_processing.dithering import burkes as bs
from digital_image_processing.edge_detection import canny
from digital_image_processing.filters import convolve as conv
from digital_image_processing.filters import gaussian_filter as gg
from digital_image_processing.filters import local_binary_pattern as lbp
from digital_image_processing.filters import median_filter as med
from digital_image_processing.filters import sobel_filter as sob
from digital_image_processing.resize import resize as rs

# Define common image paths
LENA_SMALL_PATH = "digital_image_processing/image_data/lena_small.jpg"
LENA_PATH = "digital_image_processing/image_data/lena.jpg"

img = imread(LENA_SMALL_PATH)
gray = cvtColor(img, COLOR_BGR2GRAY)


# Test: convert_to_negative()
def test_convert_to_negative():
    negative_img = cn.convert_to_negative(img)
    assert negative_img.any()


# Test: change_contrast()
def test_change_contrast():
    with Image.open(LENA_SMALL_PATH) as img:
        assert str(cc.change_contrast(img, 110)).startswith(
            "<PIL.Image.Image image mode=RGB size=100x100 at"
        )


# canny.gen_gaussian_kernel()
def test_gen_gaussian_kernel():
    resp = canny.gen_gaussian_kernel(9, sigma=1.4)
    assert resp.all()


# canny.py
def test_canny():
    canny_img = imread(LENA_SMALL_PATH, 0)
    assert canny_img.all()
    canny_array = canny.canny(canny_img)
    assert canny_array.any()


# filters/gaussian_filter.py
def test_gen_gaussian_kernel_filter():
    assert gg.gaussian_filter(gray, 5, sigma=0.9).all()


def test_convolve_filter():
    # laplace diagonals
    laplace = array([[0.25, 0.5, 0.25], [0.5, -3, 0.5], [0.25, 0.5, 0.25]])
    res = conv.img_convolve(gray, laplace).astype(uint8)
    assert res.any()


def test_median_filter():
    assert med.median_filter(gray, 3).any()


def test_sobel_filter():
    grad, theta = sob.sobel_filter(gray)
    assert grad.any()
    assert theta.any()


def test_sepia():
    sepia = sp.make_sepia(img, 20)
    assert sepia.all()


def test_burkes():
    burkes_img = bs.Burkes(imread(LENA_SMALL_PATH, 1), 120)
    burkes_img.process()
    assert burkes_img.output_img.any()


def test_nearest_neighbour():
    nn_img = rs.NearestNeighbour(imread(LENA_SMALL_PATH, 1), 400, 200)
    nn_img.process()
    assert nn_img.output.any()


def test_local_binary_pattern():
    # Use smaller image in CI environment for faster tests
    file_path = LENA_SMALL_PATH if getenv("CI") else LENA_PATH
    image = imread(file_path, 0)

    # Test get_neighbors_pixel function
    neighbors_pixels = lbp.get_neighbors_pixel(image, 0, 0, image[0][0])
    assert neighbors_pixels is not None

    # Test local_binary_pattern function
    lbp_image = np.zeros((image.shape[0], image.shape[1]))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            lbp_image[i][j] = lbp.local_binary_value(image, i, j)
    assert lbp_image.any()
