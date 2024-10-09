"""
İki boyutlu matris işlemleri için fonksiyonlar

Organiser: K. Umut Araz
"""

from __future__ import annotations

from typing import Any


def topla(*matrisler: list[list[int]]) -> list[list[int]]:
    """
    >>> topla([[1,2],[3,4]],[[2,3],[4,5]])
    [[3, 5], [7, 9]]
    >>> topla([[1.2,2.4],[3,4]],[[2,3],[4,5]])
    [[3.2, 5.4], [7, 9]]
    >>> topla([[1, 2], [4, 5]], [[3, 7], [3, 4]], [[3, 5], [5, 7]])
    [[7, 14], [12, 16]]
    >>> topla([3], [4, 5])
    Traceback (most recent call last):
      ...
    TypeError: Beklenen bir matris, int/list yerine geldi
    """
    if all(_check_not_integer(m) for m in matrisler):
        for i in matrisler[1:]:
            _verify_matrix_sizes(matrisler[0], i)
        return [[sum(t) for t in zip(*m)] for m in zip(*matrisler)]
    raise TypeError("Beklenen bir matris, int/list yerine geldi")


def çıkar(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    """
    >>> çıkar([[1,2],[3,4]],[[2,3],[4,5]])
    [[-1, -1], [-1, -1]]
    >>> çıkar([[1,2.5],[3,4]],[[2,3],[4,5.5]])
    [[-1, -0.5], [-1, -1.5]]
    >>> çıkar([3], [4, 5])
    Traceback (most recent call last):
      ...
    TypeError: Beklenen bir matris, int/list yerine geldi
    """
    if (
        _check_not_integer(matrix_a)
        and _check_not_integer(matrix_b)
        and _verify_matrix_sizes(matrix_a, matrix_b)
    ):
        return [[i - j for i, j in zip(*m)] for m in zip(matrix_a, matrix_b)]
    raise TypeError("Beklenen bir matris, int/list yerine geldi")


def skalar_çarp(matrix: list[list[int]], n: float) -> list[list[float]]:
    """
    >>> skalar_çarp([[1,2],[3,4]],5)
    [[5, 10], [15, 20]]
    >>> skalar_çarp([[1.4,2.3],[3,4]],5)
    [[7.0, 11.5], [15, 20]]
    """
    return [[x * n for x in row] for row in matrix]


def çarp(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    """
    >>> çarp([[1,2],[3,4]],[[5,5],[7,5]])
    [[19, 15], [43, 35]]
    >>> çarp([[1,2.5],[3,4.5]],[[5,5],[7,5]])
    [[22.5, 17.5], [46.5, 37.5]]
    >>> çarp([[1, 2, 3]], [[2], [3], [4]])
    [[20]]
    """
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        rows, cols = _verify_matrix_sizes(matrix_a, matrix_b)

    if cols[0] != rows[1]:
        msg = (
            "Bu boyutlardaki matrisleri çarpamazsınız "
            f"({rows[0]},{cols[0]}) ve ({rows[1]},{cols[1]})"
        )
        raise ValueError(msg)
    return [
        [sum(m * n for m, n in zip(i, j)) for j in zip(*matrix_b)] for i in matrix_a
    ]


def birim(n: int) -> list[list[int]]:
    """
    :param n: nxn matrisin boyutu
    :type n: int
    :return: [n, n] şeklinde birim matris
    >>> birim(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    n = int(n)
    return [[int(row == column) for column in range(n)] for row in range(n)]


def transpoze(
    matrix: list[list[int]], return_map: bool = True
) -> list[list[int]] | map[list[int]]:
    """
    >>> transpoze([[1,2],[3,4]]) # doctest: +ELLIPSIS
    <map object at ...
    >>> transpoze([[1,2],[3,4]], return_map=False)
    [[1, 3], [2, 4]]
    >>> transpoze([1, [2, 3]])
    Traceback (most recent call last):
      ...
    TypeError: Beklenen bir matris, int/list yerine geldi
    """
    if _check_not_integer(matrix):
        if return_map:
            return map(list, zip(*matrix))
        else:
            return list(map(list, zip(*matrix)))
    raise TypeError("Beklenen bir matris, int/list yerine geldi")


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


def ters(matrix: list[list[int]]) -> list[list[float]] | None:
    """
    >>> ters([[1, 2], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> ters([[1, 1], [1, 1]])
    """
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
    adjugate = list(transpoze(cofactors))
    return skalar_çarp(adjugate, 1 / det)


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
            "İşlemler bu şekillerle birleştirilemez "
            f"({shape[0], shape[1]}), ({shape[2], shape[3]})"
        )
        raise ValueError(msg)
    return (shape[0], shape[2]), (shape[1], shape[3])


def main() -> None:
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    matrix_c = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print(f"Toplama İşlemi, {topla(matrix_a, matrix_b) = } \n")
    print(f"Çarpma İşlemi, {çarp(matrix_a, matrix_b) = } \n")
    print(f"Birim: {birim(5)}\n")
    print(f"{matrix_c} matrisinin minoru = {minor(matrix_c, 1, 2)} \n")
    print(f"{matrix_b} matrisinin determinantı = {determinant(matrix_b)} \n")
    print(f"{matrix_d} matrisinin tersi = {ters(matrix_d)}\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
