"""
== Liouville Lambda Function ==
The Liouville Lambda function, denoted by λ(n)
and λ(n) is 1 if n is the product of an even number of prime numbers,
and -1 if it is the product of an odd number of primes.

https://en.wikipedia.org/wiki/Liouville_function
"""

# Author : Akshay Dubey (https://github.com/itsAkshayDubey)
from maths.prime_factors import prime_factors


def liouville_lambda(number: int) -> int:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes an integer number as input.
    returns 1 if n has even number of prime factors and -1 otherwise.
    >>> liouville_lambda(10)
    1
    >>> liouville_lambda(11)
    -1
    >>> liouville_lambda(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be non-zero
    >>> liouville_lambda(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be positive
    >>> liouville_lambda(11.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=11.0] must be an integer
    """
    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] must be an integer")
    if number < 0:
        raise ValueError("Input must be positive")
    if number == 0:
        raise ValueError("Input must be non-zero")
    if len(prime_factors(number)) % 2 == 0:
        return 1
    else:
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
