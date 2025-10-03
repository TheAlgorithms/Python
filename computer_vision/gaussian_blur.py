import math
import copy

"""Mean thresholding algorithm for image processing
[More info on Wikipedia](https://en.wikipedia.org/wiki/Thresholding_(image_processing))
"""
# Imagen de ejemplo: matriz 5x5
image = [
    [10, 20, 30, 40, 50],
    [20, 30, 40, 50, 60],
    [30, 40, 50, 60, 70],
    [40, 50, 60, 70, 80],
    [50, 60, 70, 80, 90],
]


def gaussian_kernel(size, sigma=1):
    """Genera un kernel gaussiano de tamaño 'size' y desviación 'sigma'"""
    kernel = [[0] * size for _ in range(size)]
    center = size // 2
    s = 2 * sigma * sigma
    sum_val = 0

    for i in range(size):
        for j in range(size):
            x, y = i - center, j - center
            kernel[i][j] = math.exp(-(x * x + y * y) / s)
            sum_val += kernel[i][j]

    # Normalizar
    for i in range(size):
        for j in range(size):
            kernel[i][j] /= sum_val

    return kernel


def apply_gaussian_blur(image, kernel):
    """Aplica el blur gaussiano a una imagen"""
    height = len(image)
    width = len(image[0])
    k_size = len(kernel)
    k_center = k_size // 2
    new_image = copy.deepcopy(image)

    for i in range(height):
        for j in range(width):
            val = 0
            for ki in range(k_size):
                for kj in range(k_size):
                    ni = i + ki - k_center
                    nj = j + kj - k_center
                    if 0 <= ni < height and 0 <= nj < width:
                        val += image[ni][nj] * kernel[ki][kj]
            new_image[i][j] = int(val)
    return new_image


kernel = gaussian_kernel(3, sigma=1)
blurred_image = apply_gaussian_blur(image, kernel)

for row in blurred_image:
    print(row)
