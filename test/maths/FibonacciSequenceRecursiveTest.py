# @author Vivek
# @version 1.0
# @since 24-07-2019

import unittest

from maths.FibonacciSequenceRecursive import FibonacciSequenceRecursive


class FibonacciSequenceRecursiveTest(unittest.TestCase):
    fibonacci = FibonacciSequenceRecursive()

    def test_generate_n_1_th_fibonacci_number(self):
        self.assertEqual(0, self.fibonacci.generate_n_1_th_fibonacci_number(0))
        self.assertEqual(1, self.fibonacci.generate_n_1_th_fibonacci_number(1))
        self.assertEqual(1, self.fibonacci.generate_n_1_th_fibonacci_number(2))
        self.assertEqual(2, self.fibonacci.generate_n_1_th_fibonacci_number(3))
        self.assertEqual(3, self.fibonacci.generate_n_1_th_fibonacci_number(4))
        self.assertEqual(5, self.fibonacci.generate_n_1_th_fibonacci_number(5))

    def test_generate_fibonacci_series(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], self.fibonacci.generate_fibonacci_series(10))


if __name__ == '__main__':
    unittest.main()
