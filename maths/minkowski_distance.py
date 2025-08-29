def minkowski_distance(
    point_a: list[float],
    point_b: list[float],
    order: int,
) -> float:
    """
    This function calculates the Minkowski distance for a given order between
    two n-dimensional points represented as lists. For the case of order = 1,
    the Minkowski distance degenerates to the Manhattan distance. For
    order = 2, the usual Euclidean distance is obtained.

    https://en.wikipedia.org/wiki/Minkowski_distance

    Note: due to floating point calculation errors the output of this
    function may be inaccurate.

    >>> minkowski_distance([1.0, 1.0], [2.0, 2.0], 1)
    2.0
    >>> minkowski_distance([1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], 2)
    8.0
    >>> import numpy as np
    >>> bool(np.isclose(5.0, minkowski_distance([5.0], [0.0], 3)))
    True
    >>> minkowski_distance([1.0], [2.0], -1)
    Traceback (most recent call last):
        ...
    ValueError: The order must be greater than or equal to 1.
    >>> minkowski_distance([1.0], [1.0, 2.0], 1)
    Traceback (most recent call last):
        ...
    ValueError: Both points must have the same dimension.
    """
    if order < 1:
        raise ValueError("The order must be greater than or equal to 1.")

    if len(point_a) != len(point_b):
        raise ValueError("Both points must have the same dimension.")

    return sum(abs(a - b) ** order for a, b in zip(point_a, point_b)) ** (1 / order)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
