"""
Swish Activation Function

Use Case: Enhances the expression of input data and weight to be learnt.
For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Swish_function
"""

import numpy as np


def swish(vector: np.ndarray) -> np.ndarray:
    """
        Implements the Swish activation function.

        Parameters:
            vector (np.ndarray): The input array for Swish activation.

        Returns:
            np.ndarray: The output array after applying the Swish activation.

        Formula: f(x) = x / (1 + np.exp(-x))

    Examples:
    >>> swish(vector=np.array([2.3,0.6,-2,-3.8]))
    array([ 2.09041719,  0.38739378, -0.23840584, -0.08314883])

    >>> swish(np.array([-9.2, -0.3, 0.45, -4.56]))
    array([-0.00092947, -0.12766724,  0.27478766, -0.04721304])

    """
    return vector / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
