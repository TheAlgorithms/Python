import math

def default_matrix_multiplication(a, b):
    """
    Multiplication only for 2x2 matrices
    """
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception('Matrices are not 2x2')
    new_matrix = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                    [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]
    return new_matrix

def matrix_addition(matrix_a, matrix_b):
    return [[matrix_a[row][col] + matrix_b[row][col] for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]

def matrix_subtraction(matrix_a, matrix_b):
    return [[matrix_a[row][col] - matrix_b[row][col] for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def split_matrix(a):
    """
    Given an even length matrix, returns the top_left, top_right, bot_left, bot_right quadrant.
    """
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception('Odd matrices are not supported!')

    matrix_length = len(a)
    mid = matrix_length // 2

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]



    return top_left, top_right, bot_left, bot_right

def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def strassen(matrix_a, matrix_b):
    """
    Recursive function to calculate the product of two matrices, using the Strassen Algorithm.
    It only supports even length matrices.
    """
    if matrix_dimensions(matrix_a) == (2, 2):
        return default_matrix_multiplication(matrix_a, matrix_b)

    a,b,c,d = split_matrix(matrix_a)
    e,f,g,h = split_matrix(matrix_b)

    t1 = strassen(a, matrix_subtraction(f, h))
    t2 = strassen(matrix_addition(a, b), h)
    t3 = strassen(matrix_addition(c, d), e)
    t4 = strassen(d, matrix_subtraction(g, e))
    t5 = strassen(matrix_addition(a, d), matrix_addition(e, h))
    t6 = strassen(matrix_subtraction(b, d), matrix_addition(g, h))
    t7 = strassen(matrix_subtraction(a, c), matrix_addition(e, f))

    top_left = matrix_addition(matrix_subtraction(matrix_addition(t5, t4), t2), t6)
    top_right = matrix_addition(t1, t2)
    bot_left = matrix_addition(t3, t4)
    bot_right = matrix_subtraction(matrix_subtraction(matrix_addition(t1, t5), t3), t7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    return new_matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def multiply_matrices(matrix1, matrix2):
    if matrix_dimensions(matrix1)[1] != matrix_dimensions(matrix2)[0]:
        raise Exception(f'Unable to multiply these matrices, please check the dimensions. \nMatrix A:{matrix1} \nMatrix B:{matrix2}')
    dimension1 = matrix_dimensions(matrix1)
    dimension2 = matrix_dimensions(matrix2)

    if dimension1[0] == dimension1[1] and dimension2[0] == dimension2[1]:
        return matrix1, matrix2

    maximum = max(max(dimension1), max(dimension2))
    maxim = int(math.pow(2, math.ceil(math.log2(maximum))))
    print(max)
    new_matrix1 = matrix1
    new_matrix2 = matrix2
    """
    Adding zeros to the matrices so that the arrays dimensions are the same and also power of 2
    """
    for i in range(0,maxim):
        if i < dimension1[0]:
            for j in range(dimension1[1],maxim):
                new_matrix1[i].append(0)
        else:
            new_matrix1.append([0] * maxim)
        if i < dimension2[0]:
            for j in range(dimension2[1],maxim):
                new_matrix2[i].append(0)
        else:
            new_matrix2.append([0] * maxim)

    final_matrix =  strassen(new_matrix1, new_matrix2)

    """
    Removing the additional zeros
    """
    for i in range(0,maxim):
        if i < dimension1[0]:
            for j in range(dimension2[1],maxim):
                final_matrix[i].pop()
        else:
            final_matrix.pop()
    return final_matrix


if __name__ == '__main__':
    matrix1 = [[2,3,4,5],[6,4,3,1],[2,3,6,7],[3,1,2,4],[2,3,4,5],[6,4,3,1],[2,3,6,7],[3,1,2,4],[2,3,4,5],[6,2,3,1]]
    matrix2 = [[0,2,1,1],[16,2,3,3],[2,2,7,7],[13,11,22,4]]
    print_matrix(multiply_matrices(matrix1,matrix2))
