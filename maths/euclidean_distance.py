from typing import List, Tuple, Union

import numpy as np

Vector = Union[List[float], List[int], Tuple[float], Tuple[int], np.ndarray]
VectorOut = Union[np.float64, int, float]


def euclidean_distance(vector_1: Vector, vector_2: Vector) -> VectorOut:
    """
    Calculate the distance between the two endpoints of two vectors.
    A vector is defined as a list, tuple, or numpy 1D array.
    2.8284271247461903
    >>> euclidean_distance(np.array([0, 0, 0]), np.array([2, 2, 2]))
    3.4641016151377544
    >>> euclidean_distance(np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]))
    8.0
    >>> euclidean_distance([1, 2, 3, 4], [5, 6, 7, 8])
    8.0
    """
    return np.sqrt(np.sum((np.asarray(vector_1) - np.asarray(vector_2)) ** 2))


if __name__ == "__main__":
    point = np.array([2, 2])
    point_2 = np.array([0, 0])
    print(euclidean_distance(point, point_2))
