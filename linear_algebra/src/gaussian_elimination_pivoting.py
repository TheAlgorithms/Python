import numpy as np
import sys
import time

matrixAB = np.loadtxt("matrix.txt")
B = np.copy(matrixAB[:, matrixAB.shape[1] - 1])


def foo(matrix):
    start = time.process_time()
    AB = np.copy(matrix)
    numOfRows = AB.shape[0]
    numOfColumns = AB.shape[1] - 1
    xLst = []

    """"Lead element search"""
    print("Matrix before leading coefficient search: ")
    print(AB)
    print(" ")

    """Upper triangular matrix"""

    for columnNum in range(numOfRows):
        for i in range(columnNum, numOfColumns):
            if abs(AB[i][columnNum]) > abs(AB[columnNum][columnNum]):
                AB[[columnNum, i]] = AB[[i, columnNum]]
                if AB[columnNum, columnNum] == 0.0:
                    sys.exit("Matrix is not correct")
            else:
                pass
        if columnNum != 0:
            for i in range(columnNum, numOfRows):
                AB[i, :] = (
                    AB[i, :]
                    - AB[i, columnNum - 1]
                    / AB[columnNum - 1, columnNum - 1]
                    * AB[columnNum - 1, :]
                )

    print("Upper triangular matrix: ")
    print(AB.round(3))
    print(" ")

    """Find x vector"""
    columnNum = numOfRows
    while columnNum != 0:
        columnNum -= 1
        lineOfX = AB[columnNum, numOfRows]
        if columnNum + 1 != numOfRows:
            for y in range(1, numOfRows - columnNum):
                lineOfX += -AB[columnNum, numOfRows - y] * xLst[y - 1]
        x = lineOfX / AB[columnNum, columnNum]
        xLst.append(x)

    stop = time.process_time()
    xLst.reverse()
    print("x vector: ")
    print(xLst)
    print(" ")
    print("Start time: ", start, "End time: ", stop)
    print("Elapsed time during the whole function in seconds:", stop - start)

    return np.asarray(xLst)


vectorOfXAlpha = foo(matrixAB)

"""Cond(A)"""
modifiedB = np.copy(B)
modifiedB[np.argmax(abs(B))] = B[np.argmax(abs(B))] / 100 * 101

matrixAB[:, matrixAB.shape[1] - 1] = modifiedB
print()
print("Cond(A) check: ")
vectorOfXBeta = foo(matrixAB)

deltaB = modifiedB - B
deltaX = vectorOfXAlpha - vectorOfXBeta
print(" ")
condA = abs(np.sum(deltaX) / np.sum(vectorOfXAlpha)) * (np.sum(B) / np.sum(deltaB))
print("Cond(A) =< {:03f}".format(condA))


# Example usage:
# n_size = 3
# a_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
# b_vector = np.array([10, 11, 12], dtype=float)

# solution = custom_gauss_elimination_pivoting(a_matrix, b_vector, n_size)
# print("Solution:", solution)


# URL that points to Wikipedia or another similar explanation.
# >>>>>>URL:https://courses.engr.illinois.edu/cs357/su2013/lectures/lecture07.pdf<<<<<#
