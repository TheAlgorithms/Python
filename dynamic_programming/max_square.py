"""
Problem :
Given a matrix of either 0 or 1, find the aera of the largest square composed of 1.
"""


from __future__ import annotations


def max_square(matrix: list[list[int]]) -> int:
    """
    Return the aera of the largest square within matrix.
    matrix is a 2d array with either 0 or 1.
    >>> max_square([[1, 0], [0, 1]])
    1
    >>> max_square([[1, 0, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]])
    4
    >>> max_square([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]])
    9
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    # Max side of squares
    max_side = max((max(row) for row in matrix))

    if len(matrix) == 1 or len(matrix[0]) == 1:
        return max_side ** 2

    # maxsq[i][j] = max square side with bottom right corner at position i, j
    maxsq = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if maxsq[i][j] == 1:
                # If we have a square above and at the left we
                # can construct a bigger square
                maxsq[i][j] = (
                    min(maxsq[i - 1][j], maxsq[i][j - 1], maxsq[i - 1][j - 1])
                    + matrix[i][j]
                )

                max_side = max(max_side, maxsq[i][j])

    return max_side ** 2


def test_max_square(matrix: list[list[int]], expected: int):
    result = max_square(matrix)
    suffix = "" if result == expected else f" != {expected}"
    print(f'> max_square({matrix}) -> {result}{suffix}"')


if __name__ == "__main__":
    # Edge cases
    test_max_square([], 0)
    test_max_square([[]], 0)
    test_max_square([[0]], 0)
    test_max_square([[1]], 1)

    # Usual cases
    test_max_square([[1, 0], [0, 1]], 1)
    test_max_square([[1, 0, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]], 4)
    test_max_square([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]], 9)
