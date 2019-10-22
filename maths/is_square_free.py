"""
References: wikipedia:square free number
python/black : True
flake8 : True
"""
from typing import List


def is_square_free(factors: List[int]) -> bool:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes a list of prime factors as input.
    returns True if the factors are square free.
    >>> is_square_free([1, 1, 2, 3, 4])
    False
    
    These are wrong but should return some value
    it simply checks for repition in the numbers.
    >>> is_square_free([1, 3, 4, 'sd', 0.0])
    True
    
    >>> is_square_free([1, 0.5, 2, 0.0])
    True
    >>> is_square_free([1, 2, 2, 5])
    False
    >>> is_square_free('asd')
    True
    >>> is_square_free(24)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    return len(set(factors)) == len(factors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
