"""
python/black : True
"""

from __future__ import annotations


def prime_factors(n: int) -> list[int]:
    """
    Returns prime factors of n as a list.

    >>> prime_factors(0)
    []
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(2560)
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 5]
    >>> prime_factors(10**-2)
    []
    >>> prime_factors(0.02)
    []
    >>> x = prime_factors(10**241) # doctest: +NORMALIZE_WHITESPACE
    >>> x == [2]*241 + [5]*241
    True
    >>> prime_factors(10**-354)
    []
    >>> prime_factors('hello')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> prime_factors([1,2,'hello'])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'

    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
