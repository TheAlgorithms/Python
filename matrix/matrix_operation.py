"""
function based version of matrix operations, which are just 2D arrays
"""


def add(matrix_a, matrix_b):
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        rows, cols = _verify_matrix_sizes(matrix_a, matrix_b)
        matrix_c = []
        for i in range(rows[0]):
            list_1 = []
            for j in range(cols[0]):
                val = matrix_a[i][j] + matrix_b[i][j]
                list_1.append(val)
            matrix_c.append(list_1)
        return matrix_c


def subtract(matrix_a, matrix_b):
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        rows, cols = _verify_matrix_sizes(matrix_a, matrix_b)
        matrix_c = []
        for i in range(rows[0]):
            list_1 = []
            for j in range(cols[0]):
                val = matrix_a[i][j] - matrix_b[i][j]
                list_1.append(val)
            matrix_c.append(list_1)
        return matrix_c


def scalar_multiply(matrix, n):
    return [[x * n for x in row] for row in matrix]


def multiply(matrix_a, matrix_b):
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        matrix_c = []
        rows, cols = _verify_matrix_sizes(matrix_a, matrix_b)

        if cols[0] != rows[1]:
            raise ValueError(f'Cannot multiply matrix of dimensions ({rows[0]},{cols[0]}) '
                             f'and ({rows[1]},{cols[1]})')
        for i in range(rows[0]):
            list_1 = []
            for j in range(cols[1]):
                val = 0
                for k in range(cols[1]):
                    val = val + matrix_a[i][k] * matrix_b[k][j]
                list_1.append(val)
            matrix_c.append(list_1)
        return matrix_c


def identity(n):
    """
    :param n: dimension for nxn matrix
    :type n: int
    :return: Identity matrix of shape [n, n]
    """
    n = int(n)
    return [[int(row == column) for column in range(n)] for row in range(n)] 


def transpose(matrix, return_map=True):
    if _check_not_integer(matrix):
        if return_map:
            return map(list, zip(*matrix))
        else:
            # mt = []
            # for i in range(len(matrix[0])):
            #     mt.append([row[i] for row in matrix])
            # return mt
            return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def minor(matrix, row, column):
    minor = matrix[:row] + matrix[row + 1:]
    minor = [row[:column] + row[column + 1:] for row in minor]
    return minor


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    
    res = 0
    for x in range(len(matrix)):
        res += matrix[0][x] * determinant(minor(matrix, 0, x)) * (-1) ** x
    return res


def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return None

    matrix_minor = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix_minor[i].append(determinant(minor(matrix, i, j)))
    
    cofactors = [[x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])] for row in range(len(matrix))]
    adjugate = transpose(cofactors)
    return scalar_multiply(adjugate, 1/det)


def _check_not_integer(matrix):
    try:
        rows = len(matrix)
        cols = len(matrix[0])
        return True
    except TypeError:
        raise TypeError("Cannot input an integer value, it must be a matrix")


def _shape(matrix):
    return list((len(matrix), len(matrix[0])))


def _verify_matrix_sizes(matrix_a, matrix_b):
    shape = _shape(matrix_a)
    shape += _shape(matrix_b)
    if shape[0] != shape[2] or shape[1] != shape[3]:
        raise ValueError(f"operands could not be broadcast together with shape "
                         f"({shape[0], shape[1]}), ({shape[2], shape[3]})")
    return [shape[0], shape[2]], [shape[1], shape[3]]


def main():
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    matrix_c = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print('Add Operation, %s + %s = %s \n' %(matrix_a, matrix_b, (add(matrix_a, matrix_b))))
    print('Multiply Operation, %s * %s = %s \n' %(matrix_a, matrix_b, multiply(matrix_a, matrix_b)))
    print('Identity:  %s \n' %identity(5))
    print('Minor of %s = %s \n' %(matrix_c, minor(matrix_c, 1, 2)))
    print('Determinant of %s = %s \n' %(matrix_b, determinant(matrix_b)))
    print('Inverse of %s = %s\n'%(matrix_d, inverse(matrix_d)))


if __name__ == '__main__':
    main()
