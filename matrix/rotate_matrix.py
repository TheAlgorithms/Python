# -*- coding: utf-8 -*-

"""
	In this problem, we want to rotate the matrix elements by 90, 180, 270 (counterclockwise)
	Discussion in stackoverflow: 
   https://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array
"""


def rotate_90(matrix: [[]]):
    """
    >>> rotate_90([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
    """
    
    transpose(matrix)
    reverse_row(matrix)
    return matrix
    

def rotate_180(matrix: [[]]):
    """
    >>> rotate_180([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
    """
    
    reverse_column(matrix)
    reverse_row(matrix)
    
    """
    OR
    
    reverse_row(matrix)
    reverse_column(matrix)
    """
    
    return matrix

    
def rotate_270(matrix: [[]]):
    """
    >>> rotate_270([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    """
    
    transpose(matrix)
    reverse_column(matrix)
    
    """
    OR
    
    reverse_row(matrix)
    transpose(matrix)
    """
    
    return matrix


def transpose(matrix: [[]]):
    matrix[:] = [list(x) for x in zip(*matrix)]
    return matrix
    
    
def reverse_row(matrix: [[]]):
    matrix[:] = matrix[::-1]
    return matrix


def reverse_column(matrix: [[]]):
    matrix[:] = [x[::-1] for x in matrix]
    return matrix
    
    
def print_matrix(matrix: [[]]):
    for i in matrix:
        print(*i)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("\norigin:\n")
    print_matrix(matrix)
    rotate_90(matrix)
    print("\nrotate 90 counterclockwise:\n")
    print_matrix(matrix)

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("\norigin:\n")
    print_matrix(matrix)
    rotate_180(matrix)
    print("\nrotate 180:\n")
    print_matrix(matrix)

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("\norigin:\n")
    print_matrix(matrix)
    rotate_270(matrix)
    print("\nrotate 270 counterclockwise:\n")
    print_matrix(matrix)
