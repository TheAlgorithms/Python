from __future__ import annotations

from typing import Iterable, Union

import numpy as np

Vector = Union[Iterable[float], Iterable[int], np.ndarray]
VectorOut = Union[np.float64, int, float]


def euclidean_distance(vector_1: Vector, vector_2: Vector) -> VectorOut:
    """
    Calculate the distance between the two endpoints of two vectors.
    A vector is defined as a list, tuple, or numpy 1D array.
    >>> euclidean_distance((0, 0), (2, 2))
    2.8284271247461903
    >>> euclidean_distance(np.array([0, 0, 0]), np.array([2, 2, 2]))
    3.4641016151377544
    >>> euclidean_distance(np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]))
    8.0
    >>> euclidean_distance([1, 2, 3, 4], [5, 6, 7, 8])
    8.0
    """
    return np.sqrt(np.sum((np.asarray(vector_1) - np.asarray(vector_2)) ** 2))


def euclidean_distance_no_np(vector_1: Vector, vector_2: Vector) -> VectorOut:
    """
    Calculate the distance between the two endpoints of two vectors without numpy.
    A vector is defined as a list, tuple, or numpy 1D array.
    >>> euclidean_distance_no_np((0, 0), (2, 2))
    2.8284271247461903
    >>> euclidean_distance_no_np([1, 2, 3, 4], [5, 6, 7, 8])
    8.0
    """
    return sum((v1 - v2) ** 2 for v1, v2 in zip(vector_1, vector_2)) ** (1 / 2)


if __name__ == "__main__":

    def benchmark() -> None:
        """
        Benchmarks
        """
        from timeit import timeit

        print("Without Numpy")
        print(
            timeit(
                "euclidean_distance_no_np([1, 2, 3], [4, 5, 6])",
                number=10000,
                globals=globals(),
            )
        )
        print("With Numpy")
        print(
            timeit(
                "euclidean_distance([1, 2, 3], [4, 5, 6])",
                number=10000,
                globals=globals(),
            )
        )

    benchmark()
