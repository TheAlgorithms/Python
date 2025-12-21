"""
finding tanspose of the given matrix
The transpose of a matrix is a new matrix formed by
flipping the original matrix over its main diagonal,
effectively interchanging its rows and columns
suppose A=[[1,2,3],
           [4,5,6],
           [7,8,9]]
           is the given matix then it's transpose will be
        A^t=[[1,4,7],
             [2,5,8],
             [3,6,9]]
Apporoach:
1. Create a empty(null) matrix of the same size of the given matrix
2.traverse the given matrix by using nested for loop
3.copy the elements in oppposite order of the traversl
i.e. trans[j][i]=matrix[i][j]
"""


def transpose(matrix):
    # create a null matrix of same dimension of given matrix
    trans = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        # row wise traversal
        for j in range(len(matrix[0])):
            # column wise traversal
            trans[j][i] = matrix[i][j]
            # copying the elements in null matrix
    return trans


# checking for main function
if __name__ == "__main__":
    # matrix(given)
    mat = [[1, 2, 3], [4, 5, 6]]
    # call the function with mat as parameter
    print(transpose(mat))
