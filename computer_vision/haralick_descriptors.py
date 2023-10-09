import imageio
import numpy as np

def root_mean_square_error(original: np.ndarray, reference: np.ndarray) -> float:
    return np.sqrt(((original - reference) ** 2).mean())

def normalize_image(
    image: np.ndarray, cap: float = 255.0, data_type: np.dtype = np.uint8
) -> np.ndarray:
    normalized = (image - np.min(image)) / (np.max(image) - np.min(image)) * cap
    return normalized.astype(data_type)

def normalize_array(array: np.ndarray, cap: float = 1) -> np.ndarray:
    diff = np.max(array) - np.min(array)
    return (array - np.min(array)) / (1 if diff == 0 else diff) * cap

def grayscale(image: np.ndarray) -> np.ndarray:
    return np.dot(image[:, :, 0:3], [0.299, 0.587, 0.114]).astype(np.uint8)

def binarize(image: np.ndarray, threshold: float = 127.0) -> np.ndarray:
    return np.where(image > threshold, 1, 0)

def transform(
    image: np.ndarray, kind: str, kernel: np.ndarray | None = None
) -> np.ndarray:
    if kernel is None:
        kernel = np.ones((3, 3))

    if kind == "erosion":
        constant = 1
        apply = np.max
    else:
        constant = 0
        apply = np.min

    center_x, center_y = (x // 2 for x in kernel.shape)

    transformed = np.zeros(image.shape, dtype=np.uint8)
    padded = np.pad(image, 1, "constant", constant_values=constant)

    for x in range(center_x, padded.shape[0] - center_x):
        for y in range(center_y, padded.shape[1] - center_y):
            center = padded[
                x - center_x : x + center_x + 1, y - center_y : y + center_y + 1
            ]
            transformed[x - center_x, y - center_y] = apply(center[kernel == 1])

    return transformed

def opening_filter(image: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    if kernel is None:
        kernel = np.ones((3, 3))

    return transform(transform(image, "dilation", kernel), "erosion", kernel)

def closing_filter(image: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    if kernel is None:
        kernel = np.ones((3, 3))
    return transform(transform(image, "erosion", kernel), "dilation", kernel)

def binary_mask(
    image_gray: np.ndarray, image_map: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    true_mask, false_mask = image_gray.copy(), image_gray.copy()
    true_mask[image_map == 1] = 1
    false_mask[image_map == 0] = 0

    return true_mask, false_mask

def matrix_concurrency(image: np.ndarray, coordinate: tuple[int, int]) -> np.ndarray:
    matrix = np.zeros([np.max(image) + 1, np.max(image) + 1])

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
    correlation = prod * matrix
    energy = np.power(matrix, 2)
    contrast = matrix * np.power(sub, 2)

    dissimilarity = matrix * np.abs(sub)
    inverse_difference = matrix / (1 + np.abs(sub))
    homogeneity = matrix / (1 + np.power(sub, 2))
    entropy = -(matrix[matrix > 0] * np.log(matrix[matrix > 0]))

    return [
        maximum_prob,
        correlation.sum(),
        energy.sum(),
        contrast.sum(),
        dissimilarity.sum(),
        inverse_difference.sum(),
        homogeneity.sum(),
        entropy.sum(),
    ]

def get_descriptors(
    masks: tuple[np.ndarray, np.ndarray], coordinate: tuple[int, int]
) -> np.ndarray:
    descriptors = np.array(
        [haralick_descriptors(matrix_concurrency(mask, coordinate)) for mask in masks]
    )
    return np.concatenate(descriptors, axis=None)

def euclidean(point_1: np.ndarray, point_2: np.ndarray) -> np.float32:
    return np.sqrt(np.sum(np.square(point_1 - point_2)))

def get_distances(descriptors: np.ndarray, base: int) -> list[tuple[int, float]]:
    distances = np.array(
        [euclidean(descriptor, descriptors[base]) for descriptor in descriptors]
    )
    normalized_distances: list[float] = normalize_array(distances, 1).tolist()
    enum_distances = list(enumerate(normalized_distances))
    enum_distances.sort(key=lambda tup: tup[1], reverse=True)
    return enum_distances

if __name__ == "__main__":
    index = int(input())
    q_value_list = [int(value) for value in input().split()]
    q_value = (q_value_list[0], q_value_list[1])

    parameters = {"format": int(input()), "threshold": int(input())}

    b_number = int(input())

    files, descriptors = [], []

    for _ in range(b_number):
        file = input().rstrip()
        files.append(file)

        image = imageio.imread(file).astype(np.float32)
        gray = grayscale(image)
        threshold = binarize(gray, parameters["threshold"])

        morphological = (
            opening_filter(threshold)
            if parameters["format"] == 1
            else closing_filter(threshold)
        )
        masks = binary_mask(gray, morphological)
        descriptors.append(get_descriptors(masks, q_value))

    distances = get_distances(np.array(descriptors), index)
    indexed_distances = np.array(distances).astype(np.uint8)[:, 0]

    print(f"Query: {files[index]}")
    print("Ranking:")
    for idx, file_idx in enumerate(indexed_distances):
        print(f"({idx}) {files[file_idx]}", end="\n")
