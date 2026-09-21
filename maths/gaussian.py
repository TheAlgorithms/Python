"""
Reference: https://en.wikipedia.org/wiki/Gaussian_function
"""

from numpy import exp, pi, sqrt


def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> float:
    """
    >>> float(gaussian(1))
    0.24197072451914337

    >>> float(gaussian(24))
    3.342714441794458e-126

    >>> float(gaussian(1, 4, 2))
    0.06475879783294587

    >>> float(gaussian(1, 5, 3))
    0.05467002489199788

    Supports NumPy Arrays
    Use numpy.meshgrid with this to generate gaussian blur on images.
    >>> import numpy as np
    >>> x = np.arange(15)
    >>> gaussian(x)
    array([3.98942280e-01, 2.41970725e-01, 5.39909665e-02, 4.43184841e-03,
           1.33830226e-04, 1.48671951e-06, 6.07588285e-09, 9.13472041e-12,
           5.05227108e-15, 1.02797736e-18, 7.69459863e-23, 2.11881925e-27,
           2.14638374e-32, 7.99882776e-38, 1.09660656e-43])

    >>> float(gaussian(15))
    5.530709549844416e-50

    >>> gaussian([1,2, 'string'])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'list' and 'float'

    >>> gaussian('hello world')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'float'

    >>> gaussian(10**234) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    OverflowError: (34, 'Result too large')

    >>> float(gaussian(10**-326))
    0.3989422804014327

    >>> float(gaussian(2523, mu=234234, sigma=3425))
    0.0
    """
    return 1 / sqrt(2 * pi * sigma**2) * exp(-((x - mu) ** 2) / (2 * sigma**2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
