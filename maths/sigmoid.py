"""
This script demonstrates the implementation of the Sigmoid function.

The sigmoid function maps real-valued inputs to the interval (0, 1).
Its implementation uses separate formulas for positive and negative inputs
to avoid overflow when evaluating large-magnitude values.

Script inspired from its corresponding Wikipedia article:
https://en.wikipedia.org/wiki/Sigmoid_function
"""

import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    Implement the sigmoid function in a numerically stable way.

    Parameters:
        vector (np.ndarray): An array of real-valued inputs.

    Returns:
        np.ndarray: The input array after applying the sigmoid function.

    Raises:
        ValueError: If the input cannot be converted to a float array or
            contains non-finite values.

    Examples:
    >>> sigmoid(np.array([-1.0, 1.0, 2.0]))
    array([0.26894142, 0.73105858, 0.88079708])

    >>> sigmoid(np.array([0.0]))
    array([0.5])

    Large positive and negative values do not overflow:
    >>> sigmoid(np.array([-1000.0, 1000.0]))
    array([0., 1.])

    Scalar arrays are supported:
    >>> sigmoid(np.array(0.0))
    array(0.5)

    Non-numeric and non-finite inputs are rejected:
    >>> sigmoid(np.array(["invalid"]))
    Traceback (most recent call last):
        ...
    ValueError: sigmoid input must be numeric
    >>> sigmoid(np.array([np.inf]))
    Traceback (most recent call last):
        ...
    ValueError: sigmoid input must contain only finite values
    """
    try:
        vector = np.asarray(vector, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError("sigmoid input must be numeric") from exc

    if not np.all(np.isfinite(vector)):
        raise ValueError("sigmoid input must contain only finite values")

    result = np.empty_like(vector)
    positive_mask = vector >= 0

    result[positive_mask] = 1 / (1 + np.exp(-vector[positive_mask]))

    negative_exponentials = np.exp(vector[~positive_mask])
    result[~positive_mask] = negative_exponentials / (1 + negative_exponentials)

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
