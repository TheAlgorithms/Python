"""
The Harmonic Mean of n numbers is defined as n divided by the sum of the
reciprocals of those numbers. It is used to calculate average rates and ratios.
https://en.wikipedia.org/wiki/Harmonic_mean
"""

from typing import Union


def compute_harmonic_mean(*args: Union[int, float]) -> float:
    """
    Return the harmonic mean of the argument numbers.

    The harmonic mean is particularly useful for rates (e.g., speed, density).

    >>> compute_harmonic_mean(1, 2, 4)
    1.7142857142857142
    >>> compute_harmonic_mean(2, 4)
    2.6666666666666665
    >>> compute_harmonic_mean('a', 4)
    Traceback (most recent call last):
        ...
    TypeError: Not a Number
    >>> compute_harmonic_mean(1, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot compute harmonic mean with zero values
    >>> compute_harmonic_mean(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: Cannot compute harmonic mean with non-positive values
    >>> compute_harmonic_mean()
    Traceback (most recent call last):
        ...
    ValueError: At least one number is required
    >>> compute_harmonic_mean(4, 4, 4)
    4.0
    >>> compute_harmonic_mean(1, 2)
    1.3333333333333333
    """
    if len(args) == 0:
        raise ValueError("At least one number is required")

    reciprocal_sum = 0
    for number in args:
        if not isinstance(number, (int, float)):
            raise TypeError("Not a Number")
        if number == 0:
            raise ValueError("Cannot compute harmonic mean with zero values")
        if number < 0:
            raise ValueError("Cannot compute harmonic mean with non-positive values")
        reciprocal_sum += 1 / number

    return len(args) / reciprocal_sum


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="compute_harmonic_mean")
    print(compute_harmonic_mean(1, 2, 4))
