import pytest

from divide_and_conquer.strassen_matrix_multiplication import split_matrix


def test_4x4_matrix():
    matrix = [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]]
    expected = ([[4, 3], [2, 3]], [[2, 4], [1, 1]], [[6, 5], [8, 4]], [[4, 3], [1, 6]])
    assert split_matrix(matrix) == expected


def test_8x8_matrix():
    matrix = [
        [4, 3, 2, 4, 4, 3, 2, 4],
        [2, 3, 1, 1, 2, 3, 1, 1],
        [6, 5, 4, 3, 6, 5, 4, 3],
        [8, 4, 1, 6, 8, 4, 1, 6],
        [4, 3, 2, 4, 4, 3, 2, 4],
        [2, 3, 1, 1, 2, 3, 1, 1],
        [6, 5, 4, 3, 6, 5, 4, 3],
        [8, 4, 1, 6, 8, 4, 1, 6],
    ]
    expected = (
        [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
        [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
        [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
        [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]],
    )
    assert split_matrix(matrix) == expected


def test_invalid_odd_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(Exception, match="Odd matrices are not supported!"):
        split_matrix(matrix)


def test_invalid_non_square_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20],
    ]
    with pytest.raises(Exception, match="Odd matrices are not supported!"):
        split_matrix(matrix)
