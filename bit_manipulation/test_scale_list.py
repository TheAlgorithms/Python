import unittest
from bit_manipulation.scale_list import scale_list


class TestScaleList(unittest.TestCase):
    def test_scaling(self):
        self.assertEqual(scale_list([1, 2, 3], 2), [2, 4, 6])
        self.assertEqual(scale_list([-1, -2], 3), [-3, -6])
        self.assertEqual(scale_list([0, 1], 0), [0, 0])


if __name__ == "__main__":
    unittest.main()
