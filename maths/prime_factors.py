from __future__ import annotations
from math import ceil, sqrt
import time
from typing import Any


def timer(func: callable) -> callable:
    """
    Decorator that measures the execution time of a function.

    :param func: The function to be timed.
    :return: The wrapped function.

    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wraps the given function and measures its execution time.
        
        :param args: Positional arguments for the function.
        :param kwargs: Keyword arguments for the function.
        :return: The result of the wrapped function.
        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds to execute.")
        return result

    return wrapper


@timer
def prime_factors(number: int) -> list[int]:
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
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors


@timer
def primeproduct(num: int) -> list[int]:
    """
    Returns prime factors of a positive integer num as a list.

    >>> primeproduct(868)
    [2, 2, 7, 31]
    >>> primeproduct(9039423423423743)
    [2, 2, 7, 31, 719, 12572216166097]
    >>> primeproduct(0.02)
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: '0.02'
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
    n = int(input("enter number: "))
    primeproduct(n)
    prime_factors(n)
    import doctest
    doctest.NORMALIZE_WHITESPACE

    doctest.testmod()
