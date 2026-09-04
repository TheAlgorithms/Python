"""
This script demonstrates the implementation of the Softmax function.

It takes as input a vector of K real numbers and normalizes it into a
probability distribution consisting of K probabilities proportional
to the exponentials of the input numbers. After applying softmax,
the elements of the vector always sum up to 1.

Script inspired by its corresponding Wikipedia article:
https://en.wikipedia.org/wiki/Softmax_function
"""

import numpy as np
from numpy.exceptions import AxisError


def softmax(vector: np.ndarray, axis: int = -1) -> np.ndarray:
    """
    Implements the softmax function.

    Parameters:
        vector (np.ndarray | list | tuple): A numpy array of shape (1, n)
            consisting of real values or a similar list/tuple.
        axis (int, optional): Axis along which to compute softmax.
            Default is -1.

    Returns:
        np.ndarray: The input numpy array after applying softmax.

    The softmax vector adds up to one. We need to ceil to mitigate precision.

    >>> float(np.ceil(np.sum(softmax([1, 2, 3, 4]))))
    1.0

    >>> vec = np.array([5, 5])
    >>> softmax(vec)
    array([0.5, 0.5])

    >>> softmax([0])
    array([1.])
    """
    # Convert input to numpy array of floats
    vector = np.asarray(vector, dtype=float)

    # Handle empty input
    if vector.size == 0:
        raise ValueError("softmax input must be non-empty")

    # Validate axis
    ndim = vector.ndim
    if axis >= ndim or axis < -ndim:
        error_message = f"axis {axis} is out of bounds for array of dimension {ndim}"
        raise AxisError(error_message)
    # Subtract max for numerical stability
    vector_max = np.max(vector, axis=axis, keepdims=True)
    exponent_vector = np.exp(vector - vector_max)

    # Sum of exponentials along the axis
    sum_of_exponents = np.sum(exponent_vector, axis=axis, keepdims=True)

    # Divide each exponent by the sum along the axis
    softmax_vector = exponent_vector / sum_of_exponents
    return softmax_vector


if __name__ == "__main__":
    # Single value
    print(softmax((0,)))
    # Vector
    print(softmax([1, 2, 3]))
    # Matrix along last axis
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    print("Softmax along last axis:\n", softmax(mat))
    # Matrix along axis 0
    print("Softmax along axis 0:\n", softmax(mat, axis=0))
