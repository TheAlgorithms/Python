"""
    Implemented an algorithm using opencv to tone an image with sepia technic
"""

from cv2 import imread, imshow, waitKey, destroyAllWindows


def make_sepia(img, factor: int):
    """ Function create sepia tone. Source: https://en.wikipedia.org/wiki/Sepia_(color) """
    pixel_h, pixel_v = img.shape[0], img.shape[1]

    def to_grayscale(blue, green, red):
        """
        Helper function to create pixel's greyscale representation
        Src: https://pl.wikipedia.org/wiki/YUV
        """
        return 0.2126 * red + 0.587 * green + 0.114 * blue

    def normalize(value):
        """ Helper function to normalize R/G/B value -> return 255 if value > 255"""
        return value if value <= 255 else 255

    for i in range(pixel_h):
        for j in range(pixel_v):
            greyscale = int(to_grayscale(*img[i][j]))
            img[i][j] = [
                normalize(greyscale),
                normalize(greyscale + factor),
                normalize(greyscale + 2 * factor),
            ]

    return img


if __name__ == "__main__":
    # read original image
    img = imread("image_data/lena.jpg", 1)
    img1 = imread("image_data/lena.jpg", 1)
    img2 = imread("image_data/lena.jpg", 1)
    img3 = imread("image_data/lena.jpg", 1)

    # convert with sepia with different factor's value
    sepia_10 = make_sepia(img, 10)
    sepia_20 = make_sepia(img1, 20)
    sepia_30 = make_sepia(img2, 30)
    sepia_40 = make_sepia(img3, 40)

    # show result images
    imshow("Original image with sepia (factor: 10)", img)
    imshow("Original image with sepia (factor: 20)", img1)
    imshow("Original image with sepia (factor: 30)", img2)
    imshow("Original image with sepia (factor: 40)", img3)
    waitKey(0)
    destroyAllWindows()
