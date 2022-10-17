"""
This script demonstrates the implementation of the Gelu function.

The function takes a vector x of K real numbers as input and
resukts x * sigmoid(1.702*x).
The Gaussian Error Linear Unit (GELU), is a high-performing neural
network activation function.

Script inspired from its corresponding research paper
https://arxiv.org/abs/1606.08415
"""

import numpy as np


def sigmoid(vector: np.array) -> np.array:
    """
    Gelu function can be implemented easily with the help of
    sigmoid function
    """
    return 1 / (1 + np.exp(-vector))


def gelu(vector: np.array) -> np.array:
    """
    Implements the Gelu function

    Parameters:
        vector (np.array): A  numpy array of shape (1,n)
        consisting of real values

    Returns:
        gelu_vec (np.array): The input numpy array, after applying
        gelu.

    Examples:
    >>> gelu(np.array([-1.0, 1.0, 2.0]))
    array([-0.15420423,  0.84579577,  1.93565862])

    >>> gelu(np.array([-3]))
    array([-0.01807131])
    """
    return vector * sigmoid(1.702 * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
