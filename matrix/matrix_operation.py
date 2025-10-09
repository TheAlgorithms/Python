"""
Functions for 2D matrix operations
"""

from __future__ import annotations

from typing import Any


def add(*matrix_s: list[list[int]]) -> list[list[int]]:
    """
    >>> add([[1,2],[3,4]],[[2,3],[4,5]])
    [[3, 5], [7, 9]]
    >>> add([[1.2,2.4],[3,4]],[[2,3],[4,5]])
    [[3.2, 5.4], [7, 9]]
    >>> add([[1, 2], [4, 5]], [[3, 7], [3, 4]], [[3, 5], [5, 7]])
    [[7, 14], [12, 16]]
    >>> add([3], [4, 5])
    Traceback (most recent call last):
      ...
    TypeError: Expected a matrix, got int/list instead
    """
    if all(_check_not_integer(m) for m in matrix_s):
        for i in matrix_s[1:]:
            _verify_matrix_sizes(matrix_s[0], i)
        return [[sum(t) for t in zip(*m)] for m in zip(*matrix_s)]
    raise TypeError("Expected a matrix, got int/list instead")


def subtract(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    """
    >>> subtract([[1,2],[3,4]],[[2,3],[4,5]])
    [[-1, -1], [-1, -1]]
    >>> subtract([[1,2.5],[3,4]],[[2,3],[4,5.5]])
    [[-1, -0.5], [-1, -1.5]]
    >>> subtract([3], [4, 5])
    Traceback (most recent call last):
      ...
    TypeError: Expected a matrix, got int/list instead
    """
    if (
        _check_not_integer(matrix_a)
        and _check_not_integer(matrix_b)
        and _verify_matrix_sizes(matrix_a, matrix_b)
    ):
        return [[i - j for i, j in zip(*m)] for m in zip(matrix_a, matrix_b)]
    raise TypeError("Expected a matrix, got int/list instead")


def scalar_multiply(matrix: list[list[int]], n: float) -> list[list[float]]:
    """
    >>> scalar_multiply([[1,2],[3,4]],5)
    [[5, 10], [15, 20]]
    >>> scalar_multiply([[1.4,2.3],[3,4]],5)
    [[7.0, 11.5], [15, 20]]
    """
    return [[x * n for x in row] for row in matrix]


def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    """
    >>> multiply([[1,2],[3,4]],[[5,5],[7,5]])
    [[19, 15], [43, 35]]
    >>> multiply([[1,2.5],[3,4.5]],[[5,5],[7,5]])
    [[22.5, 17.5], [46.5, 37.5]]
    >>> multiply([[1, 2, 3]], [[2], [3], [4]])
    [[20]]
    """
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        rows, cols = _verify_matrix_sizes(matrix_a, matrix_b)

    if cols[0] != rows[1]:
        msg = (
            "Cannot multiply matrix of dimensions "
            f"({rows[0]},{cols[0]}) and ({rows[1]},{cols[1]})"
        )
        raise ValueError(msg)
    return [
        [sum(m * n for m, n in zip(i, j)) for j in zip(*matrix_b)] for i in matrix_a
    ]


def identity(n: int) -> list[list[int]]:
    """
    :param n: dimension for nxn matrix
    :type n: int
    :return: Identity matrix of shape [n, n]
    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    n = int(n)
    return [[int(row == column) for column in range(n)] for row in range(n)]


def transpose(
    matrix: list[list[int]], return_map: bool = True
) -> list[list[int]] | map[list[int]]:
    """
    >>> transpose([[1,2],[3,4]]) # doctest: +ELLIPSIS
    <map object at ...
    >>> transpose([[1,2],[3,4]], return_map=False)
    [[1, 3], [2, 4]]
    >>> transpose([1, [2, 3]])
    Traceback (most recent call last):
      ...
    TypeError: Expected a matrix, got int/list instead
    """
    if _check_not_integer(matrix):
        if return_map:
            return map(list, zip(*matrix))
        else:
            return list(map(list, zip(*matrix)))
    raise TypeError("Expected a matrix, got int/list instead")


def minor(matrix: list[list[int]], row: int, column: int) -> list[list[int]]:
    """
    >>> minor([[1, 2], [3, 4]], 1, 1)
    [[1]]
    """
    minor = matrix[:row] + matrix[row + 1 :]
    return [row[:column] + row[column + 1 :] for row in minor]


def determinant(matrix: list[list[int]]) -> Any:
    """
    >>> determinant([[1, 2], [3, 4]])
    -2
    >>> determinant([[1.5, 2.5], [3, 4]])
    -1.5
    """
    if len(matrix) == 1:
        return matrix[0][0]

    return sum(
        x * determinant(minor(matrix, 0, i)) * (-1) ** i
        for i, x in enumerate(matrix[0])
    )


def inverse(matrix: list[list[int]]) -> list[list[float]] | None:
    """
    >>> inverse([[1, 2], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> inverse([[1, 1], [1, 1]])
    """
    # https://stackoverflow.com/questions/20047519/python-doctests-test-for-none
    det = determinant(matrix)
    if det == 0:
        return None

    matrix_minor = [
        [determinant(minor(matrix, i, j)) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]

    cofactors = [
        [x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])]
        for row in range(len(matrix))
    ]
    adjugate = list(transpose(cofactors))
    return scalar_multiply(adjugate, 1 / det)


def _check_not_integer(matrix: list[list[int]]) -> bool:
    return not isinstance(matrix, int) and not isinstance(matrix[0], int)


def _shape(matrix: list[list[int]]) -> tuple[int, int]:
    return len(matrix), len(matrix[0])


def _verify_matrix_sizes(
    matrix_a: list[list[int]], matrix_b: list[list[int]]
) -> tuple[tuple[int, int], tuple[int, int]]:
    shape = _shape(matrix_a) + _shape(matrix_b)
    if shape[0] != shape[3] or shape[1] != shape[2]:
        msg = (
            "operands could not be broadcast together with shape "
            f"({shape[0], shape[1]}), ({shape[2], shape[3]})"
        )
        raise ValueError(msg)
    return (shape[0], shape[2]), (shape[1], shape[3])


def main() -> None:
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    matrix_c = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print(f"Add Operation, {add(matrix_a, matrix_b) = } \n")
    print(f"Multiply Operation, {multiply(matrix_a, matrix_b) = } \n")
    print(f"Identity: {identity(5)}\n")
    print(f"Minor of {matrix_c} = {minor(matrix_c, 1, 2)} \n")
    print(f"Determinant of {matrix_b} = {determinant(matrix_b)} \n")
    print(f"Inverse of {matrix_d} = {inverse(matrix_d)}\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
