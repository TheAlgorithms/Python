"""
A Sophie Germain prime is any prime p, where 2p + 1 is also prime.
The second number, 2p + 1 is called a safe prime.

Examples of Germain primes include: 2, 3, 5, 11, 23

Their corresponding safe primes: 5, 7, 11, 23, 47
https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes
"""

from maths.prime_check import is_prime


def is_germain_prime(number: int) -> bool:
    """Checks if input number and 2*number + 1 are prime.

    >>> is_germain_prime(3)
    True
    >>> is_germain_prime(11)
    True
    >>> is_germain_prime(4)
    False
    >>> is_germain_prime(23)
    True
    >>> is_germain_prime(13)
    False
    >>> is_germain_prime(20)
    False
    >>> is_germain_prime('abc')
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a positive integer. Input value: abc
    """
    if not isinstance(number, int) or number < 1:
        msg = f"Input value must be a positive integer. Input value: {number}"
        raise TypeError(msg)

    return is_prime(number) and is_prime(2 * number + 1)


def is_safe_prime(number: int) -> bool:
    """Checks if input number and (number - 1)/2 are prime.
    The smallest safe prime is 5, with the Germain prime is 2.

    >>> is_safe_prime(5)
    True
    >>> is_safe_prime(11)
    True
    >>> is_safe_prime(1)
    False
    >>> is_safe_prime(2)
    False
    >>> is_safe_prime(3)
    False
    >>> is_safe_prime(47)
    True
    >>> is_safe_prime('abc')
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a positive integer. Input value: abc
    """
    if not isinstance(number, int) or number < 1:
        msg = f"Input value must be a positive integer. Input value: {number}"
        raise TypeError(msg)

    return (number - 1) % 2 == 0 and is_prime(number) and is_prime((number - 1) // 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
