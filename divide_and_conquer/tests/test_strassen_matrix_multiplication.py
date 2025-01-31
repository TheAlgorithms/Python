import unittest
from strassen_matrix_multiplication import split_matrix


class TestSplitMatrix(unittest.TestCase):

    def test_4x4_matrix(self):
        matrix = [
            [4, 3, 2, 4],
            [2, 3, 1, 1],
            [6, 5, 4, 3],
            [8, 4, 1, 6]
        ]
        expected = (
            [[4, 3], [2, 3]],
            [[2, 4], [1, 1]],
            [[6, 5], [8, 4]],
            [[4, 3], [1, 6]]
        )
        self.assertEqual(split_matrix(matrix), expected)

    def test_8x8_matrix(self):
        matrix = [
            [4, 3, 2, 4, 4, 3, 2, 4],
            [2, 3, 1, 1, 2, 3, 1, 1],
            [6, 5, 4, 3, 6, 5, 4, 3],
            [8, 4, 1, 6, 8, 4, 1, 6],
            [4, 3, 2, 4, 4, 3, 2, 4],
            [2, 3, 1, 1, 2, 3, 1, 1],
            [6, 5, 4, 3, 6, 5, 4, 3],
            [8, 4, 1, 6, 8, 4, 1, 6]
        ]
        expected = (
            [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
            [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
            [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
            [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]]
        )
        self.assertEqual(split_matrix(matrix), expected)

    def test_invalid_odd_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        with self.assertRaises(Exception):
            split_matrix(matrix)

    def test_invalid_non_square_matrix(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        with self.assertRaises(Exception):
            split_matrix(matrix)


if __name__ == "__main__":
    unittest.main()
