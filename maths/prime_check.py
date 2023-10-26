"""Prime Check."""

import math
import unittest

import pytest


def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).

    A number is prime if it has exactly two factors: 1 and itself.

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(87)
    False
    >>> is_prime(563)
    True
    >>> is_prime(2999)
    True
    >>> is_prime(67483)
    False
    >>> is_prime(16.1)
    Traceback (most recent call last):
        ...
    ValueError: is_prime() only accepts positive integers
    >>> is_prime(-4)
    Traceback (most recent call last):
        ...
    ValueError: is_prime() only accepts positive integers
    """

    # precondition
    if not isinstance(number, int) or not number >= 0:
        raise ValueError("is_prime() only accepts positive integers")

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        # Negatives, 0, 1, all even numbers, all multiples of 3 are not primes
        return False

    # All primes number are in format of 6k +/- 1
    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


class Test(unittest.TestCase):
    def test_primes(self):
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(5)
        assert is_prime(7)
        assert is_prime(11)
        assert is_prime(13)
        assert is_prime(17)
        assert is_prime(19)
        assert is_prime(23)
        assert is_prime(29)

    def test_not_primes(self):
        with pytest.raises(ValueError):
            is_prime(-19)
        assert not is_prime(
            0
        ), "Zero doesn't have any positive factors, primes must have exactly two."
        assert not is_prime(
            1
        ), "One only has 1 positive factor, primes must have exactly two."
        assert not is_prime(2 * 2)
        assert not is_prime(2 * 3)
        assert not is_prime(3 * 3)
        assert not is_prime(3 * 5)
        assert not is_prime(3 * 5 * 7)


if __name__ == "__main__":
    unittest.main()
