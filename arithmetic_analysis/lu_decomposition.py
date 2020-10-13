import numpy


def lower_upper_decompose(table: list) -> (list, list):
    """Lower–Upper (LU) decomposition - https://en.wikipedia.org/wiki/LU_decomposition

    Args:
        table (list): Table that contains our data

    Raises:
        ValueError: If table is not an square array.

    Returns:
        (list, list): L, U. Lower and upper arrays.

    >>> lower_upper_decompose(numpy.array([[2, -2, 1], [0, 1, 2], [5, 3]]))
    Traceback (most recent call last):
    ...
    ValueError: not enough values to unpack (expected 2, got 1)
    >>> lower_upper_decompose(numpy.array([[2, -2], [0, 1], [5, 3]]))
    Traceback (most recent call last):
    ...
    ValueError: Table should be square array.
    >>> matrix = numpy.array([[2, -2, 1], [0, 1, 2], [5, 3, -1]])
    >>> lower_upper_decompose(matrix)
    (array([[1. , 0. , 0. ],
           [0. , 1. , 0. ],
           [2.5, 8. , 1. ]]), array([[  2. ,  -2. ,   1. ],
           [  0. ,   1. ,   2. ],
           [  0. ,   0. , -19.5]]))
    """
    # table input has to be a square array so we need to check first
    rows, columns = numpy.shape(table)
    if rows != columns:
        raise ValueError("Table should be square array.")

    L = numpy.zeros((rows, columns))
    U = numpy.zeros((rows, columns))
    for i in range(columns):
        for j in range(i):
            sum = 0
            for k in range(j):
                sum += L[i][k] * U[k][j]
            L[i][j] = (table[i][j] - sum) / U[j][j]
        L[i][i] = 1
        for j in range(i, columns):
            sum1 = 0
            for k in range(i):
                sum1 += L[i][k] * U[k][j]
            U[i][j] = table[i][j] - sum1
    return L, U


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    matrix = numpy.array([[2, -2, 1], [0, 1, 2], [5, 3, 3]])
    L, U = lower_upper_decompose(matrix)
    print(L)
    print(U)
