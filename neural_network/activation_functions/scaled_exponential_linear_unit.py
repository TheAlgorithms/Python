"""
Implements the Scaled Exponential Linear Unit or SELU function.
The function takes a vector of K real numbers and two real numbers
alpha(default = 1.6732) & lambda (default = 1.0507) as input and
then applies the SELU function to each element of the vector.
SELU is a self-normalizing activation function. It is a variant
of the ELU. The main advantage of SELU is that we can be sure
that the output will always be standardized due to its
self-normalizing behavior. That means there is no need to
include Batch-Normalization layers.
References :
https://iq.opengenus.org/scaled-exponential-linear-unit/
"""

import numpy as np


def scaled_exponential_linear_unit(
    vector: np.ndarray, alpha: float = 1.6732, lambda_: float = 1.0507
) -> np.ndarray:
    """
    Applies the Scaled Exponential Linear Unit function to each element of the vector.
    Parameters :
        vector : np.ndarray
        alpha : float (default = 1.6732)
        lambda_ : float (default = 1.0507)

    Returns : np.ndarray
    Formula : f(x) = lambda_ * x if x > 0
                     lambda_ * alpha * (e**x - 1) if x <= 0
    Examples :
    >>> scaled_exponential_linear_unit(vector=np.array([1.3, 3.7, 2.4]))
    array([1.36591, 3.88759, 2.52168])

    >>> scaled_exponential_linear_unit(vector=np.array([1.3, 4.7, 8.2]))
    array([1.36591, 4.93829, 8.61574])
    """
    return lambda_ * np.where(vector > 0, vector, alpha * (np.exp(vector) - 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
