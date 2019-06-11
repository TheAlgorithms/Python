from __future__ import print_function

def add(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = []
    for i in range(rows):
        list_1 = []
        for j in range(columns):
            val = matrix_a[i][j] + matrix_b[i][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c

def scalarMultiply(matrix , n):
    return [[x * n for x in row] for row in matrix]

def multiply(matrix_a, matrix_b):
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c

def identity(n):
    return [[int(row == column) for column in range(n)] for row in range(n)] 

def transpose(matrix):
    return map(list , zip(*matrix))

def minor(matrix, row, column):
    minor = matrix[:row] + matrix[row + 1:]
    minor = [row[:column] + row[column + 1:] for row in minor]
    return minor

def determinant(matrix):
    if len(matrix) == 1: return matrix[0][0]
    
    res = 0
    for x in range(len(matrix)):
        res += matrix[0][x] * determinant(minor(matrix , 0 , x)) * (-1) ** x
    return res

def inverse(matrix):
    det = determinant(matrix)
    if det == 0: return None

    matrixMinor = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrixMinor[i].append(determinant(minor(matrix , i , j)))
    
    cofactors = [[x * (-1) ** (row + col) for col, x in enumerate(matrixMinor[row])] for row in range(len(matrix))]
    adjugate = transpose(cofactors)
    return scalarMultiply(adjugate , 1/det)

def main():
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    matrix_c = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    print('Add Operation, %s + %s = %s \n' %(matrix_a, matrix_b, (add(matrix_a, matrix_b))))
    print('Multiply Operation, %s * %s = %s \n' %(matrix_a, matrix_b, multiply(matrix_a, matrix_b)))
    print('Identity:  %s \n' %identity(5))
    print('Minor of %s = %s \n' %(matrix_c, minor(matrix_c , 1 , 2)))
    print('Determinant of %s = %s \n' %(matrix_b, determinant(matrix_b)))
    print('Inverse of %s = %s\n'%(matrix_d, inverse(matrix_d)))

if __name__ == '__main__':
    main()
