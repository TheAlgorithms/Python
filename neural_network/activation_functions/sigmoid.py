import numpy as np

def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    Implements the sigmoid activation function.

    Parameters:
        vector (np.ndarray): The input array for the sigmoid activation.

    Returns:
        np.ndarray: The input array after applying the sigmoid activation.

    Formula: f(x) = 1 / (1 + exp(-x))

    Examples:
    >>> sigmoid(np.array([2.3, 0.6, -2, -3.8]))
    array([0.90887704, 0.64565631, 0.11920292, 0.02136602])

    >>> sigmoid(np.array([-9.2, -0.3, 0.45, -4.56]))
    array([0.00010713, 0.42555748, 0.61063923, 0.01022693])

    """
    return 1 / (1 + np.exp(-vector))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
