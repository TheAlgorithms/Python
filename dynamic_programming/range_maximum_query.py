"""
Range Maximum Query Problem:

    Given an array of integers and q queries,
    For each query find the maximum value in the range [l, r).

    The array is 0-indexed and the queries are 0-indexed.

    More details:
        https://www.geeksforgeeks.org/range-maximum-query-using-sparse-table/
"""
from __future__ import annotations


class RangeMaximumQuery:
    def __init__(self, array: list | tuple | str) -> None:
        """
        Initialize RangeMaximumQuery with given array.

        Parameters:
            array: list[int]

        Example:
        >>> rmq = RangeMaximumQuery([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        """
        self.array = array
        self._preprocess()

    def __len__(self):
        return len(self.array)

    def _preprocess(self) -> None:
        """
        Preprocess the DP array for RMQ in O(n log n).
        ------------------------------
        >>> rmq = RangeMaximumQuery([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> rmq.log[7]
        2
        >>> rmq.log[8]
        3
        >>> rmq.log[9]
        3
        >>> rmq.dp[0][0]
        1
        >>> rmq.dp[0][9]
        10
        >>> rmq.dp[1][0]
        2
        >>> rmq.dp[1][9]
        10
        >>> rmq.dp[1][8]
        10
        """
        # Fill logarithm array for O(1) usage
        self.log = [0] * (len(self) + 1)
        for i in range(2, len(self) + 1):
            self.log[i] = self.log[i >> 1] + 1
        log_size = self.log[len(self)] + 1

        # Create empty DP 2D array with size log(n) x n
        self.dp = [[0] * len(self) for _ in range(log_size)]
        for i in range(self.size):
            self.dp[0][i] = self.array[i]
        for p in range(1, log_size):
            for i in range(self.size):
                if i + (1 << p) <= self.size:
                    self.dp[p][i] = max(
                        self.dp[p - 1][i], self.dp[p - 1][i + (1 << (p - 1))]
                    )
                else:
                    self.dp[p][i] = self.dp[p - 1][i]

    def query(self, left: int, right: int) -> int:
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
        """
        p = self.log[right - left]  # Find the logarithm of the size of range
        return max(self.dp[p][left], self.dp[p][right - (1 << p)])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
