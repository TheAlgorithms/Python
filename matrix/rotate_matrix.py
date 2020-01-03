"""
In this problem, we want to rotate the matrix elements by 90, 180, 270 (counterclockwise)
Discussion in stackoverflow:
https://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array
"""


def make_matrix(row_size: int = 4) -> [[int]]:
    """
    >>> make_matrix()
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    >>> make_matrix(1)
    [[1]]
    >>> make_matrix(-2)
    [[1, 2], [3, 4]]
    >>> make_matrix(3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> make_matrix() == make_matrix(4)
    True
    """
    row_size = abs(row_size) or 4
    return [[1 + x + y * row_size for x in range(row_size)] for y in range(row_size)]


def rotate_90(matrix: [[]]) -> [[]]:
    """
    >>> rotate_90(make_matrix())
    [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
    >>> rotate_90(make_matrix()) == transpose(reverse_column(make_matrix()))
    True
    """

    return reverse_row(transpose(matrix))
    # OR.. transpose(reverse_column(matrix))


def rotate_180(matrix: [[]]) -> [[]]:
    """
    >>> rotate_180(make_matrix())
    [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
    >>> rotate_180(make_matrix()) == reverse_column(reverse_row(make_matrix()))
    True
    """

    return reverse_row(reverse_column(matrix))
    # OR.. reverse_column(reverse_row(matrix))


def rotate_270(matrix: [[]]) -> [[]]:
    """
    >>> rotate_270(make_matrix())
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    >>> rotate_270(make_matrix()) == transpose(reverse_row(make_matrix()))
    True
    """

    return reverse_column(transpose(matrix))
    # OR.. transpose(reverse_row(matrix))


def transpose(matrix: [[]]) -> [[]]:
    matrix[:] = [list(x) for x in zip(*matrix)]
    return matrix


def reverse_row(matrix: [[]]) -> [[]]:
    matrix[:] = matrix[::-1]
    return matrix


def reverse_column(matrix: [[]]) -> [[]]:
    matrix[:] = [x[::-1] for x in matrix]
    return matrix


def print_matrix(matrix: [[]]) -> [[]]:
    for i in matrix:
        print(*i)


if __name__ == "__main__":
    matrix = make_matrix()
    print("\norigin:\n")
    print_matrix(matrix)
    print("\nrotate 90 counterclockwise:\n")
    print_matrix(rotate_90(matrix))

    matrix = make_matrix()
    print("\norigin:\n")
    print_matrix(matrix)
    print("\nrotate 180:\n")
    print_matrix(rotate_180(matrix))

    matrix = make_matrix()
    print("\norigin:\n")
    print_matrix(matrix)
    print("\nrotate 270 counterclockwise:\n")
    print_matrix(rotate_270(matrix))
