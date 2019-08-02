"""
Implementation hog(Histogram of Oriented Gradients) feature of image according
the paper[https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf].
"""

import math
import cv2
import numpy as np
from digital_image_processing.filters.convolve import img_convolve


def hog_feature(image, gamma=0.4, cell_size=6, bin_size=18, block_size=4):
    rows, cols = image.shape[0], image.shape[1]

    """
    Gamma normalization, however, the author point out this step can be omitted in HOG descriptor computation.
    """
    norm = (image + 0.5)/255
    norm = np.power(norm, 1/gamma)
    img_norm = 255 * norm - 0.5

    # Get gradient and angle, the kernel below perform better than others(3x3 Sobel).
    kernel_x = np.array([[-1, 0, 1]])
    kernel_y = np.array([[-1], [0], [1]])

    dst_x = img_convolve(img_norm, kernel_x)
    dst_y = img_convolve(img_norm, kernel_y)

    dst_xy = np.sqrt((np.square(dst_x)) + (np.square(dst_y)))
    dst_xy = dst_xy * 255 / np.max(dst_xy)
    gradient_magnitude_global = dst_xy

    # Get the angles and convert them in range (0, 360)
    theta = np.arctan2(dst_y, dst_x)
    gradient_angle_global = np.rad2deg(theta)  # range(-180, 180)
    gradient_angle_global = np.where(gradient_angle_global < 0,
                                     gradient_angle_global + 360,
                                     gradient_angle_global)  # range(0, 360)

    """
    Orientation binning, The second step of calculation is creating the cell histograms. Each pixel within the cell 
    casts a weighted vote for an orientation-based histogram channel based on the values found in the gradient 
    computation. In tests, the gradient magnitude itself generally produces the best results.
    """
    angle_unit = 360 / bin_size
    cell_gradient_mtx = np.zeros((rows // cell_size, cols // cell_size, bin_size))
    for i in range(cell_gradient_mtx.shape[0]):
        for j in range(cell_gradient_mtx.shape[1]):
            pixes_grad_per_cell = gradient_magnitude_global[i * cell_size:(i + 1) * cell_size,
                                                            j * cell_size:(j + 1) * cell_size]
            pixes_angle_per_cell = gradient_angle_global[i * cell_size:(i + 1) * cell_size,
                                                         j * cell_size:(j + 1) * cell_size]

            orientation_centers = [0] * bin_size
            for cell_i in range(pixes_grad_per_cell.shape[0]):
                for cell_j in range(pixes_grad_per_cell.shape[1]):
                    gradient_strength = pixes_grad_per_cell[cell_i][cell_j]
                    gradient_angle = pixes_angle_per_cell[cell_i][cell_j]

                    bin_index = int(gradient_angle / angle_unit)
                    if gradient_angle == 360:
                        bin_index = 0
                    orientation_centers[bin_index] += gradient_strength

            cell_gradient_mtx[i][j] = orientation_centers

    """
    Descriptor blocks. Grouping cells into larger spatial blocks and contrast normalizing each 
    block separately. The final descriptor is then the vector of all components of the normalized cell
    responses from all of the blocks in the detection window.
    """
    hog_descriptor_mtx = []
    out_rows, out_cols = cell_gradient_mtx.shape[1] - block_size + 1, cell_gradient_mtx.shape[0] - block_size + 1
    for i in range(0, out_rows):
        for j in range(0, out_cols):
            block_vector = np.ravel(cell_gradient_mtx[i:i + block_size, j:j + block_size, :])

            # Block L2 normalization
            eps = 1e-5
            block_vector = block_vector / np.sqrt(np.sum(block_vector ** 2) + eps ** 2)
            hog_descriptor_mtx.append(block_vector)

    # showing hog
    hog_dst_image = np.zeros([rows, cols])
    cell_gradient = cell_gradient_mtx
    cell_width = cell_size // 2
    max_mag = np.array(cell_gradient).max()
    for x in range(cell_gradient.shape[0]):
        for y in range(cell_gradient.shape[1]):
            cell_grad = cell_gradient[x][y]
            cell_grad /= max_mag
            angle = 0
            angle_gap = angle_unit
            for magnitude in cell_grad:
                angle_radian = math.radians(angle)
                x1 = int(x * cell_size + magnitude * cell_width * math.cos(angle_radian))
                y1 = int(y * cell_size + magnitude * cell_width * math.sin(angle_radian))
                x2 = int(x * cell_size - magnitude * cell_width * math.cos(angle_radian))
                y2 = int(y * cell_size - magnitude * cell_width * math.sin(angle_radian))

                strength = int(255 * math.sqrt(magnitude))
                cv2.line(hog_dst_image, (y1, x1), (y2, x2), strength)

                angle += angle_gap

    return hog_descriptor_mtx, hog_dst_image


if __name__ == '__main__':
    # read original image in gray model
    img = cv2.imread('../image_data/lena.jpg', 0)
    # extract hog feature
    hog_dsp, hog_img = hog_feature(img)
    cv2.imshow('hog', hog_img.astype(np.uint8))
    cv2.waitKey(0)
