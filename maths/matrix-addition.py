""" add two matrices that are the same size"""

def add(matrix_a, matrix_b):
    """
    >>> add([[0, 1], [0, 0]], [[0, 1], [0, 0]])
    [[0, 2], [0, 0]]
    >>> add([[7, 1], [5, 0]], [[0, 1], [3, 2]])
    [[7, 2], [8, 2]]
    """
    row_index = 0
    column_index = 0

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise Exception("Matrices must be the same size")

    for row in matrix_a:
        for column in matrix_a:
            matrix_a[row_index][column_index] = matrix_a[row_index][column_index] + matrix_b[row_index][column_index]
            column_index = column_index + 1
        row_index = row_index + 1
        column_index = 0

    return matrix_a


if __name__ == "__main__":
    a = [[0, 1], [0, 0]]
    b = [[0, 1], [0, 0]]
    sum = add(a, b)
    print(f"The sum of {a} + {b} is {sum}")

