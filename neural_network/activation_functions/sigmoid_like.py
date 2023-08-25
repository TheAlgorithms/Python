import numpy as np


def _base_activation(vector: np.ndarray, alpha: float, beta: float) -> np.ndarray:
    """
    Base activation for sigmoid, swish, and SiLU.
    """
    return np.power(vector, alpha) / (1 + np.exp(-beta * vector))


def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    The standard sigmoid function.
    Args:
        vector: (np.ndarray): The input array.
    Returns:
        np.ndarray: The result of the sigmoid activation applied to the input array.
    Examples:
    >>> result = sigmoid(vector=np.array([0, np.log(2), np.log(5)]))
    >>> np.linalg.norm(np.array([0.5, 0.66666667, 0.83333333]) - result) < 10**(-5)
    True
    """
    return _base_activation(vector, 0, 1)


def swish(vector: np.ndarray, beta: float) -> np.ndarray:
    """
    Swish activation: https://arxiv.org/abs/1710.05941v2
    Args:
        vector: (np.ndarray): The input array.
        beta: (float)
    Returns:
        np.ndarray: The result of the swish activation applied to the input array.
    Examples:
    >>> result = swish(np.array([1, 2, 3]), 0)
    >>> np.linalg.norm(np.array([0.5, 1., 1.5]) - result) < 10**(-5)
    True
    >>> result = swish(np.array([0, 1, 2]), np.log(2))
    >>> np.linalg.norm(np.array([0, 0.66666667, 1.6]) - result) < 10**(-5)
    True
    """
    return _base_activation(vector, 1, beta)


def sigmoid_linear_unit(vector: np.ndarray) -> np.ndarray:
    """
    SiLU activation: https://arxiv.org/abs/1606.08415
    Args:
        vector: (np.ndarray): The input array.

    Returns:
        np.ndarray: The result of the sigmoid linear unit applied to the input array.
    Examples:
    >>> result = sigmoid_linear_unit(np.array([0, 1, np.log(2)]))
    >>> np.linalg.norm(np.array([0, 0.7310585, 0.462098]) - result) < 10**(-5)
    True
    """
    return swish(vector, 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
