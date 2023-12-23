"""
The maximum submatrix sum problem is the task of finding the maximum sum that can be
obtained from a contiguous submatrix within a given 3D matrix of numbers. For example, given
the matrix
[[-2, 1, -3],
 [4, -1, 2],
 [1, -5, 4]], the contiguous submatrix with the maximum sum
is [[4, -1, 2],
    [1, -5, 4]], so the maximum submatrix sum is 6.

Kadane's algorithm is a simple dynamic programming algorithm that solves the maximum
subarray sum problem in O(n) time and O(1) space. We modify this algorithm to solve the maximum
submatrix sum problem in O(nm^2) time and O(n) space.

Reference: https://www.geeksforgeeks.org/maximum-sum-submatrix/
"""

from collections.abc import Sequence


def max_submatrix_sum(matrix: list[list[str]]) -> int:
    n, m = len(matrix), len(matrix[0])

    answer = -float("inf")
    for i in range(m):
        rows = [0] * n
        for j in range(i, m):
            for k in range(n):
                rows[k] += int(matrix[k][j])

            maxSum = maxSoFar = 0
            for x in rows:
                maxSoFar = max(maxSoFar + x, x)
                maxSum = max(maxSum, maxSoFar)

            answer = max(answer, maxSum)
    return answer


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    matrix = [[-2, 1, -3], [4, -1, 2], [1, -5, 4]]
    print(f"{max_submatrix_sum(matrix) = }")
