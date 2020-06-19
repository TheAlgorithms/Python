from typing import List


def matrix_maximum_path_sum(matrix: List[List[int]]) -> int:
    '''
    Find the maximum sum of values traced by all the paths from top left to bottom
    right in a given matrix

    >>> matrix_maximum_path_sum([[2, 1], [-1, 1], [4, 2]])
    7

    >>> matrix_maximum_path_sum([[2, 1, 4], [2, -1, -3], [3, 2, 1]])
    10
    '''

    # preprocessing the first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    # preprocessing the first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
