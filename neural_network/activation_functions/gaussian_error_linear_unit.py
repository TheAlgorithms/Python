import numpy as np

"""
The GELU (Gaussian Error Linear Unit) activation function
is a smooth, non-linear function used in neural networks.
For more details: https://en.wikipedia.org/wiki/Gaussian_error_linear_unit
"""


def gelu(vector: np.ndarray) -> np.ndarray:
    """
    Implements the GELU (Gaussian Error Linear Unit) activation function.

    Parameters:
        vector (np.ndarray): The input array for GELU activation.

    Returns:
        np.ndarray: The input array after applying the GELU activation.

    Formula: GELU(x) = 0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3)))

    Examples:
    >>> gelu(np.array([2.3, 0.6, -2, -3.8]))
    array([ 2.27567297e+00,  4.35415199e-01, -4.54023059e-02, -1.76119217e-04])

    >>> gelu(np.array([-9.2, -0.3, 0.45, -4.56]))
    array([-0.00000000e+00, -1.14629076e-01,  3.03128456e-01, -3.63404370e-06])
    """
    return (
        0.5
        * vector
        * (1 + np.tanh(np.sqrt(2 / np.pi) * (vector + 0.044715 * vector**3)))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
