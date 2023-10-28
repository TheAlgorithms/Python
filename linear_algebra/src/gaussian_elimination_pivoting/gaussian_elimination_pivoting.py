import sys
import time

import numpy as np

matrixab = np.loadtxt("matrix.txt")
B = np.copy(matrixab[:, matrixab.shape[1] - 1])


def foo(matrix):
    start = time.process_time()
    ab = np.copy(matrix)
    numofrows = ab.shape[0]
    numofcolumns = ab.shape[1] - 1
    xlst = []

    """Lead element search"""
    print("Matrix before leading coefficient search: ")
    print(ab)
    print(" ")

    """Upper triangular matrix"""
    for columnnum in range(numofrows):
        for i in range(columnnum, numofcolumns):
            if abs(ab[i][columnnum]) > abs(ab[columnnum][columnnum]):
                ab[[columnnum, i]] = ab[[i, columnnum]]
                if ab[columnnum, columnnum] == 0.0:
                    sys.exit("Matrix is not correct")
            else:
                pass
        if columnnum != 0:
            for i in range(columnnum, numofrows):
                ab[i, :] -= (
                    ab[i, columnnum - 1]
                    / ab[columnnum - 1, columnnum - 1]
                    * ab[columnnum - 1, :]
                )

    print("Upper triangular matrix: ")
    print(ab.round(3))
    print(" ")

    """Find x vector"""
    columnnum = numofrows
    while columnnum != 0:
        columnnum -= 1
        lineofx = ab[columnnum, numofrows]
        if columnnum + 1 != numofrows:
            for y in range(1, numofrows - columnnum):
                lineofx += -ab[columnnum, numofrows - y] * xlst[y - 1]
        x = lineofx / ab[columnnum, columnnum]
        xlst.append(x)

    stop = time.process_time()
    xlst.reverse()
    print("x vector: ")
    print(xlst)
    print(" ")
    print(f"Start time: {start}, End time: {stop}")
    print(f"Elapsed time during the whole function in seconds: {stop - start}")

    return np.asarray(xlst)


if __name__ == "__main__":
    vectorofxalpha = foo(matrixab)

"""Cond(A)"""
modifiedb = np.copy(B)
modifiedb[np.argmax(abs(B))] = B[np.argmax(abs(B))] / 100 * 101

matrixab[:, matrixab.shape[1] - 1] = modifiedb
print()
print("Cond(A) check: ")
vectorofxbeta = foo(matrixab)

deltab = modifiedb - B
deltax = vectorofxalpha - vectorofxbeta
print(" ")
conda = abs(np.sum(deltax) / np.sum(vectorofxalpha)) * (np.sum(B) / np.sum(deltab))
print(f"Cond(A) =< {conda:0.6f}")


# Example usage:
# n_size = 3
# a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
# b_vector = np.array([10, 11, 12], dtype=float)

# solution = custom_gauss_elimination_pivoting(a_matrix, b_vector, n_size)
# print("Solution:", solution)


# URL that points to Wikipedia or another similar explanation.
# >>>>>>URL:https://courses.engr.illinois.edu/cs357/su2013/lectures/lecture07.pdf<<<<<#
