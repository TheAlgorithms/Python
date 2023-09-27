"""
Leaky Rectified Linear Unit (Leaky ReLU)

Use Case: Leaky ReLU addresses the problem of the vanishing gradient.
For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Leaky_ReLU
"""

import numpy as np


def leaky_rectified_linear_unit(vector: np.ndarray, alpha: float) -> np.ndarray:
    """
        Implements the LeakyReLU activation function.

        Parameters:
            vector (np.ndarray): The input array for LeakyReLU activation.
            alpha (float): The slope for negative values.

        Returns:
            np.ndarray: The input array after applying the LeakyReLU activation.

        Formula: f(x) = x if x > 0 else f(x) = alpha * x

    Examples:
    >>> leaky_rectified_linear_unit(vector=np.array([2.3,0.6,-2,-3.8]), alpha=0.3)
    array([ 2.3 ,  0.6 , -0.6 , -1.14])

    >>> leaky_rectified_linear_unit(np.array([-9.2, -0.3, 0.45, -4.56]), alpha=0.067)
    array([-0.6164 , -0.0201 ,  0.45   , -0.30552])

    """
    return np.where(vector > 0, vector, alpha * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
