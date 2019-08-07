"""
PyTest's for Digital Image Processing
"""

# add change_contrast
from PIL import Image
import digital_image_processing.change_contrast as cc
# add canny
import digital_image_processing.edge_detection.canny as canny
import cv2
# add gen_gaussian
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey
from numpy import array, pi, mgrid, exp, square, zeros, ravel, dot, uint8
import digital_image_processing.filters.gaussian_filter as gg
# add convolve
import digital_image_processing.filters.convolve as conv
# add median
import digital_image_processing.filters.median_filter as med
# add sobel_filter
import digital_image_processing.filters.sobel_filter as sob
# add img
img = imread(r'digital_image_processing/image_data/lena.jpg')
# add gray
gray = cvtColor(img, COLOR_BGR2GRAY)

# Test: change_contrast()
def test_change_contrast():
    # Image object
    with Image.open("digital_image_processing/image_data/lena.jpg") as img:
        # Work around assertion for response
        assert str(cc.change_contrast(img, 110)).startswith('<PIL.Image.Image image mode=RGB size=512x512 at')

# Test: canny.gen_gaussian_kernel()
def test_gen_gaussian_kernel():
    # get ambiguous array
    resp = canny.gen_gaussian_kernel(9, sigma=1.4)
    # Assert ambiguous array
    assert resp.all()

# Test: canny()
def test_canny():
    # read image in gray
    canny_img = imread('digital_image_processing/image_data/lena.jpg', 0)
    # assert ambiguos array for all == True
    assert canny_img.all()
    # Get canny array
    canny_array = canny.canny(canny_img)
    # assert canny array for at least one True
    assert canny_array.any()

# Test: filters/gaussian_filter.py
def test_gen_gaussian_kernel_filter():
    # Filter 5x5
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