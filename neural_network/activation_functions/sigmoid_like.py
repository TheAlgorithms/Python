import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    """
    The standard sigmoid function.
    Args:
        vector: (np.ndarray): The input array.
    Returns:
        np.ndarray: The result of the sigmoid activation applied to the input array.

    >>> np.linalg.norm(np.array([0.5, 0.66666667, 0.83333333])
    ... - sigmoid(vector=np.array([0, np.log(2), np.log(5)]))) < 10**(-5)
    True
    """
    return 1 / (1 + np.exp(-vector))


def swish(vector: np.ndarray, beta: float) -> np.ndarray:
    """
    Swish activation: https://arxiv.org/abs/1710.05941v2
    Args:
        vector: (np.ndarray): The input array.
        beta: (float)
    Returns:
        np.ndarray: The result of the swish activation applied to the input array.

    >>> np.linalg.norm(np.array([0.5, 1., 1.5])
    ... - swish(np.array([1, 2, 3]), 0)) < 10**(-5)
    True
    >>> np.linalg.norm(np.array([0, 0.66666667, 1.6])
    ... - swish(np.array([0, 1, 2]), np.log(2))) < 10**(-5)
    True
    """
    return vector / (1 + np.exp(-beta * vector))


def sigmoid_linear_unit(vector: np.ndarray) -> np.ndarray:
    """
    SiLU activation: https://arxiv.org/abs/1606.08415
    Args:
        vector: (np.ndarray): The input array.
    Returns:
        np.ndarray: The result of the sigmoid linear unit applied to the input array.

    >>> np.linalg.norm(np.array([0, 0.7310585, 0.462098])
    ... - sigmoid_linear_unit(np.array([0, 1, np.log(2)]))) < 10**(-5)
    True
    """
    return vector / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
