"""
This script demonstrates the implementation of the Sigmoid function.

The function takes a vector of K real numbers as input and then 1 / (1 + exp(-x)).
After through Sigmoid, the element of the vector mostly 0 between 1. or 1 between -1.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Sigmoid_function
"""

import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    Implements the sigmoid function

    Parameters:
        vector (np.array): A  numpy array of shape (1,n)
        consisting of real values

    Returns:
        sigmoid_vec (np.array): The input numpy array, after applying
        sigmoid.

    Examples:
    >>> sigmoid(np.array([-1.0, 1.0, 2.0]))
    array([0.26894142, 0.73105858, 0.88079708])

    >>> sigmoid(np.array([0.0]))
    array([0.5])

    >>> sigmoid(np.array([100.0]))
    array([1.])

    >>> sigmoid(np.array([-100.0]))
    array([3.72007598e-44])
    """
    return 1 / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
