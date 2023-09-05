"""
https://en.wikipedia.org/wiki/Image_texture
https://en.wikipedia.org/wiki/Co-occurrence_matrix#Application_to_image_analysis
"""
import imageio.v2 as imageio
import numpy as np


def root_mean_square_error(original: np.ndarray, reference: np.ndarray) -> float:
    """Simple implementation of Root Mean Squared Error
    for two N dimensional numpy arrays.

    Examples:
        >>> root_mean_square_error(np.array([1, 2, 3]), np.array([1, 2, 3]))
        0.0
        >>> root_mean_square_error(np.array([1, 2, 3]), np.array([2, 2, 2]))
        0.816496580927726
        >>> root_mean_square_error(np.array([1, 2, 3]), np.array([6, 4, 2]))
        3.1622776601683795
    """
    return np.sqrt(((original - reference) ** 2).mean())


def normalize_image(
    image: np.ndarray, cap: float = 255.0, data_type: np.dtype = np.uint8
) -> np.ndarray:
    """
    Normalizes image in Numpy 2D array format, between ranges 0-cap,
    as to fit uint8 type.

    Args:
        image: 2D numpy array representing image as matrix, with values in any range
        cap: Maximum cap amount for normalization
        data_type: numpy data type to set output variable to
    Returns:
        return 2D numpy array of type uint8, corresponding to limited range matrix

    Examples:
        >>> normalize_image(np.array([[1, 2, 3], [4, 5, 10]]),
        ...                 cap=1.0, data_type=np.float64)
        array([[0.        , 0.11111111, 0.22222222],
               [0.33333333, 0.44444444, 1.        ]])
        >>> normalize_image(np.array([[4, 4, 3], [1, 7, 2]]))
        array([[127, 127,  85],
               [  0, 255,  42]], dtype=uint8)
    """
    normalized = (image - np.min(image)) / (np.max(image) - np.min(image)) * cap
    return normalized.astype(data_type)


def normalize_array(array: np.ndarray, cap: float = 1) -> np.ndarray:
    """Normalizes a 1D array, between ranges 0-cap.

    Args:
        array: List containing values to be normalized between cap range.
        cap: Maximum cap amount for normalization.
    Returns:
        return 1D numpy array, corresponding to limited range array

    Examples:
        >>> normalize_array(np.array([2, 3, 5, 7]))
        array([0. , 0.2, 0.6, 1. ])
        >>> normalize_array(np.array([[5], [7], [11], [13]]))
        array([[0.  ],
               [0.25],
               [0.75],
               [1.  ]])
    """
    diff = np.max(array) - np.min(array)
    return (array - np.min(array)) / (1 if diff == 0 else diff) * cap


def grayscale(image: np.ndarray) -> np.ndarray:
    """
    Uses luminance weights to transform RGB channel to greyscale, by
    taking the dot product between the channel and the weights.

    Example:
        >>> grayscale(np.array([[[108, 201, 72], [255, 11,  127]],
        ...                     [[56,  56,  56], [128, 255, 107]]]))
        array([[158,  97],
               [ 56, 200]], dtype=uint8)
    """
    return np.dot(image[:, :, 0:3], [0.299, 0.587, 0.114]).astype(np.uint8)


def binarize(image: np.ndarray, threshold: float = 127.0) -> np.ndarray:
    """
    Binarizes a grayscale image based on a given threshold value,
    setting values to 1 or 0 accordingly.

    Examples:
        >>> binarize(np.array([[128, 255], [101, 156]]))
        array([[1, 1],
               [0, 1]])
        >>> binarize(np.array([[0.07, 1], [0.51, 0.3]]), threshold=0.5)
        array([[0, 1],
               [1, 0]])
    """
    return np.where(image > threshold, 1, 0)


def transform(image: np.ndarray, kind: str, kernel: np.ndarray = None) -> np.ndarray:
    """
    Simple image transformation using one of two available filter functions:
    Erosion and Dilation.

    Args:
        image: binarized input image, onto which to apply transformation
        kind: Can be either 'erosion', in which case the :func:np.max
              function is called, or 'dilation', when :func:np.min is used instead.
        kernel: n x n kernel with shape < :attr:image.shape,
              to be used when applying convolution to original image

    Returns:
        returns a numpy array with same shape as input image,
        corresponding to applied binary transformation.

    Examples:
        >>> img = np.array([[1, 0.5], [0.2, 0.7]])
        >>> img = binarize(img, threshold=0.5)
        >>> transform(img, 'erosion')
        array([[1, 1],
               [1, 1]], dtype=uint8)
        >>> transform(img, 'dilation')
        array([[0, 0],
               [0, 0]], dtype=uint8)
    """
    if kernel is None:
        kernel = np.ones((3, 3))

    if kind == "erosion":
        constant = 1
        apply = np.max
    else:
        constant = 0
        apply = np.min

    center_x, center_y = (x // 2 for x in kernel.shape)

    # Use padded image when applying convolotion
    # to not go out of bounds of the original the image
    transformed = np.zeros(image.shape, dtype=np.uint8)
    padded = np.pad(image, 1, "constant", constant_values=constant)

    for x in range(center_x, padded.shape[0] - center_x):
        for y in range(center_y, padded.shape[1] - center_y):
            center = padded[
                x - center_x : x + center_x + 1, y - center_y : y + center_y + 1
            ]
            # Apply transformation method to the centered section of the image
            transformed[x - center_x, y - center_y] = apply(center[kernel == 1])

    return transformed


def opening_filter(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """
    Opening filter, defined as the sequence of
    erosion and then a dilation filter on the same image.

    Examples:
        >>> img = np.array([[1, 0.5], [0.2, 0.7]])
        >>> img = binarize(img, threshold=0.5)
        >>> opening_filter(img)
        array([[1, 1],
               [1, 1]], dtype=uint8)
    """
    if kernel is None:
        np.ones((3, 3))

    return transform(transform(image, "dilation", kernel), "erosion", kernel)


def closing_filter(image: np.ndarray, kernel: np.ndarray = None) -> np.ndarray:
    """
    Opening filter, defined as the sequence of
    dilation and then erosion filter on the same image.

    Examples:
        >>> img = np.array([[1, 0.5], [0.2, 0.7]])
        >>> img = binarize(img, threshold=0.5)
        >>> closing_filter(img)
        array([[0, 0],
               [0, 0]], dtype=uint8)
    """
    if kernel is None:
        kernel = np.ones((3, 3))
    return transform(transform(image, "erosion", kernel), "dilation", kernel)


def binary_mask(
    image_gray: np.ndarray, image_map: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Apply binary mask, or thresholding based
    on bit mask value (mapping mask is binary).

    Returns the mapped true value mask and its complementary false value mask.

    Example:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gray = grayscale(img)
        >>> binary = binarize(gray)
        >>> morphological = opening_filter(binary)
        >>> binary_mask(gray, morphological)
        (array([[1, 1],
               [1, 1]], dtype=uint8), array([[158,  97],
               [ 56, 200]], dtype=uint8))
    """
    true_mask, false_mask = image_gray.copy(), image_gray.copy()
    true_mask[image_map == 1] = 1
    false_mask[image_map == 0] = 0

    return true_mask, false_mask


def matrix_concurrency(image: np.ndarray, coordinate: tuple[int, int]) -> np.ndarray:
    """
    Calculate sample co-occurrence matrix based on input image
    as well as selected coordinates on image.

    Implementation is made using basic iteration,
    as function to be performed (np.max) is non-linear and therefore
    not callable on the frequency domain.

    Example:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gray = grayscale(img)
        >>> binary = binarize(gray)
        >>> morphological = opening_filter(binary)
        >>> mask_1 = binary_mask(gray, morphological)[0]
        >>> matrix_concurrency(mask_1, (0, 1))
        array([[0., 0.],
               [0., 0.]])
    """
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
    """Calculates all 8 Haralick descriptors based on co-occurence input matrix.
    All descriptors are as follows:
    Maximum probability, Inverse Difference, Homogeneity, Entropy,
    Energy, Dissimilarity, Contrast and Correlation

    Args:
        matrix: Co-occurence matrix to use as base for calculating descriptors.

    Returns:
        Reverse ordered list of resulting descriptors

    Example:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gray = grayscale(img)
        >>> binary = binarize(gray)
        >>> morphological = opening_filter(binary)
        >>> mask_1 = binary_mask(gray, morphological)[0]
        >>> concurrency = matrix_concurrency(mask_1, (0, 1))
        >>> haralick_descriptors(concurrency)
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    """
    # Function np.indices could be used for bigger input types,
    # but np.ogrid works just fine
    i, j = np.ogrid[0 : matrix.shape[0], 0 : matrix.shape[1]]  # np.indices()

    # Pre-calculate frequent multiplication and subtraction
    prod = np.multiply(i, j)
    sub = np.subtract(i, j)

    # Calculate numerical value of Maximum Probability
    maximum_prob = np.max(matrix)
    # Using the definition for each descriptor individually to calculate its matrix
    correlation = prod * matrix
    energy = np.power(matrix, 2)
    contrast = matrix * np.power(sub, 2)

    dissimilarity = matrix * np.abs(sub)
    inverse_difference = matrix / (1 + np.abs(sub))
    homogeneity = matrix / (1 + np.power(sub, 2))
    entropy = -(matrix[matrix > 0] * np.log(matrix[matrix > 0]))

    # Sum values for descriptors ranging from the first one to the last,
    # as all are their respective origin matrix and not the resulting value yet.
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
    """
    Calculate all Haralick descriptors for a sequence of
    different co-occurrence matrices, given input masks and coordinates.

    Example:
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gray = grayscale(img)
        >>> binary = binarize(gray)
        >>> morphological = opening_filter(binary)
        >>> get_descriptors(binary_mask(gray, morphological), (0, 1))
        array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    """
    descriptors = np.array(
        [haralick_descriptors(matrix_concurrency(mask, coordinate)) for mask in masks]
    )

    # Concatenate each individual descriptor into
    # one single list containing sequence of descriptors
    return np.concatenate(descriptors, axis=None)


def euclidean(point_1: np.ndarray, point_2: np.ndarray) -> np.float32:
    """
    Simple method for calculating the euclidean distance between two points,
    with type np.ndarray.

    Example:
        >>> a = np.array([1, 0, -2])
        >>> b = np.array([2, -1, 1])
        >>> euclidean(a, b)
        3.3166247903554
    """
    return np.sqrt(np.sum(np.square(point_1 - point_2)))


def get_distances(descriptors: np.ndarray, base: int) -> list[tuple[int, float]]:
    """
    Calculate all Euclidean distances between a selected base descriptor
    and all other Haralick descriptors
    The resulting comparison is return in decreasing order,
    showing which descriptor is the most similar to the selected base.

    Args:
        descriptors: Haralick descriptors to compare with base index
        base: Haralick descriptor index to use as base when calculating respective
        euclidean distance to other descriptors.

    Returns:
        Ordered distances between descriptors

    Example:
        >>> index = 1
        >>> img = np.array([[[108, 201, 72], [255, 11,  127]],
        ...                 [[56,  56,  56], [128, 255, 107]]])
        >>> gray = grayscale(img)
        >>> binary = binarize(gray)
        >>> morphological = opening_filter(binary)
        >>> get_distances(get_descriptors(
        ...                 binary_mask(gray, morphological), (0, 1)),
        ...               index)
        [(0, 0.0), (1, 0.0), (2, 0.0), (3, 0.0), (4, 0.0), (5, 0.0), \
(6, 0.0), (7, 0.0), (8, 0.0), (9, 0.0), (10, 0.0), (11, 0.0), (12, 0.0), \
(13, 0.0), (14, 0.0), (15, 0.0)]
    """
    distances = np.array(
        [euclidean(descriptor, descriptors[base]) for descriptor in descriptors]
    )
    # Normalize distances between range [0, 1]
    normalized_distances: list[float] = normalize_array(distances, 1).tolist()
    enum_distances = list(enumerate(normalized_distances))
    enum_distances.sort(key=lambda tup: tup[1], reverse=True)
    return enum_distances


if __name__ == "__main__":
    # Index to compare haralick descriptors to
    index = int(input())
    q_value_list = [int(value) for value in input().split()]
    q_value = (q_value_list[0], q_value_list[1])

    # Format is the respective filter to apply,
    # can be either 1 for the opening filter or else for the closing
    parameters = {"format": int(input()), "threshold": int(input())}

    # Number of images to perform methods on
    b_number = int(input())

    files, descriptors = [], []

    for _ in range(b_number):
        file = input().rstrip()
        files.append(file)

        # Open given image and calculate morphological filter,
        # respective masks and correspondent Harralick Descriptors.
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

    # Transform ordered distances array into a sequence of indexes
    # corresponding to original file position
    distances = get_distances(np.array(descriptors), index)
    indexed_distances = np.array(distances).astype(np.uint8)[:, 0]

    # Finally, print distances considering the Haralick descriptions from the base
    # file to all other images using the morphology method of choice.
    print(f"Query: {files[index]}")
    print("Ranking:")
    for idx, file_idx in enumerate(indexed_distances):
        print(f"({idx}) {files[file_idx]}", end="\n")
