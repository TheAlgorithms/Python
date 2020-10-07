#!/usr/bin/python3
# Rank transform: http://www.cs.cornell.edu/~rdz/Papers/ZW-ECCV94.pdf

import numpy as np


def rank_patch(patch: np.ndarray) -> int:
    """
    Given a 3x3 patch window, calculate the rank for the centric pixel.

    >>> rank_patch(np.zeros((3,3)))
    0
    >>> rank_patch(np.eye(3))
    6

    """
    assert np.all(patch.shape == (3, 3))
    return np.sum(patch < patch[1, 1])


def rank_transform(image: np.ndarray) -> np.ndarray:
    """
    Rank transforms the given image.
    Mainly used for applying optical-flow / object tracking.

    Assuming grayscale image. For RGB apply on each channel separately.

    >>> img = np.array([[1,3,3,0,5],
    ...                 [0,1,4,3,2],
    ...                 [1,1,1,2,1],
    ...                 [0,5,0,5,0],
    ...                 [1,0,1,2,2]])
    >>> rank_transform(img)
    array([[0, 0, 0, 0, 0],
           [0, 1, 8, 5, 0],
           [0, 3, 1, 4, 0],
           [0, 8, 0, 8, 0],
           [0, 0, 0, 0, 0]], dtype=uint8)

    >>> rank_transform(np.eye(10))
    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 6, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 6, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 6, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)

    """
    assert len(image.shape) == 2
    result = np.zeros(image.shape, dtype=np.uint8)
    for row in range(1, image.shape[0] - 1):
        for col in range(1, image.shape[1] - 1):
            rank = rank_patch(image[row - 1 : row + 2, col - 1 : col + 2])
            result[row, col] = rank
    return result
