"""              Matrix Determinant             """

"""
        Cofactor expansion is a recursive method to calculate the determinant
        of a NxN matrix.
        
        
        - The Cofactor Expansion:
        
        Given a matrix NxN A, its determinant can be calculated doing this:
        
        det(A) = (-1)**(i+0)*det(A(i|0))*Ai0 
                + (-1)**(i+1)*det(A(i|1))*Ai1 + ...
                + (-1)**(i+n-1)*det(A(i|n-1))*Ain-1
        
        Example:
        
        Let A = [[1,2,3],  
                 [4,5,6],
                 [7,8,9]]
                 
        det(A) = (-1)**(0)*det(A(1|1))*A[0][0] 
                + (-1)**(1)*det(A(1|2))*A[0][1] 
                + (-1)**(2)*det(A(1|3))*A[0][2]
               = 
                   det([[5,6],[8,9]])*1 
                 - det([[4,6],[7,9]])*2 
                 + det([[4,5],[7,8]])*3 =
               = -3 - 2*(-6) + 3(-3)
               = 0        
        
        
        
        -The Definition of A(i|j):
        
        
        Let A be an NxN matrix. We define A(i|j) to be the matrix obtained 
        from A by removing row i and column j from A.
        
        Example:
        
        Let A = [[1,2,3],  
                 [4,5,6],
                 [7,8,9]]
                 
        Then, A(1|1) = [[5,6],
                        [8,9]], 
              A(2|2) = [[1,3], 
                        [7,9]], 
              A(3|1) = [[2,3],
                        [5,6]]
                
        source: https://people.math.carleton.ca/~kcheung/math/notes/MATH1107/wk07/07_cofactor_expansion.html        
"""


def determinant(matrix):
    n = len(matrix)
    det = 0

    # trivial cases
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if n == 1:
        return matrix[0]

    # general case
    for i in range(n):
        det += (-1)**(i) * determinant(aux_matrix(matrix, 0, i))*matrix[0][i]
    return det


def aux_matrix(matrix, i, j):
    """
    returns a new matrix without the row i and the column j from 
    matrix
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
    print(determinant(matrix))  # = 1986 :D
