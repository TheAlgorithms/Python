import math
import unittest


def primeCheck(number):
    """
    A number is prime if it has exactly two dividers: 1 and itself.
    """
    if number < 2:
        # Negatives, 0 and 1 are not primes
        return False
    if number < 4:
        # 2 and 3 are primes
        return True
    if number % 2 == 0:
        # Even values are not primes
        return False

    # Except 2, all primes are odd. If any odd value divide
    # the number, then that number is not prime.
    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2)
    return not any(number % i == 0 for i in odd_numbers)


class Test(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(primeCheck(2))
        self.assertTrue(primeCheck(3))
        self.assertTrue(primeCheck(5))
        self.assertTrue(primeCheck(7))
        self.assertTrue(primeCheck(11))
        self.assertTrue(primeCheck(13))
        self.assertTrue(primeCheck(17))
        self.assertTrue(primeCheck(19))
        self.assertTrue(primeCheck(23))
        self.assertTrue(primeCheck(29))

    def test_not_primes(self):
        self.assertFalse(primeCheck(-19),
                "Negative numbers are not prime.")
        self.assertFalse(primeCheck(0),
                "Zero doesn't have any divider, primes must have two")
        self.assertFalse(primeCheck(1),
                "One just have 1 divider, primes must have two.")
        self.assertFalse(primeCheck(2 * 2))
        self.assertFalse(primeCheck(2 * 3))
        self.assertFalse(primeCheck(3 * 3))
        self.assertFalse(primeCheck(3 * 5))
        self.assertFalse(primeCheck(3 * 5 * 7))


if __name__ == '__main__':
    unittest.main()

