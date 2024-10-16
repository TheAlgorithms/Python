"""
Parametric Rectified Linear Unit (PReLU)

Use Case: PReLU addresses the problem of dying ReLU by allowing a
small, learnable slope for negative values, which can improve model
performance.

For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Parametric_ReLU
"""

import numpy as np


def parametric_rectified_linear_unit(
    vector: np.ndarray, alpha: np.ndarray
) -> np.ndarray:
    """
    Implements the Parametric ReLU (PReLU) activation function.

    Parameters:
        vector (np.ndarray): The input array for PReLU activation.
        alpha (np.ndarray): The learnable slope for negative values,
            must be the same shape as vector.

    Returns:
        np.ndarray: The input array after applying the PReLU activation.

    Formula:
    f(x) = x if x > 0 else f(x) = alpha * x

    Examples:
    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([2.3, 0.6, -2, -3.8]),
    ...     alpha=np.array([0.3])
    ... )
    array([ 2.3 ,  0.6 , -0.6 , -1.14])

    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([-9.2, -0.3, 0.45, -4.56]),
    ...     alpha=np.array([0.067])
    ... )
    array([-0.6164 , -0.0201 ,  0.45   , -0.30552])

    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([0, 0, 0]),
    ...     alpha=np.array([0.1, 0.1, 0.1])
    ... )
    array([0., 0., 0.])

    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([-1, -2, -3]),
    ...     alpha=np.array([0.5, 1, 1.5])
    ... )
    array([-0.5, -2. , -4.5])

    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([-1, 2, -3]),
    ...     alpha=np.array([1, 0.5, 2])
    ... )
    array([-1.,  2., -6.])

    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([-5, -10]),
    ...     alpha=np.array([2, 3])
    ... )
    array([-10, -30])

    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([-1, -2]),
    ...     alpha=np.array([1, 0])
    ... )
    array([-1,  0])

    >>> parametric_rectified_linear_unit(
    ...     vector=np.array([1, -1]),
    ...     alpha=np.array([0.5, 2])
    ... )
    array([ 1., -2.])
    """

    return np.where(vector > 0, vector, alpha * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
