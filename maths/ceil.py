"""
https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
"""
import unittest

def ceil(x: float) -> int:
    """
    Return the ceiling of x as an Integral.

    :param x: the number
    :return: the smallest integer >= x.

    >>> import math
    >>> all(ceil(n) == math.ceil(n) for n
    ...     in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000))
    True

    >>> ceil("not_a_number")  # Add a test case with non-numeric input
    Traceback (most recent call last):
        ...
    ValueError: Input must be a float or integer
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a float or integer")
    
    return int(x) if x - int(x) <= 0 else int(x) + 1


class TestCeil(unittest.TestCase):

    def test_ceil_float(self):
        self.assertEqual(ceil(1.5), 2)

    def test_ceil_integer(self):
        self.assertEqual(ceil(5), 5)

    def test_ceil_negative(self):
        self.assertEqual(ceil(-1.5), -1)

    def test_ceil_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            ceil("not_a_number")
        self.assertEqual("Input must be a float or integer", str(context.exception))


if __name__ == "__main__":
    import doctest
    unittest.main()
    doctest.testmod()