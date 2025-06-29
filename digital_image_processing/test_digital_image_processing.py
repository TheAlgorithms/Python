"""
PyTest's for Digital Image Processing
"""

import os

import numpy as np
from cv2 import COLOR_BGR2GRAY, cvtColor, imread
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

img = imread(r"digital_image_processing/image_data/lena_small.jpg")
gray = cvtColor(img, COLOR_BGR2GRAY)


def test_convert_to_negative():
    """Test negative image conversion."""
    negative_img = cn.convert_to_negative(img)
    # Verify output contains at least one non-zero value
    assert negative_img.any()


def test_change_contrast():
    """Test contrast adjustment functionality."""
    with Image.open("digital_image_processing/image_data/lena_small.jpg") as img_pil:
        # Verify returns a PIL Image object
        assert str(cc.change_contrast(img_pil, 110)).startswith(
            "<PIL.Image.Image image mode=RGB size=100x100 at"
        )


def test_gen_gaussian_kernel():
    """Test Gaussian kernel generation."""
    kernel = canny.gen_gaussian_kernel(9, sigma=1.4)
    # Verify kernel contains valid values
    assert kernel.all()


def test_canny():
    """Test Canny edge detection."""
    canny_img = imread("digital_image_processing/image_data/lena_small.jpg", 0)
    assert canny_img.all()  # Verify input image loaded correctly
    edges = canny.canny(canny_img)
    assert edges.any()  # Verify edge detection produced output


def test_gen_gaussian_kernel_filter():
    """Test Gaussian filter application."""
    assert gg.gaussian_filter(gray, 5, sigma=0.9).all()


def test_convolve_filter():
    """Test image convolution operation."""
    # Laplace kernel for edge detection
    laplace = array([[0.25, 0.5, 0.25], [0.5, -3, 0.5], [0.25, 0.5, 0.25]])
    result = conv.img_convolve(gray, laplace).astype(uint8)
    assert result.any()  # Verify convolution output


def test_median_filter():
    """Test median noise reduction filter."""
    assert med.median_filter(gray, 3).any()


def test_sobel_filter():
    """Test Sobel edge detection."""
    gradient, direction = sob.sobel_filter(gray)
    assert gradient.any()  # Verify gradient magnitude
    assert direction.any()  # Verify gradient direction


def test_sepia():
    """Test sepia tone filter."""
    sepia_img = sp.make_sepia(img, 20)
    assert sepia_img.all()


def test_burkes():
    """Test Burkes dithering algorithm."""
    burkes = bs.Burkes(
        imread("digital_image_processing/image_data/lena_small.jpg", 1), 120
    )
    burkes.process()
    assert burkes.output_img.any()


def test_nearest_neighbour():
    """Test nearest-neighbor resizing."""
    nn = rs.NearestNeighbour(
        imread("digital_image_processing/image_data/lena_small.jpg", 1), 400, 200
    )
    nn.process()
    assert nn.output.any()


def test_local_binary_pattern():
    """Test Local Binary Pattern feature extraction."""
    # Use smaller image in CI environments for faster tests
    file_name = "lena_small.jpg" if os.getenv("CI") else "lena.jpg"
    file_path = f"digital_image_processing/image_data/{file_name}"

    # Load image in grayscale
    image = imread(file_path, 0)

    # Test neighbor pixel collection
    center = image[0][0]
    neighbors = lbp.get_neighbors_pixel(image, 0, 0, center)
    assert neighbors is not None

    # Test LBP feature map generation
    lbp_image = np.zeros_like(image, dtype=np.float32)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            lbp_image[i][j] = lbp.local_binary_value(image, i, j)
    assert lbp_image.any()
