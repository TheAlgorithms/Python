import numpy as np

def matrix_factorization_svd(matrix):
    """
    Perform matrix factorization using Singular Value Decomposition (SVD).
    
    Args:
    matrix (list of lists): A 2D matrix to be factorized.
    
    Returns:
    tuple: A tuple containing U, S, and Vt matrices.
    
    Example:
    
    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> U, S, Vt = matrix_factorization_svd(matrix)
    
    >>> U.shape
    (3, 3)
    
    >>> S.shape
    (3,)
    
    >>> Vt.shape
    (3, 3)
    
    >>> reconstructed_matrix = np.dot(U, np.dot(np.diag(S), Vt))
    >>> np.allclose(reconstructed_matrix, matrix, rtol=1e-5, atol=1e-8)
    True
    
    For more information on Singular Value Decomposition (SVD), see:
    https://en.wikipedia.org/wiki/Singular_value_decomposition
    """
    # Convert the input matrix to a NumPy array for numerical operations
    matrix = np.array(matrix)
    
    # Perform SVD
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)
    
    return U, S, Vt

if __name__ == "__main__":
    import doctest
    doctest.testmod()
