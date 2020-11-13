"""
Similarity Search : https://en.wikipedia.org/wiki/Similarity_search
Similarity search is a search algorithm for finding the nearest vector from
vectors, used in natural language processing.
In this algorithm, it calculates distance with euclidean distance and
returns a list containing two data for each vector:
    1. the nearest vector
    2. distance between the vector and the nearest vector (float)
"""
import math

import numpy as np


def euclidean(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    Calculates euclidean distance between two data.
    :param input_a: ndarray of first vector.
    :param input_b: ndarray of second vector.
    :return: Euclidean distance of input_a and input_b. By using math.sqrt(),
             result will be float.

    >>> euclidean(np.array([0]), np.array([1]))
    1.0
    >>> euclidean(np.array([0, 1]), np.array([1, 1]))
    1.0
    >>> euclidean(np.array([0, 0, 0]), np.array([0, 0, 1]))
    1.0
    """
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(input_a, input_b)))


def similarity_search(dataset: np.ndarray, value_array: np.ndarray) -> list:
    """
    :param dataset: Set containing the vectors. Should be ndarray.
    :param value_array: vector/vectors we want to know the nearest vector from dataset.
    :return: Result will be a list containing
            1. the nearest vector
            2. distance from the vector

    >>> dataset = np.array([[0], [1], [2]])
    >>> value_array = np.array([[0]])
    >>> similarity_search(dataset, value_array)
    [[[0], 0.0]]

    >>> dataset = np.array([[0, 0], [1, 1], [2, 2]])
    >>> value_array = np.array([[0, 1]])
    >>> similarity_search(dataset, value_array)
    [[[0, 0], 1.0]]

    >>> dataset = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> value_array = np.array([[0, 0, 1]])
    >>> similarity_search(dataset, value_array)
    [[[0, 0, 0], 1.0]]

    >>> dataset = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> value_array = np.array([[0, 0, 0], [0, 0, 1]])
    >>> similarity_search(dataset, value_array)
    [[[0, 0, 0], 0.0], [[0, 0, 0], 1.0]]

    These are the errors that might occur:

    1. If dimensions are different.
    For example, dataset has 2d array and value_array has 1d array:
    >>> dataset = np.array([[1]])
    >>> value_array = np.array([1])
    >>> similarity_search(dataset, value_array)
    Traceback (most recent call last):
    ...
    ValueError: Wrong input data's dimensions... dataset : 2, value_array : 1

    2. If data's shapes are different.
    For example, dataset has shape of (3, 2) and value_array has (2, 3).
    We are expecting same shapes of two arrays, so it is wrong.
    >>> dataset = np.array([[0, 0], [1, 1], [2, 2]])
    >>> value_array = np.array([[0, 0, 0], [0, 0, 1]])
    >>> similarity_search(dataset, value_array)
    Traceback (most recent call last):
    ...
    ValueError: Wrong input data's shape... dataset : 2, value_array : 3

    3. If data types are different.
    When trying to compare, we are expecting same types so they should be same.
    If not, it'll come up with errors.
    >>> dataset = np.array([[0, 0], [1, 1], [2, 2]], dtype=np.float32)
    >>> value_array = np.array([[0, 0], [0, 1]], dtype=np.int32)
    >>> similarity_search(dataset, value_array)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ...
    TypeError: Input data have different datatype...
    dataset : float32, value_array : int32
    """

    if dataset.ndim != value_array.ndim:
        raise ValueError(
            f"Wrong input data's dimensions... dataset : {dataset.ndim}, "
            f"value_array : {value_array.ndim}"
        )

    try:
        if dataset.shape[1] != value_array.shape[1]:
            raise ValueError(
                f"Wrong input data's shape... dataset : {dataset.shape[1]}, "
                f"value_array : {value_array.shape[1]}"
            )
    except IndexError:
        if dataset.ndim != value_array.ndim:
            raise TypeError("Wrong shape")

    if dataset.dtype != value_array.dtype:
        raise TypeError(
            f"Input data have different datatype... dataset : {dataset.dtype}, "
            f"value_array : {value_array.dtype}"
        )

    answer = []

    for value in value_array:
        dist = euclidean(value, dataset[0])
        vector = dataset[0].tolist()

        for dataset_value in dataset[1:]:
            temp_dist = euclidean(value, dataset_value)

            if dist > temp_dist:
                dist = temp_dist
                vector = dataset_value.tolist()

        answer.append([vector, dist])

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
