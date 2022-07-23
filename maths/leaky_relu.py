"""
This algorithm implements the leaky rectified linear algorithm (LReLU).

LReLU is at times used as a substitute to ReLU because it fixes the dying ReLU problem.
This is done by adding a slight slope to the negative portion of the function.
The default value for the slope is 0.01.
The new slope is determined before the network is trained.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
"""
from __future__ import annotations


def leaky_relu(
    vector: float | list[float], negative_slope: float = 0.01
) -> float | list[float]:
    """
    Implements the leaky rectified linear activation function

    :param vector: The float or list of floats to apply the algorithm to
    :param slope: The multiplier that is applied to every negative value in the list
    :return: The modified value or list of values after applying LReLU

    >>> leaky_relu([-5])
    [-0.05]
    >>> leaky_relu([-2, 0.8, -0.3])
    [-0.02, 0.8, -0.003]
    >>> leaky_relu(-3.0)
    -0.03
    >>> leaky_relu(2)
    Traceback (most recent call last):
      ...
    ValueError: leaky_relu() only accepts floats or a list of floats for vector
    """
    if isinstance(vector, int):
        raise ValueError(
            "leaky_relu() only accepts floats or a list of floats for vector"
        )
    if not isinstance(negative_slope, float):
        raise ValueError("leaky_relu() only accepts a float value for negative_slope")

    if isinstance(vector, float):
        if vector < 0:
            return vector * negative_slope
        return vector

    for index, value in enumerate(vector):
        if value < 0:
            vector[index] = value * negative_slope

    return vector


if __name__ == "__main__":
    import doctest

    doctest.testmod()
