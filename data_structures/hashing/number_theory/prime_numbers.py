#!/usr/bin/env python3
"""
    module to operations with prime numbers
"""


def check_prime(number):
    """
    checks that the given number is a prime number.
    >>> check_prime(1)
    False
    >>> check_prime(5)
    True
    >>> check_prime(7)
    True
    >>> check_prime(11)
    True
    >>> check_prime(8)
    False
    """
    if number < 2:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True


def next_prime(value, factor=1, **kwargs):
    """
    Starting from value * factor, finds the first prime number above/ below.
    If an argument of desc=True is passed, finds the first prime number below.
    >>> next_prime(1)
    2
    >>> next_prime(2, 2)
    5
    >>> next_prime(6)
    7
    >>> next_prime(11)
    13
    >>> next_prime(8, 1, desc=True)
    7
    """
    value = factor * value
    first_value_val = value
    while not check_prime(value):
        value += 1 if not ("desc" in kwargs.keys() and kwargs["desc"] is True) else -1
    if value == first_value_val:
        return next_prime(value + 1, **kwargs)
    return value
