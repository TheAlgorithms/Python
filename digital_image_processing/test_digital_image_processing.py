from PIL import Image
import digital_image_processing.change_contrast as cc

# Test: change_contrast()
def test_change_contrast():
    with Image.open("image_data/lena.jpg") as img:
        assert str(cc.change_contrast(img, 110)).startswith('<PIL.Image.Image image mode=RGB size=512x512 at')