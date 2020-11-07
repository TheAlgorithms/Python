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


def euclidean(input_a: np.ndarray, input_b: np.ndarray):
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

    dist = 0

    try:
        for index, v in enumerate(input_a):
            dist += pow(input_a[index] - input_b[index], 2)
        return math.sqrt(dist)
    except TypeError:
        raise TypeError("Euclidean's input types are not right ...")


def similarity_search(dataset: np.ndarray, value: np.ndarray) -> list:
    """
    :param dataset: Set containing the vectors. Should be ndarray.
    :param value: vector/vectors we want to know the nearest vector from dataset.
    :return: Result will be a list containing
            1. the nearest vector
            2. distance from the vector

    >>> a = np.array([[0], [1], [2]])
    >>> b = np.array([[0]])
    >>> similarity_search(a, b)
    [[[0], 0.0]]

    >>> a = np.array([[0, 0], [1, 1], [2, 2]])
    >>> b = np.array([[0, 1]])
    >>> similarity_search(a, b)
    [[[0, 0], 1.0]]

    >>> a = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> b = np.array([[0, 0, 1]])
    >>> similarity_search(a, b)
    [[[0, 0, 0], 1.0]]

    >>> a = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> b = np.array([[0, 0, 0], [0, 0, 1]])
    >>> similarity_search(a, b)
    [[[0, 0, 0], 0.0], [[0, 0, 0], 1.0]]
    """

    if dataset.ndim != value.ndim:
        raise ValueError(
            f"Wrong input data's dimensions... dataset : {dataset.ndim}, "
            f"value: {value.ndim}"
        )

    try:
        if dataset.shape[1] != value.shape[1]:
            raise ValueError(
                f"Wrong input data's shape... dataset : {dataset.shape[1]}, "
                f"value : {value.shape[1]}"
            )
    except IndexError:
        if dataset.ndim != value.ndim:
            raise TypeError("Wrong type")

    if dataset.dtype != value.dtype:
        raise TypeError(
            f"Input data have different datatype... dataset : {dataset.dtype}, "
            f"value : {value.dtype}"
        )

    answer = []

    for index, v in enumerate(value):
        dist = euclidean(value[index], dataset[0])
        vector = dataset[0].tolist()

        for index2 in range(1, len(dataset)):
            temp_dist = euclidean(value[index], dataset[index2])

            if dist > temp_dist:
                dist = temp_dist
                vector = dataset[index2].tolist()

        answer.append([vector, dist])

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
