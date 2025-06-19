import unittest
from recursion.factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_valid_inputs(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_invalid_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
