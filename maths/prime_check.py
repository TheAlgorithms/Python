"""Prime Check."""

import math
import unittest


def prime_check(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).

    A number is prime if it has exactly two factors: 1 and itself.

    >>> prime_check(0)
    False
    >>> prime_check(1)
    False
    >>> prime_check(2)
    True
    >>> prime_check(3)
    True
    >>> prime_check(27)
    False
    >>> prime_check(87)
    False
    >>> prime_check(563)
    True
    >>> prime_check(2999)
    True
    >>> prime_check(67483)
    False
    """

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or not number % 2:
        # Negatives, 0, 1 and all even numbers are not primes
        return False

    odd_numbers = range(3, int(math.sqrt(number) + 1), 2)
    return not any(not number % i for i in odd_numbers)


class Test(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(prime_check(2))
        self.assertTrue(prime_check(3))
        self.assertTrue(prime_check(5))
        self.assertTrue(prime_check(7))
        self.assertTrue(prime_check(11))
        self.assertTrue(prime_check(13))
        self.assertTrue(prime_check(17))
        self.assertTrue(prime_check(19))
        self.assertTrue(prime_check(23))
        self.assertTrue(prime_check(29))

    def test_not_primes(self):
        self.assertFalse(
            prime_check(-19),
            "Negative numbers are excluded by definition of prime numbers.",
        )
        self.assertFalse(
            prime_check(0),
            "Zero doesn't have any positive factors, primes must have exactly two.",
        )
        self.assertFalse(
            prime_check(1),
            "One only has 1 positive factor, primes must have exactly two.",
        )
        self.assertFalse(prime_check(2 * 2))
        self.assertFalse(prime_check(2 * 3))
        self.assertFalse(prime_check(3 * 3))
        self.assertFalse(prime_check(3 * 5))
        self.assertFalse(prime_check(3 * 5 * 7))


if __name__ == "__main__":
    unittest.main()
