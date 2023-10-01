import numpy as np

def add_matrices(matrix_a, matrix_b):
    """
    Add two matrices.

    Args:
        matrix_a (numpy.ndarray): The first matrix.
        matrix_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix addition.
        
    Raises:
        ValueError: If the input matrices have incompatible shapes.

    Example:
        >>> add_matrices(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))
        array([[ 6,  8],
               [10, 12]])
    """
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("Matrix dimensions are not compatible for addition.")
    return np.add(matrix_a, matrix_b)

def subtract_matrices(matrix_a, matrix_b):
    """
    Subtract one matrix from another.

    Args:
        matrix_a (numpy.ndarray): The matrix from which to subtract.
        matrix_b (numpy.ndarray): The matrix to subtract.

    Returns:
        numpy.ndarray: The result of the matrix subtraction.
        
    Raises:
        ValueError: If the input matrices have incompatible shapes.

    Example:
        >>> subtract_matrices(np.array([[5, 6], [7, 8]]), np.array([[1, 2], [3, 4]]))
        array([[4, 4],
               [4, 4]])
    """
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("Matrix dimensions are not compatible for subtraction.")
    return np.subtract(matrix_a, matrix_b)

def multiply_matrices(matrix_a, matrix_b):
    """
    Multiply two matrices.

    Args:
        matrix_a (numpy.ndarray): The first matrix.
        matrix_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.
        
    Raises:
        ValueError: If the number of columns in matrix_a does not match the number of rows in matrix_b.

    Example:
        >>> multiply_matrices(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))
        array([[19, 22],
               [43, 50]])
    """
    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("Matrix dimensions are not compatible for multiplication.")
    return np.matmul(matrix_a, matrix_b)

def calculate_determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (numpy.ndarray): The square matrix for which to calculate the determinant.

    Returns:
        float: The determinant of the matrix.
        
    Raises:
        ValueError: If the input matrix is not square.

    Example:
        >>> calculate_determinant(np.array([[1, 2], [3, 4]]))
        -2.0
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square to calculate its determinant.")
    return np.linalg.det(matrix)
