"""
This program print the matrix in spiral form.
This problem has been solved through recursive way.
      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii) number of column of all rows should be equal
"""


def check_matrix(matrix: list[list[int]]) -> bool:
    # must be
    matrix = list(list(row) for row in matrix)
    if matrix and isinstance(matrix, list):
        if isinstance(matrix[0], list):
            prev_len = 0
            for row in matrix:
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
        else:
            result = True
    else:
        result = False

    return result


def spiral_print_clockwise(a: list[list[int]]) -> None:
    """
    >>> spiral_print_clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    1
    2
    3
    4
    8
    12
    11
    10
    9
    5
    6
    7
    """
    if check_matrix(a) and len(a) > 0:
        a = list(list(row) for row in a)
        mat_row = len(a)
        if isinstance(a[0], list):
            mat_col = len(a[0])
        else:
            for dat in a:
                print(dat)
            return

        # horizotal printing increasing
        for i in range(0, mat_col):
            print(a[0][i])
        # vertical printing down
        for i in range(1, mat_row):
            print(a[i][mat_col - 1])
        # horizotal printing decreasing
        if mat_row > 1:
            for i in range(mat_col - 2, -1, -1):
                print(a[mat_row - 1][i])
        # vertical printing up
        for i in range(mat_row - 2, 0, -1):
            print(a[i][0])
        remain_mat = [row[1 : mat_col - 1] for row in a[1 : mat_row - 1]]
        if len(remain_mat) > 0:
            spiral_print_clockwise(remain_mat)
        else:
            return
    else:
        print("Not a valid matrix")
        return


# driver code
if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    spiral_print_clockwise(a)
