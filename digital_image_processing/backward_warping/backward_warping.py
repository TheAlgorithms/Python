import cv2
import numpy as np


def backward_warping(matrix: np.ndarray, img: np.ndarray) -> np.ndarray:
    """
    Get backward_warping image
    :param matrix: 3x3 list
    :param img: np.array
    :return: np.array

    Example
    M2 is a translation matrix
    points are moved at points*1.5
    img[50][50] -> result img[75][75]
    img[50][50] : 171
    -------
    >>> trans = np.array([[1.5, 0, 0],
    ...                 [0, 1.5, 0],
    ...                 [0, 0, 1]])
    >>> image = cv2.imread('image_data/lena.jpg', cv2.IMREAD_GRAYSCALE)
    >>> result = backward_warping(trans, image)
    >>> result[75][75]
    171
    """
    src_h, src_w = img.shape
    y_scale = matrix[1, 1]
    x_scale = matrix[0, 0]

    # result image resizing
    dst_h = max(int(src_h * y_scale + 0.5), src_h)
    dst_w = max(int(src_w * x_scale + 0.5), src_w)
    dst = np.zeros((dst_h, dst_w), img.dtype)

    # inverse matrix
    inv_m = np.linalg.inv(matrix)

    for y in range(dst_h):
        for x in range(dst_w):
            # applying inverse matrix to x, y points
            temp = inv_m @ np.array([x, y, 1])
            # each point is a point applying inverse matrix
            x_ = temp[0]
            y_ = temp[1]

            # original image's points would be decimal points
            # using bilinear interpolation

            # a real point of x that left avobe estimated point
            px = int(x_)
            # prevent overflow
            if px >= src_w - 1:
                px = src_w - 2
            if px < 0:
                px = 0
            # a real point of y that left avobe estimated point
            py = int(y_)
            # prevent overflow
            if py >= src_h - 1:
                py = src_h - 2
            if py < 0:
                py = 0

            # a distance between left real point and estimated point x
            fx1 = x_ - px
            # a distance between right real point and estimated point x
            fx2 = 1 - fx1
            # a distance between left real point and estimated point y
            fy1 = y_ - py
            # a distance between right real point and estimated point y
            fy2 = 1 - fy1

            # each area of 4 rectangles
            # the ractangles are based on estimated points
            w1 = fx2 * fy2
            w2 = fx1 * fy2
            w3 = fx2 * fy1
            w4 = fx1 * fy1

            # 4 points around estimated points
            # each p1,2,3,4 is symmetric to rectangle w1,2,3,4
            p1 = img[py, px]
            p2 = img[py, px + 1]
            p3 = img[py + 1, px]
            p4 = img[py + 1, px + 1]

            # a case that points are on real image size
            if 0 <= x_ < src_w - 1 and 0 <= y_ < src_h - 1:
                # sum of symmetric point's value * rectangle's area
                dst[y, x] = w1 * p1 + w2 * p2 + w3 * p3 + w4 * p4
            # a case that points are not on real image size
            else:
                dst[y, x] = 0

    return dst


if __name__ == "__main__":
    img = cv2.imread("image_data/lena.jpg", cv2.IMREAD_GRAYSCALE)
    angle = np.deg2rad(15)
    M1 = np.array([[1, 0, 50], [0, 1, 100], [0, 0, 1]])

    M2 = np.array([[1.5, 0, 0], [0, 1.5, 0], [0, 0, 1]])

    M3 = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )

    M4 = np.array([[1, 0.2, 0], [0.2, 1, 0], [0, 0, 1]])

    dst1 = backward_warping(M1, img)
    dst2 = backward_warping(M2, img)
    dst3 = backward_warping(M3, img)
    dst4 = backward_warping(M4, img)

    cv2.imshow("original", img)
    cv2.imshow("translation", dst1)
    cv2.imshow("scaling", dst2)
    cv2.imshow("rotation", dst3)
    cv2.imshow("shear", dst4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
