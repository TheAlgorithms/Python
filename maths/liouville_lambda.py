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
    This functions takes an integer number as input.
    returns 1 if n has even number of prime factors and -1 otherwise.
    >>> liouville_lambda(10)
    1
    >>> liouville_lambda(11)
    -1
    >>> liouville_lambda(0)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer
    >>> liouville_lambda(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a positive integer
    >>> liouville_lambda(11.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=11.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        raise ValueError("Input must be a positive integer")
    return -1 if len(prime_factors(number)) % 2 else 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
