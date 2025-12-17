""" "
this program returns the transpose of a given 2-D matrix
The transpose of a matrix is a new matrix formed by flipping the original matrix over its diagonal.

In python a matrix is represented by list inside a list
suppose given matrix A is
    [[4,5,2],
 A= [7,5,9],
    [1,8,3]]
    then it's transpose will be
       [[4,7,1],
 A^t = [5,5,8],
       [3,9,3]]

"""
def transpose_matrix(matrix: list[list[int]]) ->list[list[int]]:
    """""
    creating a new empty matrix for storing transposed values
    number of rows in the matrix=len(matrix)
    number of columns =number of elements in the matrix=number of element in 1st row of the matrix=len(matrix[0])
    """
    transposed_matrix=[[0]*len(matrix) for _ in range(len(matrix[0]))]
    """ 
    created an empty matrix of dimension len(matrix)*len(matrix[0])
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            """ 
    traversing the matrix element-by-element starting from 1st element of 1st row to last element of last row
    1st loop--> traversing through the row
    2nd loop--> traversing through the column
    by this whole matrix is traversing

    """ 
            transposed_matrix[j][i]=matrix[i][j]
        """
        keeping the values of matrix to resultant matrix in transposed order
        for example 2nd element of 3rd row will be 3rd element of 2nd row
                    1nd element of 2rd row will be 2rd element of 1nd row
        likwise diagonal element will reamin intact 

        """    
        #return the transposed_matrix
    return transposed_matrix
"""
check for main function
give input and call the transpose_matrix () function with matirx as a parameter
"""
if __name__=="__main__":
    matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(transpose_matrix(matrix))
