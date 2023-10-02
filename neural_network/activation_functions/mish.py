import numpy as np

"""
Mish is a non-monotonic activation
function defined as
f(x) = x * tanh(softplus(x)).
It smoothly combines the characteristics
of ReLU and Sigmoid functions.
The "softplus" function is a smooth
approximation of the ReLU.

For more details:
https://paperswithcode.com/method/mish
"""


def mish(vector: np.ndarray) -> np.ndarray:
    """
    Implements the Mish activation function.

    Parameters:
        vector (np.ndarray): The input array for Mish activation.

    Returns:
        np.ndarray: The input array after applying the Mish activation.

    Formula: Mish(x) = x * tanh(softplus(x))

    Use Case & Importance:
    - Mish is a smooth, non-monotonic activation function
    that combines the benefits of ReLU and Sigmoid.
    - It can help with training deep neural networks by
    mitigating the vanishing gradient problem.

    Examples:
    >>> mish(np.array([2.3, 0.6, -2, -3.8]))
    array([ 2.26211893,  0.46613649, -0.25250148, -0.08405831])

    >>> mish(np.array([-9.2, -0.3, 0.45, -4.56]))
    array([-0.00092952, -0.15113318,  0.33152014, -0.04745745])
    """
    return vector * np.tanh(np.log(1 + np.exp(vector)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
