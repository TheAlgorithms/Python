"""
PyTest's for Digital Image Processing
"""

import digital_image_processing.edge_detection.canny as canny
import digital_image_processing.filters.gaussian_filter as gg
import digital_image_processing.filters.median_filter as med
import digital_image_processing.filters.sobel_filter as sob
import digital_image_processing.filters.convolve as conv
import digital_image_processing.change_contrast as cc
from cv2 import imread, cvtColor, COLOR_BGR2GRAY
from numpy import array, uint8
from PIL import Image

img = imread(r"digital_image_processing/image_data/lena_small.jpg")
gray = cvtColor(img, COLOR_BGR2GRAY)

# Test: change_contrast()
def test_change_contrast():
    with Image.open("digital_image_processing/image_data/lena_small.jpg") as img:
        # Work around assertion for response
        assert str(cc.change_contrast(img, 110)).startswith(
            "<PIL.Image.Image image mode=RGB size=100x100 at"
        )


# canny.gen_gaussian_kernel()
def test_gen_gaussian_kernel():
    resp = canny.gen_gaussian_kernel(9, sigma=1.4)
    # Assert ambiguous array
    assert resp.all()


# canny.py
def test_canny():
    canny_img = imread("digital_image_processing/image_data/lena_small.jpg", 0)
    # assert ambiguos array for all == True
    assert canny_img.all()
    canny_array = canny.canny(canny_img)
    # assert canny array for at least one True
    assert canny_array.any()


# filters/gaussian_filter.py
def test_gen_gaussian_kernel_filter():
    assert gg.gaussian_filter(gray, 5, sigma=0.9).all()


def test_convolve_filter():
    # laplace diagonals
    Laplace = array([[0.25, 0.5, 0.25], [0.5, -3, 0.5], [0.25, 0.5, 0.25]])
    res = conv.img_convolve(gray, Laplace).astype(uint8)
    assert res.any()


def test_median_filter():
    assert med.median_filter(gray, 3).any()


def test_sobel_filter():
    grad, theta = sob.sobel_filter(gray)
    assert grad.any() and theta.any()
