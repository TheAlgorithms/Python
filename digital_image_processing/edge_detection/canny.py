import cv2
import numpy as np

# from digital_image_processing.filters.convolve import img_convolve
# from digital_image_processing.filters.sobel_filter import sobel_filter

from numpy import dot, pad, ravel, zeros

PI = 180

def sobel_filter(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    dst_x = np.abs(img_convolve(image, kernel_x))
    dst_y = np.abs(img_convolve(image, kernel_y))
    # modify the pix within [0, 255]
    dst_x = dst_x * 255 / np.max(dst_x)
    dst_y = dst_y * 255 / np.max(dst_y)

    dst_xy = np.sqrt((np.square(dst_x)) + (np.square(dst_y)))
    dst_xy = dst_xy * 255 / np.max(dst_xy)
    dst = dst_xy.astype(np.uint8)

    theta = np.arctan2(dst_y, dst_x)
    return dst, theta

def im2col(image, block_size):
    rows, cols = image.shape
    dst_height = cols - block_size[1] + 1
    dst_width = rows - block_size[0] + 1
    image_array = zeros((dst_height * dst_width, block_size[1] * block_size[0]))
    row = 0
    for i in range(0, dst_height):
        for j in range(0, dst_width):
            window = ravel(image[i : i + block_size[0], j : j + block_size[1]])
            image_array[row, :] = window
            row += 1

    return image_array

def img_convolve(image, filter_kernel):
    height, width = image.shape[0], image.shape[1]
    k_size = filter_kernel.shape[0]
    pad_size = k_size // 2
    # Pads image with the edge values of array.
    image_tmp = pad(image, pad_size, mode="edge")

    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = im2col(image_tmp, (k_size, k_size))

    #  turn the kernel into shape(k*k, 1)
    kernel_array = ravel(filter_kernel)
    # reshape and get the dst image
    dst = dot(image_array, kernel_array).reshape(height, width)
    return dst



def gen_gaussian_kernel(k_size, sigma):
    center = k_size // 2
    x, y = np.mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = (
        1
        / (2 * np.pi * sigma)
        * np.exp(-(np.square(x) + np.square(y)) / (2 * np.square(sigma)))
    )
    return g

def non_maximum_suppression(image, grad_dir, grad_mag, strong, weak, low, high): 
    """
    Non-maximum suppression. If the edge strength of the current pixel is the largest
    compared to the other pixels in the mask with the same direction, the value will be
    preserved. Otherwise, the value will be suppressed.
    """
    image_row, image_col = image.shape
    for row in range(1, image_row - 1):
        for col in range(1, image_col - 1):
            direction = grad_dir[row, col]
            angle_case1(direction, grad_mag, image, row, col)
            angle_case2(direction, grad_mag, image, row, col)
            angle_case3(direction, grad_mag, image, row, col)
            angle_case4(direction, grad_mag, image, row, col)
            threshold(image, row, col, high, low, strong, weak)

def angle_case1(dir, grad_mag, image, row, col):
    """
    Suppress the non-maximum value horizontally.
    Args:
        dir: gradient direction
        grad_mag: map of gradient magnitude
        image: edge map
        row: first dimension coordinate of image
        col: second dimension coordinate of image
    """
    if (
        0 <= dir < 22.5
        or 15 * PI / 8 <= dir <= 2 * PI
        or 7 * PI / 8 <= dir <= 9 * PI / 8
    ):
        w = grad_mag[row, col - 1]
        e = grad_mag[row, col + 1]
        if grad_mag[row, col] >= w and grad_mag[row, col] >= e:
            image[row, col] = grad_mag[row, col]
            
def angle_case2(dir, grad_mag, image, row, col):
    """
    Suppress the non-maximum value subdiagonally.
    Args:
        dir: gradient direction
        grad_mag: map of gradient magnitude
        image: edge map
        row: first dimension coordinate of image
        col: second dimension coordinate of image
    """
    if (PI / 8 <= dir < 3 * PI / 8) or (
        9 * PI / 8 <= dir < 11 * PI / 8
    ):
        sw = grad_mag[row + 1, col - 1]
        ne = grad_mag[row - 1, col + 1]
        if grad_mag[row, col] >= sw and grad_mag[row, col] >= ne:
            image[row, col] = grad_mag[row, col]
            
def angle_case3(dir, grad_mag, image, row, col):
    """
    Suppress the non-maximum value vertically.
    Args:
        dir: gradient direction
        grad_mag: map of gradient magnitude
        image: edge map
        row: first dimension coordinate of image
        col: second dimension coordinate of image
    """
    if (3 * PI / 8 <= dir < 5 * PI / 8) or (
        11 * PI / 8 <= dir < 13 * PI / 8
    ):
        n = grad_mag[row - 1, col]
        s = grad_mag[row + 1, col]
        if grad_mag[row, col] >= n and grad_mag[row, col] >= s:
            image[row, col] = grad_mag[row, col]

def angle_case4(dir, grad_mag, image, row, col):
    """
    Suppress the non-maximum value diagonally.
    Args:
        dir: gradient direction
        grad_mag: map of gradient magnitude
        image: edge map
        row: first dimension coordinate of image
        col: second dimension coordinate of image
    """
    if (5 * PI / 8 <= dir < 7 * PI / 8) or (
        13 * PI / 8 <= dir < 15 * PI / 8
    ):
        nw = grad_mag[row - 1, col - 1]
        se = grad_mag[row + 1, col + 1]
        if grad_mag[row, col] >= nw and grad_mag[row, col] >= se:
            image[row, col] = grad_mag[row, col]
                    
def threshold(image, row, col, high, low, strong, weak):
    """
    High-Low threshold detection. If an edge pixel's gradient value is higher
    than the high threshold value, it is marked as a strong edge pixel. If an
    edge pixel's gradient value is smaller than the high threshold value and
    larger than the low threshold value, it is marked as a weak edge pixel. If
    an edge pixel's value is smaller than the low threshold value, it will be
    suppressed.
    """
    if image[row, col] >= high:
        image[row, col] = strong
    elif image[row, col] <= low:
        image[row, col] = 0
    else:
        image[row, col] = weak

def edge_tracking(image, weak, strong):
    """
    Edge tracking. Usually a weak edge pixel caused from true edges will be connected
    to a strong edge pixel while noise responses are unconnected. As long as there is
    one strong edge pixel that is involved in its 8-connected neighborhood, that weak
    edge point can be identified as one that should be preserved.
    """
    image_row, image_col = image.shape
    for row in range(1, image_row):
        for col in range(1, image_col):
            if image[row, col] == weak:
                if 255 in (
                    image[row, col + 1],
                    image[row, col - 1],
                    image[row - 1, col],
                    image[row + 1, col],
                    image[row - 1, col - 1],
                    image[row + 1, col - 1],
                    image[row - 1, col + 1],
                    image[row + 1, col + 1],
                ):
                    image[row, col] = strong
                else:
                    image[row, col] = 0


def canny(image, threshold_low=15, threshold_high=30, weak=128, strong=255):
    image_row, image_col = image.shape[0], image.shape[1]
    # gaussian_filter
    gaussian_out = img_convolve(image, gen_gaussian_kernel(9, sigma=1.4))
    # get the gradient and degree by sobel_filter
    sobel_grad, sobel_theta = sobel_filter(gaussian_out)
    gradient_direction = np.rad2deg(sobel_theta)
    gradient_direction += PI

    dst = np.zeros((image_row, image_col))

    non_maximum_suppression(dst, gradient_direction, sobel_grad, strong, weak, threshold_low, threshold_high)
    
    edge_tracking(dst, weak, strong)

    return dst


if __name__ == "__main__":
    # read original image in gray mode
    lena = cv2.imread(r"../image_data/lena.jpg", 0)
    # canny edge detection
    canny_dst = canny(lena)
    cv2.imshow("canny", canny_dst)
    cv2.waitKey(0)
