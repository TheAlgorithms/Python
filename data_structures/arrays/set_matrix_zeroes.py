"""
Set Matrix Zeroes Algorithm
---------------------------
If an element in an m x n matrix is 0, set its entire row and column to 0.

Explanation:
We use the first row and first column as markers to track which rows and
columns should be zeroed, avoiding extra space usage (O(1) space complexity).

References:
https://leetcode.com/problems/set-matrix-zeroes/

Doctest:
>>> matrix = [
...     [1, 1, 1],
...     [1, 0, 1],
...     [1, 1, 1]
... ]
>>> set_matrix_zeroes(matrix)
>>> matrix
[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
"""


def set_matrix_zeroes(matrix: list[list[int]]) -> None:
    """
    Modify the matrix in-place such that if an element is 0,
    its entire row and column are set to 0.

    :param matrix: 2D list of integers
    :return: None (modifies matrix in-place)

    Time Complexity: O(m * n)
    Space Complexity: O(1)
    """
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = 1

    # Step 1: Mark rows and columns that need to be zeroed
    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 2: Update the inner matrix cells
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Handle the first row
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0

    # Step 4: Handle the first column
    if col0 == 0:
        for i in range(rows):
            matrix[i][0] = 0
