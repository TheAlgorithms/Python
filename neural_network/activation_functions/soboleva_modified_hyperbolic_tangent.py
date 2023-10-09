"""
This script implements the Soboleva Modified Hyperbolic Tangent function.

The function applies the Soboleva Modified Hyperbolic Tangent function
to each element of the vector.

More details about the activation function can be found on:
https://en.wikipedia.org/wiki/Soboleva_modified_hyperbolic_tangent
"""


import numpy as np


def soboleva_modified_hyperbolic_tangent(
    vector: np.ndarray, a_value: float, b_value: float, c_value: float, d_value: float
) -> np.ndarray:
    """
    Implements the Soboleva Modified Hyperbolic Tangent function

    Parameters:
        vector (ndarray): A vector that consists of numeric values
        a_value (float): parameter a of the equation
        b_value (float): parameter b of the equation
        c_value (float): parameter c of the equation
        d_value (float): parameter d of the equation

    Returns:
        vector (ndarray): Input array after applying SMHT function

    >>> vector = np.array([5.4, -2.4, 6.3, -5.23, 3.27, 0.56])
    >>> soboleva_modified_hyperbolic_tangent(vector, 0.2, 0.4, 0.6, 0.8)
    array([ 0.11075085, -0.28236685,  0.07861169, -0.1180085 ,  0.22999056,
            0.1566043 ])
    """

    # Separate the numerator and denominator for simplicity
    # Calculate the numerator and denominator element-wise
    numerator = np.exp(a_value * vector) - np.exp(-b_value * vector)
    denominator = np.exp(c_value * vector) + np.exp(-d_value * vector)

    # Calculate and return the final result element-wise
    return numerator / denominator


if __name__ == "__main__":
    import doctest

    doctest.testmod()
