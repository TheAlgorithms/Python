"""
Amicable Numbers are two different numbers such that sum of the proper divisor
of each number is equal to the other number.

Wikipedia link for Reference: https://en.wikipedia.org/wiki/Amicable_numbers
"""
import math


def sum_of_divisor(number: int) -> int:
    """
    Return the sum of all proper divisor of a number.
    >>> sum_of_divisor(20)
    22
    >>> sum_of_divisor(100)
    117
    >>> sum_of_divisor(-1)
    Traceback (most recent call last):
      ...
    ValueError: Number should br greater than zero
    """
    if number <= 0:
        raise ValueError("Number should br greater than zero")
    total = 0
    for divisor in range(2, int(math.sqrt(number) + 1)):
        # Check number is divisible by divisor.
        if number % divisor == 0:
            # If both divisor are the same, add one to the total.
            if divisor == int(number / divisor):
                total += divisor
            # If both divisor are not the same, add both to total.
            else:
                total += (divisor + int(number / divisor))
    # Add 1 to the total because all numbers are divisible by 1
    return total + 1


def is_amicable(x: int, y: int) -> bool:
    """
    Check whether the pair is amicable or not.
    >>> is_amicable(220, 284)
    True
    >>> is_amicable(120, 100)
    False
    >>> is_amicable(6368, 6232)
    True
    """
    if sum_of_divisor(x) != y:
        return False
    return sum_of_divisor(y) == x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
