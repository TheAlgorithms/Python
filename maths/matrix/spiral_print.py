"""
This program print the matrix in spiral form.
This problem has been solved through recursive way.

      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii) number of column of all rows should be equal
"""

from collections.abc import Iterable


def check_matrix(matrix):
    # must be
    if matrix and isinstance(matrix, Iterable):
        if isinstance(matrix[0], Iterable):
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


def spiralPrint(a):
    if check_matrix(a) and len(a) > 0:
        matRow = len(a)
        if isinstance(a[0], Iterable):
            matCol = len(a[0])
        else:
            for dat in a:
                print(dat),
            return

        # horizotal printing increasing
        for i in range(0, matCol):
            print(a[0][i]),
        # vertical printing down
        for i in range(1, matRow):
            print(a[i][matCol - 1]),
        # horizotal printing decreasing
        if matRow > 1:
            for i in range(matCol - 2, -1, -1):
                print(a[matRow - 1][i]),
        # vertical printing up
        for i in range(matRow - 2, 0, -1):
            print(a[i][0]),
        remainMat = [row[1 : matCol - 1] for row in a[1 : matRow - 1]]
        if len(remainMat) > 0:
            spiralPrint(remainMat)
        else:
            return
    else:
        print("Not a valid matrix")
        return


# driver code
if __name__ == "__main__":
    a = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
    spiralPrint(a)
