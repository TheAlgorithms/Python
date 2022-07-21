"""
Cofactor expansion is a recursive method to calculate the determinant
of a NxN matrix.

You can read more about it here:        
https://people.math.carleton.ca/~kcheung/math/notes/MATH1107/wk07/07_cofactor_expansion.html        
"""


def determinant(matrix: list) -> int or float:
    """
    Return the determinant of matrix

    >>> determinant([[1]])
    1
    >>> determinant([[1,2],[1,2]])
    0
    >>> determinant([[1,2],[1,3]])
    1
    >>> determinant([[1,2,3],[4,5,6],[7,8,9]])
    0
    >>> determinant([[0,0,0],[12,15,1],[6,9,5]])
    0
    >>> determinant([[0, 3, 1, 5, 1, 1],[5, 2, 1, 3, 1, 1],[3, 5, 0, 1, 2, 3],[1, 3, 0, 1, 4, 5],[1, 9, 0, 7, 1, 5],[2, 5, 0, 7, 6, 5]])
    1986
    >>> determinant([[5,6,1,-5],[12,-10,2,14.5],[0,0.5,1.2,5.1],[9.2,14,-15,16]])
    -15758.410000000003
    >>> determinant([[3000,1,3123,-5123],[3123,32,3,1],[0,213,0,-12312],[0,213,0,-12312]])
    0
    """

    dimension = len(matrix)
    det = 0

    # trivial cases
    if dimension == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if dimension == 1:
        return matrix[0][0]

    # general case
    for i in range(dimension):
        det += (-1)**(i) * determinant(aux_matrix(matrix, 0, i))*matrix[0][i]
    return det


def aux_matrix(matrix: list, i: int, j: int) -> list:
    """
    returns a new matrix without the row i and the column j from 
    matrix

    >>> aux_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0)
    [[5, 6], [8, 9]]
    >>> aux_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 1)
    [[1, 3], [4, 6]]
    >>> aux_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2)
    [[1, 2], [7, 8]]
    """
    mat = []
    for row_i, row in enumerate(matrix):
        if row_i != i:
            aux = []
            for column_j, value in enumerate(row):
                if column_j != j:
                    aux.append(value)
            mat.append(aux)
    return mat


if __name__ == "__main__":
    matrix = [
        [0, 3, 1, 5, 1, 1],
        [5, 2, 1, 3, 1, 1],
        [3, 5, 0, 1, 2, 3],
        [1, 3, 0, 1, 4, 5],
        [1, 9, 0, 7, 1, 5],
        [2, 5, 0, 7, 6, 5]
    ]
    dimension = len(matrix)
    for row in matrix:
        if type(row) != list:
            raise TypeError("A matrix must be a list of lists")
        if len(row) != dimension:
            raise TypeError(f"The matrix must be {dimension}x{dimension}")
    print(determinant(matrix))
