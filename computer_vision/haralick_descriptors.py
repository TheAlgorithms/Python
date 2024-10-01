import imageio.v2 as imageio
import numpy as np

def root_mean_square_error(original: np.ndarray, reference: np.ndarray) -> float:
    return float(np.sqrt(((original - reference) ** 2).mean()))

def normalize_image(image: np.ndarray, cap: float = 255.0, data_type: np.dtype = np.uint8) -> np.ndarray:
    normalized = (image - np.min(image)) / (np.max(image) - np.min(image)) * cap
    return normalized.astype(data_type)

def normalize_array(array: np.ndarray, cap: float = 1) -> np.ndarray:
    diff = np.max(array) - np.min(array)
    if diff == 0:
        return np.zeros_like(array)
    return (array - np.min(array)) / diff * cap

def grayscale(image: np.ndarray) -> np.ndarray:
    return np.dot(image[:, :, 0:3], [0.299, 0.587, 0.114]).astype(np.uint8)

def binarize(image: np.ndarray, threshold: float = 127.0) -> np.ndarray:
    return np.where(image > threshold, 1, 0)

def transform(image: np.ndarray, kind: str, kernel: np.ndarray | None = None) -> np.ndarray:
    if kernel is None:
        kernel = np.ones((3, 3))

    if kind == "erosion":
        constant = 1
        apply = np.max
    else:
        constant = 0
        apply = np.min

    padding_x, padding_y = kernel.shape[0] // 2, kernel.shape[1] // 2
    padded = np.pad(image, ((padding_x, padding_x), (padding_y, padding_y)), 'constant', constant_values=constant)

    transformed = np.zeros(image.shape, dtype=np.uint8)
    for x in range(padding_x, padded.shape[0] - padding_x):
        for y in range(padding_y, padded.shape[1] - padding_y):
            center = padded[x - padding_x : x + padding_x + 1, y - padding_y : y + padding_y + 1]
            transformed[x - padding_x, y - padding_y] = apply(center[kernel == 1])

    return transformed

def opening_filter(image: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    if kernel is None:
        kernel = np.ones((3, 3))
    return transform(transform(image, "dilation", kernel), "erosion", kernel)

def closing_filter(image: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    if kernel is None:
        kernel = np.ones((3, 3))
    return transform(transform(image, "erosion", kernel), "dilation", kernel)

def binary_mask(image_gray: np.ndarray, image_map: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mask, inverse_mask = image_gray.copy(), image_gray.copy()
    mask[image_map == 1] = 1
    inverse_mask[image_map == 0] = 0
    return mask, inverse_mask

def matrix_concurrency(image: np.ndarray, coordinate: tuple[int, int]) -> np.ndarray:
    matrix = np.zeros([int(np.max(image)) + 1, int(np.max(image)) + 1], dtype=np.float32)
    offset_x, offset_y = coordinate

    for x in range(1, image.shape[0] - 1):
        for y in range(1, image.shape[1] - 1):
            base_pixel = image[x, y]
            offset_pixel = image[x + offset_x, y + offset_y]
            matrix[base_pixel, offset_pixel] += 1

    matrix_sum = np.sum(matrix)
    return matrix / (1 if matrix_sum == 0 else matrix_sum)

def haralick_descriptors(matrix: np.ndarray) -> list[float]:
    i, j = np.ogrid[0 : matrix.shape[0], 0 : matrix.shape[1]]
    prod = np.multiply(i, j)
    sub = np.subtract(i, j)

    maximum_prob = np.max(matrix)
    correlation = np.sum(prod * matrix)
    energy = np.sum(np.power(matrix, 2))
    contrast = np.sum(matrix * np.power(sub, 2))
    dissimilarity = np.sum(matrix * np.abs(sub))
    inverse_difference = np.sum(matrix / (1 + np.abs(sub)))
    homogeneity = np.sum(matrix / (1 + np.power(sub, 2)))
    entropy = -(matrix[matrix > 0] * np.log(matrix[matrix > 0])).sum()

    return [maximum_prob, correlation, energy, contrast, dissimilarity, inverse_difference, homogeneity, entropy]

def get_descriptors(masks: tuple[np.ndarray, np.ndarray], coordinate: tuple[int, int]) -> np.ndarray:
    descriptors = np.zeros([2, 8], dtype=np.float32)
    for idx in range(len(masks)):
        matrix = matrix_concurrency(masks[idx], coordinate)
        descriptors[idx, :] = haralick_descriptors(matrix)
    return descriptors
