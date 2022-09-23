"""Prime Check."""

import math
import unittest


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
    """

    # precondition
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' must been an int and positive"

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
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))

    def test_not_primes(self):
        with self.assertRaises(AssertionError):
            is_prime(-19)
        self.assertFalse(
            is_prime(0),
            "Zero doesn't have any positive factors, primes must have exactly two.",
        )
        self.assertFalse(
            is_prime(1),
            "One only has 1 positive factor, primes must have exactly two.",
        )
        self.assertFalse(is_prime(2 * 2))
        self.assertFalse(is_prime(2 * 3))
        self.assertFalse(is_prime(3 * 3))
        self.assertFalse(is_prime(3 * 5))
        self.assertFalse(is_prime(3 * 5 * 7))


if __name__ == "__main__":
    unittest.main()
