"""
PyTest's for Digital Image Processing
"""
# Test: change_contrast()
def test_change_contrast():
    from PIL import Image
    import digital_image_processing.change_contrast as cc
    # Image object
    with Image.open("digital_image_processing/image_data/lena.jpg") as img:
        # Work around assertion for response
        assert str(cc.change_contrast(img, 110)).startswith('<PIL.Image.Image image mode=RGB size=512x512 at')

# Test: canny.gen_gaussian_kernel()
def test_gen_gaussian_kernel():
    # import canny
    import digital_image_processing.edge_detection.canny as cc
    # get ambiguous array
    resp = cc.gen_gaussian_kernel(9, sigma=1.4)
    # Assert ambiguous array
    assert resp.all()

# Test: canny()
def test_canny():
    # import reqs
    import cv2
    import digital_image_processing.edge_detection.canny as cc
    # read image in gray
    img = cv2.imread('digital_image_processing/image_data/lena.jpg', 0)
    # assert ambiguos array for all == True
    assert img.all()
    # Get canny array
    canny_array = cc.canny(img)
    # assert canny array for at least one True
    assert canny_array.any()

"""
# Test: filters/gaussian_filter.py
def gen_gaussian_kernel_filter():
    # imports
    from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey
    from numpy import pi, mgrid, exp, square, zeros, ravel, dot, uint8
    # import gaussian filter file
    import digital_image_processing.filters.gen_gaussian_kernel as gg 
    
"""
