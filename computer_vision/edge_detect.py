"""
[Vikas Ukani]
(Edge Detection Object)
https://github.com/vikas-ukani/
"""


def detect (image_name):    
    # Import Necessary Packages
    import sys # system important
    import cv2 # computer visualization
    import numpy as np # multi-dimensional array # linear algebra

    # Get arguments from command line.
    image_name = sys.argv[1] # take an argument from command line

    # Load Image and Convert into Gray
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE) # read image with gray scal image
    height, weight = image.shape # Extract from image shape to height and weight

    # Make sobel for better customization.
    sobel_horizontal = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_vertical = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    canny = cv2.Canny(image, 50, 240) 

    # show all images MODELS here.
    cv2.imshow("Original", image) # Show in Original Video Form
    cv2.imshow("Sobel Horizontal", sobel_horizontal) # Sobel orizantal Mode
    cv2.imshow("Sobel Vertical", sobel_vertical) #  Sobel Vertical Mode
    cv2.imshow("Laplacian", laplacian) # Show in Laplcian Model
    cv2.imshow("Canny", canny) # Show in Cannery Mode 

    # Wait for EXIT ...
    cv2.waitKey() # Any key press to exit from video mode.


if __name__ == "__main__":
    detect("img_path_from_current_dir")

