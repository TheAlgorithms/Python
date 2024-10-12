"""
Maxout activation function

Use Case: Maxout allows for more flexibility than traditional
activation functions like ReLU and can improve model capacity.

For more detailed information, you can refer to the following link:
https://arxiv.org/abs/1302.4389
"""

import numpy as np


def maxout(vector: np.ndarray) -> np.ndarray:
    """
    Implements the Maxout Activation Function.

    Parameters:
        vector (np.ndarray): The input array for Maxout activation.

    Returns:
        np.ndarray: The output of Maxout activation applied to pairs of inputs.

    Formula: f(x) = max(x_1, x_2)

    Examples:
    >>> maxout(np.array([[2., -3.], [-1., 4.]]))
    array([[2.],
           [4.]])

    >>> maxout(np.array([[5, -5], [3, -3]]))
    array([[5],
           [3]])

    """
    return np.maximum(
        vector[:, : vector.shape[1] // 2], vector[:, vector.shape[1] // 2 :]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
