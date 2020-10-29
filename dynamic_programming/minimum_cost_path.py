# Youtube Explanation: https://www.youtube.com/watch?v=lBRtnuxg-gU

from __future__ import annotations


def minimum_cost_path(matrix: list[list[int]]) -> int:
    """
    Find the minimum cost traced by all possible paths from top left to bottom right in
    a given matrix

    >>> minimum_cost_path([[2, 1], [3, 1], [4, 2]])
    6

    >>> minimum_cost_path([[2, 1, 4], [2, 1, 3], [3, 2, 1]])
    7
    """

    # preprocessing the first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    # preprocessing the first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    # updating the path cost for current position
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
