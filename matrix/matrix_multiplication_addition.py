def add(matrix_a, matrix_b):
    if(not is_matrix(matrix_a) or not is_matrix(matrix_b)):
        raise Exception('One or more of the arguments of multiply is not a matrix!')
    size_a = matrix_size(matrix_a)
    size_b = matrix_size(matrix_b)
    if(not size_a[0] == size_b[0] or not size_a[1] == size_b[1]):
        raise Exception('Matrices are incompatible in size')
    rows = size_a[0]
    columns = size_a[1]
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
    '''Returns the matrix product of two matrices, expressed as a list of lists'''

    if(not is_matrix(matrix_a) or not is_matrix(matrix_b)):
        raise Exception('One or more of the arguments of multiply is not a matrix!')
    size_a = matrix_size(matrix_a)
    size_b = matrix_size(matrix_b)
    if(not size_a[0] == size_b[1]):
        raise Exception('Matrices are incompatible in size')
    matrix_c = []
    iteration_num = 0
    
    for i in range(size_a[0]):
        row_c = []
        for j in range(size_b[1]):
            element_c = 0
            #We previously checked that the number of columns in a is the number of rows in b
            for k in range(size_a[1]):
                element_c += matrix_a[i][k] * matrix_b[k][j]
            row_c.append(element_c)
        matrix_c.append(row_c)
    return matrix_c

def identity(n):
    return [[int(row == column) for column in range(n)] for row in range(n)] 

def transpose(matrix):
    if(not is_matrix(matrix)):
        raise Exception('Argument is not a matrix!')
    return map(list , zip(*matrix))

def minor(matrix, row, column):
    if(not is_matrix(matrix)):
        raise Exception('Argument is not a matrix!')
    minor = matrix[:row] + matrix[row + 1:]
    minor = [row[:column] + row[column + 1:] for row in minor]
    return minor

def determinant(matrix):
    if(not is_matrix(matrix)):
        raise Exception('Argument is not a matrix!')
    if len(matrix) == 1: return matrix[0][0]
    
    res = 0
    for x in range(len(matrix)):
        res += matrix[0][x] * determinant(minor(matrix , 0 , x)) * (-1) ** x
    return res

def inverse(matrix):
    if(not is_matrix(matrix)):
        raise Exception('Argument is not a matrix!')
    det = determinant(matrix)
    if det == 0: return None

    matrixMinor = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrixMinor[i].append(determinant(minor(matrix , i , j)))
    
    cofactors = [[x * (-1) ** (row + col) for col, x in enumerate(matrixMinor[row])] for row in range(len(matrix))]
    adjugate = transpose(cofactors)
    return scalarMultiply(adjugate , 1/det)
    
def check_matrix_size_consistency(matrix):
    '''Checks that each row in a matrix has the same number of elements'''
    if(is_list(matrix)):
        for element in matrix:
            if(not is_list(element)):
                return False
            if(len(matrix[0]) != len(element)):
                return False
    return True;

def is_list(element):
    '''Checks is a variable is a list'''
    if(type(element) == type([])):
        return True;
    else:
        return False;

def is_int_or_float(element):
    '''Checks is a variable is an int or a float'''
    if(type(element) == type(1) or type(element) == type(1.1)):
        return True
    else:
        return False;
        
def is_matrix(matrix):
    '''Checks is a variable is a matrix'''
    #A variable is a matrix if and only if it is a list of lists of numbers (ints or floats)
    if(is_list(matrix)):
        for row in matrix:
            if(is_list(row)):
                for element in row:
                    if(not is_int_or_float(element)):
                        return False
            else:
                return False
    else:
        return False
    return True
    
def matrix_size(matrix):
    '''Returns the size of a matrix as a list [rows, columns]'''
    if(not is_matrix(matrix)):
       raise Exception('argument is not a matrix!')
    return [len(matrix), len(matrix[0])]

def main():
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    matrix_c = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
    matrix_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
    matrix_e = [ [1, 2], [2, 1] , [1, 1]]
    matrix_f = [ [1, 2, 5], [2, 1, 1] ]

    print(add(matrix_a, matrix_b))
    print(multiply(matrix_e, matrix_f))
    print(identity(5))
    print(minor(matrix_c , 1 , 2))
    print(determinant(matrix_b))
    print(inverse(matrix_d))

if __name__ == '__main__':
    main()
