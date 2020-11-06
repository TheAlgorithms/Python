"""
Simularity search is a search algorithm for finding the nearest vector from
vectors, used in natural language processing.
In this algorithm, it calculates distance with euclidean distance and
returns a list containing two data for each vector:
    1. the nearest vector
    2. distance between the vector and the nearest vector
"""
import math
from typing import Union

import numpy as np

InputVal = Union[int, float, np.ndarray]


def euclidean(input_a: InputVal, input_b: InputVal):
    """
    Calculates euclidean distance between two data. The result should be float.
    >>> euclidean(0, 1)
    1.0
    >>> euclidean(np.array([0, 1]), np.array([1, 1]))
    1.0
    >>> euclidean(np.array([0, 0, 0]), np.array([0, 0, 1]))
    1.0
    """
    dist = 0

    if type(input_a) == type(input_b):
        if type(input_a) != np.ndarray:
            dist = pow(input_a - input_b, 2)
        else:
            for index in range(len(input_a)):
                dist += pow(input_a[index] - input_b[index], 2)
        return math.sqrt(dist)
    return None


def similarity_search(dataset: np.ndarray, value: np.ndarray) -> list:
    """
    :param dataset: Set containing the vectors.
    :param value: vector/vectors we want to know the nearest vector from dataset.
    Result will be a list containing 1. the nearest vector, 2. distance from the vector
    >>> a = np.array([0, 1, 2])
    >>> b = np.array([0])
    >>> similarity_search(a, b)
    [[0, 0.0]]

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
        raise TypeError(
            "Wrong input data's dimensions... dataset : ",
            dataset.ndim,
            ", value : ",
            value.ndim,
        )

    try:
        if dataset.shape[1] != value.shape[1]:
            raise TypeError(
                "Wrong input data's shape... dataset : ",
                dataset.shape[1],
                ", value : ",
                value.shape[1],
            )
    except IndexError:
        if (dataset.ndim == value.ndim) != 1:
            raise TypeError("Wrong type")

    if dataset.dtype != value.dtype:
        raise TypeError(
            "Input data have different datatype... dataset : ",
            dataset.dtype,
            ", value : ",
            value.dtype,
        )

    answer = []

    for index in range(len(value)):
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
