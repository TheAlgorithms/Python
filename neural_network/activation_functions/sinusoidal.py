"""
Sinusoidal activation function.

Reference:
https://arxiv.org/abs/2006.09661
"""

import numpy as np


def sinusoidal(vector: np.ndarray, omega: float = 1.0) -> np.ndarray:
    """
    Apply the sinusoidal activation element-wise.

    Formula: f(x) = sin(omega * x)

    >>> sinusoidal(np.array([0, np.pi / 2, np.pi])).round(5)
    array([0., 1., 0.])

    >>> sinusoidal(np.array([0, np.pi / 4]), omega=2).round(5)
    array([0., 1.])

    >>> sinusoidal(np.array([])).size
    0

    >>> sinusoidal(np.array([[0, 1], [2, 3]])).shape
    (2, 2)
    """
    return np.sin(omega * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
