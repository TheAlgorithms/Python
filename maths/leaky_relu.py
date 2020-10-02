"""
This script demonstrates the implementation of the Leaky ReLU function.

It's a kind of activation function in the context of neural network.
The function takes a vector of K real numbers and parameter alpha as
input and then if x > 0, return x or x * alpha.
After through Leaky ReLU, the element of the vector always real number
or real number * alpha.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
"""
from __future__ import annotations

import numpy as np


def leaky_relu(vector: list[float], alpha: float):
    """
    Implements the leaky relu function

    Parameters:
        vector (np.array, list, tuple): A  numpy array of shape (1,n)
        consisting of real values or a similar list,tuple
        alpha (float): Float >= 0

    Returns:
        leaky_relu_vec (np.array): The input numpy array, after applying
        leaky_relu.

    >>> vec = (np.array([-1, 0, 5]), 0.01)
    >>> leaky_relu(vec)
    array([-0.01, 0, 5])
    """

    vector = np.array(vector)

    # compare two arrays and then return real values' or multiplied values' vector.
    return np.where(vector > 0, vector, vector * alpha)


if __name__ == "__main__":
    print(leaky_relu([-1, 0, 5], 0.01))  # --> [-0.01, 0, 5]
