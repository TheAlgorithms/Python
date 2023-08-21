from __future__ import annotations
from math import ceil, sqrt
from typing import Any


def prime_factors(num: int) -> list[int]:
    """
    Returns prime factors of a given number as a list.
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
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors


def primeproduct(num: int) -> list[int]:
    """
    Returns prime factors of a positive integer num as a list.
    2 is only even prime so special while loop to handle it.
    Skipping other even numbers.
    Taking root n approach for getting prime number.

    >>> primeproduct(868)
    [2, 2, 7, 31]
    >>> primeproduct(9039423423423743)
    [7, 719, 1796030880871]
    >>> primeproduct(435345234543252)
    [2, 2, 3, 3, 3, 11, 3119, 5171, 22721]
    >>> primeproduct(-2342)
    []

    """
    if num <= 1:
        return []

    prime_factors: list[int] = []
    while num > 1:
        if len(prime_factors) >= 1 and prime_factors[-1] % num == 0:
            prime_factors.append(prime_factors[-1])

        else:
            sq = ceil(sqrt(num))
            flag = 0

            if prime_factors != []:
                for i in range(prime_factors[-1], sq + 1, 2):
                    if num % i == 0:
                        num = num // i
                        prime_factors.append(i)
                        flag = 1
                        break

            else:
                while num % 2 == 0:
                    num = num // 2
                    prime_factors.append(2)

                for i in range(3, sq + 1, 2):
                    if num % i == 0:
                        num = num // i
                        prime_factors.append(i)
                        flag = 1
                        break

            if not flag and num > 1:
                prime_factors.append(num)
                num = 1
                break

    return prime_factors


if __name__ == "__main__":
    n = int(input("enter number: ").strip())
    primeproduct(n)
    prime_factors(n)
    import doctest

    doctest.testmod()
