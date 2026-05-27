"""
Image style reconstruction with Gram matrices.

https://arxiv.org/pdf/1603.08155#page=7&zoom=auto,-294,3
"""

import numpy as np


def gram_matrix(mat: np.ndarray) -> np.ndarray:
    """
    Returns the Gram (Gramian) matrix of an image.

    :param mat: matrix of shape (C, H, W); C = color channels, H = height, W = width.
    :type mat: np.ndarray
    :return: matrix of shape (C, C).
    :rtype: np.ndarray

    Examples
    --------
    >>> gram_matrix(np.ones((2,5,5)))
    array([[0.5, 0.5],
           [0.5, 0.5]])
    >>> gram_matrix(np.ones((3,5,5)))
    array([[0.33333333, 0.33333333, 0.33333333],
           [0.33333333, 0.33333333, 0.33333333],
           [0.33333333, 0.33333333, 0.33333333]])
    >>> gram_matrix(np.ones((3,5,5))).shape
    (3, 3)
    """
    color, height, width = mat.shape
    vec = mat.reshape(color, height * width)
    gram = vec @ vec.T
    return gram / (color * height * width)


def gram_loss(input_features: np.ndarray, reference_features: np.ndarray) -> np.float64:
    """
    Calculates the squared Frobenius norm of the difference between
    the Gram matrices of the input and reference image.

    :param input_features: Feature map of shape (C, H, W)
    :type input_features: np.ndarray
    :param reference_features: Feature map of shape (C, H, W)
    :type reference_features: np.ndarray
    :return: Gram loss between the two feature maps.
    :rtype: float64

    Examples
    --------
    >>> a = np.random.randn(3,5,5)
    >>> gram_loss(a, a)
    np.float64(0.0)
    >>> a = np.zeros((3,5,5))
    >>> b = np.ones((3,5,5))
    >>> gram_loss(a, b)
    np.float64(1.0)
    """
    input_gram = gram_matrix(input_features)
    reference_gram = gram_matrix(reference_features)
    return np.sum(np.square(input_gram - reference_gram)).astype(np.float64)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
