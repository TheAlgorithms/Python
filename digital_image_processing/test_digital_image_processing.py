import numpy as np
from cv2 import COLOR_BGR2GRAY, cvtColor, imread
from numpy import array, uint8
from PIL import Image
import pytest

import digital_image_processing
from digital_image_processing import change_contrast as cc, image_data
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

# Sample image path for testing
IMG_PATH = r"C:/Users/USER/Python/digital_image_processing/image_data/lena_small.jpg"


@pytest.fixture
def gray_image():
    img = imread(IMG_PATH)
    gray = cvtColor(img, COLOR_BGR2GRAY)
    return gray


# Test: convert_to_negative()
def test_convert_to_negative():
    img = imread(IMG_PATH)
    negative_img = cn.convert_to_negative(img)
    assert negative_img.any()


# Test: change_contrast()
def test_change_contrast():
    with Image.open(IMG_PATH) as img:
        result_img = cc.change_contrast(img, 110)
        assert isinstance(result_img, Image.Image)


# Test: canny edge detection
def test_canny():
    img = imread(IMG_PATH, 0)
    edges = canny.canny(img)
    assert edges.any()


# Test: Gaussian filter
def test_gaussian_filter(gray_image):
    result = gg.gaussian_filter(gray_image, 5, sigma=0.9)
    assert result.any()


# Test: Convolution filter
def test_convolve_filter(gray_image):
    laplace_kernel = array([[0.25, 0.5, 0.25], [0.5, -3, 0.5], [0.25, 0.5, 0.25]])
    result = conv.img_convolve(gray_image, laplace_kernel).astype(uint8)
    assert result.any()


# Test: Median filter
def test_median_filter(gray_image):
    result = med.median_filter(gray_image, 3)
    assert result.any()


# Test: Sobel filter
def test_sobel_filter(gray_image):
    grad, theta = sob.sobel_filter(gray_image)
    assert grad.any()
    assert theta.any()


# Test: Sepia filter
def test_sepia():
    img = imread(IMG_PATH)
    sepia_img = sp.make_sepia(img, 20)
    assert sepia_img.any()


# Test: Burkes dithering
def test_burkes():
    burkes = bs.Burkes(imread(IMG_PATH, 1), 120)
    burkes.process()
    assert burkes.output_img.any()


# Test: Nearest Neighbour resize
def test_nearest_neighbour():
    nn = rs.NearestNeighbour(imread(IMG_PATH, 1), 400, 200)
    nn.process()
    assert nn.output.any()


# Test: Local Binary Pattern
def test_local_binary_pattern():
    img = imread(IMG_PATH, 0)
    neighbors = lbp.get_neighbors_pixel(img, 0, 0, img[0, 0])
    assert neighbors is not None

    lbp_image = np.zeros((img.shape[0], img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            lbp_image[i][j] = lbp.local_binary_value(img, i, j)

    assert lbp_image.any()
