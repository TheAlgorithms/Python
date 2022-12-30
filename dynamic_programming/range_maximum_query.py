"""
Range Maximum Query Problem:

    Given an array of integers and q queries,
    For each query find the maximum value in the range [l, r).

    The array is 0-indexed and the queries are 0-indexed.

    More details:
        https://www.geeksforgeeks.org/range-maximum-query-using-sparse-table/
"""
from __future__ import annotations

import typing


class RangeMaximumQuery:
    def __init__(self, array: typing.Sequence[int | float]) -> None:
        """
        Initialize RangeMaximumQuery with given array.

        Example:
        >>> rmq = RangeMaximumQuery([1, 3, 5, 7, 9, 11])
        """
        self.array = array

        self.logarithm_array: list[int] = []
        self._preprocess_logarithm()

        self.maximum_array: list[list[int | float]] = []
        self._preprocess_maximum()

    def __len__(self) -> int:
        """
        Returns:
            the length of the array
        ------------------------------------
        >>> len(RangeMaximumQuery([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        10
        >>> len(RangeMaximumQuery([]))
        0
        >>> len(RangeMaximumQuery((1, 3, 5.9)))
        3
        """
        return len(self.array)

    def _preprocess_logarithm(self) -> None:
        """
        Preprocess the logarithm array from 1 to n for later O(1) usage.
        ------------------------------
        >>> rmq = RangeMaximumQuery([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> rmq.logarithm_array[7]
        2
        >>> rmq.logarithm_array[8]
        3
        >>> rmq.logarithm_array[9]
        3
        """
        size = len(self) + 1
        self.logarithm_array = [0] * size
        for i in range(2, size):
            self.logarithm_array[i] = self.logarithm_array[i >> 1] + 1

    def _preprocess_maximum(self) -> None:
        """
        Preprocess the Maximum array for RMQ in O(n log n) using Dynamic Programming.

        maximum_array[i][j] stores the maximum value in the range [j, j + 2^i)
        ------------------------------
        >>> rmq = RangeMaximumQuery([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> rmq.maximum_array[0][0]
        1
        >>> rmq.maximum_array[0][9]
        10
        >>> rmq.maximum_array[1][0]
        2
        >>> rmq.maximum_array[1][9]
        10
        >>> rmq.maximum_array[1][8]
        10
        """
        size = len(self)
        logarithm_of_size = self.logarithm_array[size] + 1

        # Create empty Maximum 2D array with size log(n) x n
        self.maximum_array = [[0] * size for _ in range(logarithm_of_size)]
        for i in range(size):
            self.maximum_array[0][i] = self.array[i]
        for p in range(1, logarithm_of_size):
            for i in range(size):
                if i + (1 << p) <= size:
                    self.maximum_array[p][i] = max(
                        self.maximum_array[p - 1][i],
                        self.maximum_array[p - 1][i + (1 << (p - 1))],
                    )
                else:
                    self.maximum_array[p][i] = self.maximum_array[p - 1][i]

    def query(self, left: int, right: int) -> int | float:
        """
        Finds the maximum value in the range [left, right) in O(1).

        Parameters:
            left: int, the left index of the range (inclusive)
            right: int, the right index of the range (exclusive)

        Returns:
            int, the maximum value in the range [left, right)

        Example:
        >>> array = [1, 3, 5, 7, 9, 11]
        >>> queries = [(0, 1), (1, 4), (0, 5), (2, 3), (0, 6)]
        >>> rmq = RangeMaximumQuery(array)
        >>> for l, r in queries:
        ...     print(rmq.query(l, r))
        1
        7
        9
        5
        11
        >>> rmq.query(0, 0)
        Traceback (most recent call last):
        ValueError: Invalid range
        >>> rmq.query(5, 2)
        Traceback (most recent call last):
        ValueError: Invalid range
        >>> rmq.query(-1, 2)
        Traceback (most recent call last):
        ValueError: Range out of bounds
        >>> rmq.query(2, 7)
        Traceback (most recent call last):
        ValueError: Range out of bounds
        >>> rmq.query(-1, 100)
        Traceback (most recent call last):
        ValueError: Range out of bounds
        """
        if left >= right:
            raise ValueError("Invalid range")
        if left < 0 or right > len(self):
            raise ValueError("Range out of bounds")

        # Find the logarithm of the size of range
        p = self.logarithm_array[right - left]

        return max(self.maximum_array[p][left], self.maximum_array[p][right - (1 << p)])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
