"""
PyTest's for Digital Image Processing
"""
# Test: change_contrast()
def test_change_contrast():
    from PIL import Image
    import digital_image_processing.change_contrast as cc
    # Image object
    with Image.open("image_data/lena.jpg") as img:
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
