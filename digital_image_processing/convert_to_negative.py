"""
    Implemented an algorithm using opencv to convert a colored image into its negative
"""
from cv2 import destroyAllWindows, imread, imshow, waitKey


def convert_to_negative(img):
    # getting number of pixels in the image
    pixel_h, pixel_v = img.shape[0], img.shape[1]

    # converting each pixel's color to its negative
    for i in range(pixel_h):
        for j in range(pixel_v):
            img[i][j] = [255, 255, 255] - img[i][j]

    return img


if __name__ == "__main__":
    # read original image
    img = imread("image_data/lena.jpg", 1)

    # convert to its negative
    neg = convert_to_negative(img)

    # show result image
    imshow("negative of original image", img)
    waitKey(0)
    destroyAllWindows()
