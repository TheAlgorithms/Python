"""
This is the implementation of inter_quartile range (IQR).

function takes the list of numeric values as input
and return the IQR as output.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Interquartile_range
"""

import numpy as np


def find_median(x: np.array) -> float:
    """
    This is the implementation of median.
    :param x: The list of numeric values
    :return: Median of the list
    >>> find_median(x=np.array([1,2,2,3,4]))
    2

    >>> find_median(np.array([1,2,2,3,4,4]))
    2.5


    """
    length = len(x)
    if length % 2:
        return x[length // 2]
    return float((x[length // 2] + x[(length // 2) - 1]) / 2)


def inter_quartile_range(x: np.array) -> float:
    """
    This is the implementation of inter_quartile
    range for a list of numeric.
    :param x: The list of data point
    :return: Inter_quartile range

    >>> inter_quartile_range(x=np.array([4,1,2,3,2]))
    2.0

    >>> inter_quartile_range(x=np.array([25,32,49,21,37,43,27,45,31]))
    18.0
    """
    length = len(x)
    if length == 0:
        raise ValueError
    x.sort()
    q1 = find_median(x[0: length // 2])
    half_length = (length // 2) + 1 if length % 2 else length // 2
    q3 = find_median(x[half_length:length])
    return q3 - q1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
