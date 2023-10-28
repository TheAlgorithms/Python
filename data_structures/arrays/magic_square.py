# https://www.codingninjas.com/studio/library/check-if-the-given-matrix-is-a-magic-square-or-not

from typing import List

def is_magic_square(matrix: List[List[int]]) -> bool:
    """
    Check if a given 3x3 matrix is a magic square.

    Parameters:
    - matrix (List[List[int]]): A 3x3 square matrix represented as a list of lists of integers.

    Returns:
    - bool: True if it's a magic square, False otherwise.

    >>> is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    True
    >>> is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    >>> is_magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]])
    False
    """

    # Check if the matrix is a 3x3 square matrix
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        return False

    # Calculate the sum of the first row as the expected sum
    expected_sum = sum(matrix[0])

    # Check rows and columns
    for i in range(3):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(3))
        if row_sum != expected_sum or col_sum != expected_sum:
            return False

    # Check diagonals
    diagonal1_sum = sum(matrix[i][i] for i in range(3))
    diagonal2_sum = sum(matrix[i][2 - i] for i in range(3))
    if diagonal1_sum != expected_sum or diagonal2_sum != expected_sum:
        return False

    return True

if __name__ == "__main__":
    import doctest

    doctest.testmod()



if __name__ == "__main__":
    import doctest

    doctest.testmod()
