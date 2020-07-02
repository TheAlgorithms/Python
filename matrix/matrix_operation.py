"""
Functions for 2D matrix operations
"""

from typing import List, Tuple


def add(matrix_a: List[list], matrix_b: List[list]) -> List[list]:
    """
    >>> add([[1,2],[3,4]],[[2,3],[4,5]])
    [[3, 5], [7, 9]]
    >>> add([[1.2,2.4],[3,4]],[[2,3],[4,5]])
    [[3.2, 5.4], [7, 9]]
    """
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        _verify_matrix_sizes(matrix_a, matrix_b)
        matrix_c = [[i + j for i, j in zip(m, n)]
                    for m, n in zip(matrix_a, matrix_b)]
        return matrix_c


def subtract(matrix_a: List[list], matrix_b: List[list]) -> List[list]:
    """
    >>> subtract([[1,2],[3,4]],[[2,3],[4,5]])
    [[-1, -1], [-1, -1]]
    >>> subtract([[1,2.5],[3,4]],[[2,3],[4,5.5]])
    [[-1, -0.5], [-1, -1.5]]
    """
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        _verify_matrix_sizes(matrix_a, matrix_b)
        matrix_c = [[i - j for i, j in zip(m, n)]
                    for m, n in zip(matrix_a, matrix_b)]
        return matrix_c


def scalar_multiply(matrix: List[list], n: int) -> List[list]:
    """
    >>> scalar_multiply([[1,2],[3,4]],5)
    [[5, 10], [15, 20]]
    >>> scalar_multiply([[1.4,2.3],[3,4]],5)
    [[7.0, 11.5], [15, 20]]
    """
    return [[x * n for x in row] for row in matrix]


def multiply(matrix_a: List[list], matrix_b: List[list]) -> List[list]:
    """
    >>> multiply([[1,2],[3,4]],[[5,5],[7,5]])
    [[19, 15], [43, 35]]
    >>> multiply([[1,2.5],[3,4.5]],[[5,5],[7,5]])
    [[22.5, 17.5], [46.5, 37.5]]
    """
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        matrix_c = []
        rows, cols = _verify_matrix_sizes(matrix_a, matrix_b)

        if cols[0] != rows[1]:
            raise ValueError(
                f"Cannot multiply matrix of dimensions ({rows[0]},{cols[0]}) "
                f"and ({rows[1]},{cols[1]})"
            )
        for i in range(rows[0]):
            list_1 = []
            for j in range(cols[1]):
                val = 0
                for k in range(cols[1]):
                    val += matrix_a[i][k] * matrix_b[k][j]
                list_1.append(val)
            matrix_c.append(list_1)
        return matrix_c


def identity(n: int) -> List[list]:
    """
    :param n: dimension for nxn matrix
    :type n: int
    :return: Identity matrix of shape [n, n]
    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    n = int(n)
    return [[int(row == column) for column in range(n)] for row in range(n)]


def transpose(matrix: List[list], return_map: bool = True) -> List[list]:
    """
    >>> transpose([[1,2],[3,4]]) # doctest: +ELLIPSIS
    <map object at ...
    >>> transpose([[1,2],[3,4]], return_map=False)
    [[1, 3], [2, 4]]
    """
    if _check_not_integer(matrix):
        if return_map:
            return map(list, zip(*matrix))
        else:
            return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def minor(matrix: List[list], row: int, column: int) -> List[list]:
    """
    >>> minor([[1, 2], [3, 4]], 1, 1)
    [[1]]
    """
    minor = matrix[:row] + matrix[row + 1:]
    minor = [row[:column] + row[column + 1:] for row in minor]
    return minor


def determinant(matrix: List[list]) -> int:
    """
    >>> determinant([[1, 2], [3, 4]])
    -2
    >>> determinant([[1.5, 2.5], [3, 4]])
    -1.5
    """
    if len(matrix) == 1:
        return matrix[0][0]

    res = 0
    for x in range(len(matrix)):
        res += matrix[0][x] * determinant(minor(matrix, 0, x)) * (-1) ** x
    return res


def inverse(matrix: List[list]) -> List[list]:
    """
    >>> inverse([[1, 2], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> inverse([[1, 1], [1, 1]])
    """
    # https://stackoverflow.com/questions/20047519/python-doctests-test-for-none
    det = determinant(matrix)
    if det == 0:
        return None

    matrix_minor = [[] for _ in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix_minor[i].append(determinant(minor(matrix, i, j)))

    cofactors = [
        [x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])]
        for row in range(len(matrix))
    ]
    adjugate = transpose(cofactors)
    return scalar_multiply(adjugate, 1 / det)


def _check_not_integer(matrix: List[list]) -> bool:
    if not isinstance(matrix, int) and not isinstance(matrix[0], int):
        return True
    raise TypeError("Expected a matrix, got int/list instead")


def _shape(matrix: List[list]) -> list:
    return list((len(matrix), len(matrix[0])))


def _verify_matrix_sizes(
        matrix_a: List[list], matrix_b: List[list]) -> Tuple[list]:
    shape = _shape(matrix_a)
    shape += _shape(matrix_b)
    if shape[0] != shape[2] or shape[1] != shape[3]:
        raise ValueError(
            f"operands could not be broadcast together with shape "
            f"({shape[0], shape[1]}), ({shape[2], shape[3]})"
        )
    return [shape[0], shape[2]], [shape[1], shape[3]]


def main():
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    matrix_c = [[11, 12, 13, 14], [21, 22, 23, 24],
                [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print(
        f"Add Operation, {matrix_a} + {matrix_b}"
        f" = {add(matrix_a, matrix_b)} \n")
    print(
        f"Multiply Operation, {matrix_a} * {matrix_b}",
        f"= {multiply(matrix_a, matrix_b)} \n",
    )
    print(f"Identity: {identity(5)}\n")
    print(f"Minor of {matrix_c} = {minor(matrix_c, 1, 2)} \n")
    print(f"Determinant of {matrix_b} = {determinant(matrix_b)} \n")
    print(f"Inverse of {matrix_d} = {inverse(matrix_d)}\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
