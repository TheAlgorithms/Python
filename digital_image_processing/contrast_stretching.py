import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey


def contrast_stretching(
    img: np.ndarray,
    coordinate_x1: int,
    coordinate_y1: int,
    coordinate_x2: int,
    coordinate_y2: int,
) -> np.ndarray:
    """
    Returns the numpy array of contrast stretched image.
    """

    # getting number of pixels in the image
    pixel_h, pixel_v = img.shape[0], img.shape[1]

    # making an empty numpy array which will store the contrast stretched image
    img_contrast = np.zeros((pixel_h, pixel_v), dtype=int)

    # threshold values
    A = 150
    B = 250

    # applying the contrast stretching logic on each pixel of the image
    for i in range(pixel_h):
        for j in range(pixel_v):
            if 0 <= img[i, j] < A:
                img_contrast[i, j] = int(coordinate_y1 / coordinate_x1) * img[i, j]
            elif A <= img[i, j] < B:
                img_contrast[i, j] = (
                    int(coordinate_y2 - coordinate_y1 / coordinate_x2 - coordinate_x1)
                    * (img[i, j] - coordinate_x1)
                    + coordinate_y1
                )
            else:
                img_contrast[i, j] = (
                    int(255 - coordinate_y2 / 255 - coordinate_x2)
                    * (img[i, j] - coordinate_x2)
                    + coordinate_y2
                )

    return img_contrast


if __name__ == "__main__":

    # Taking pair of coordinates as input to apply contrast stretching
    a, v = map(int, input("Enter the pair a, v: ").split())
    b, w = map(int, input("Enter the pair b, w: ").split())

    # read original image
    img = imread("digital_image_processing/image_data/lena.jpg", 0)

    # apply contrast stretching on the image
    contrast_stretched_img = contrast_stretching(img, a, v, b, w)

    # show result image
    imshow("contrast stretched image", img)
    waitKey(0)
    destroyAllWindows()
