import numpy as np

def rayleigh_quotient(input_matrix: np.array, vector: np.array):

    num = np.dot(vector.T, np.dot(input_matrix, vector))
    den = np.dot(vector.T,vector)

    return num/den

def power_iteration(input_matrix: np.array,vector: np.array,
    error_tol = 1e-12, max_iterations=100) -> [float, np.array]:

    """
    Input
    input_matrix: input matrix whose largest eigenvalue we will find.
    Numpy array. np.shape(matrix) == (N,N).
    vector: random initial vector in same space as matrix.
    Numpy array. np.shape(init_vector) == (N,) or (N,1)

    Output
    largest_eigenvalue: largest eigenvalue of the matrix input_matrix.
    Float. Scalar.
    largest_eigenvector: eigenvector corresponding to largest_eigenvalue.
    Numpy array. np.shape(largest_eigenvector) == (N,) or (N,1).
    """

    #Ensure matrix is square.
    assert(np.shape(input_matrix)[0] == np.shape(input_matrix)[1])
    #Ensure proper dimensionality.
    assert(np.shape(input_matrix)[0] == np.shape(vector)[0])

    #Set convergence to False. Will define convergence when we exceed max_iterations
    # or when we have small changes from one iteration to next.

    convergence = False
    lamda_previous = 0
    iterations = 0
    error = 1e12

    while (convergence == False):
        w = np.dot(input_matrix,vector)
        vector = w / np.linalg.norm(w)
        lamda = np.dot(vector.T, np.dot(input_matrix, vector))

        #Check convergence.
        error = np.abs(lamda - lamda_previous)/lamda
        iterations += 1

        if (error <= error_tol or iterations >= max_iterations):
            convergence = True

        lamda_previous = lamda


    return lamda, vector


if __name__ == "__main__":
    # Perform a test of power iteration by comparing to built in numpy.linalg.eigh

    # Example
    np.random.seed(100)
    #Set dimension of space
    n = 10

    #Create random matrix in space R^{nxn}
    A = np.random.rand(n,n)
    #Ensure matrix A is Symmetric
    A = np.dot(A.T,A)
    #Create random vector in space R^n
    v = np.random.rand(n)

    # Find eigenvalues using python built in library.
    # https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html
    # The function will return eignevalues in ascending order and eigenvectors correspondingly.
    # The last element is the largest eigenvalue and eigenvector index.
    eigenvalues, eigenvectors =  np.linalg.eigh(A)
    largest_eigenvalue = eigenvalues[-1]
    largest_eigenvector = eigenvectors[:,-1]

    print('#########################################################')
    print('From Numpy built in library.')
    print(f'Largest Eigenvalue: {largest_eigenvalue}')
    print(f'Largest Eigenvector: {largest_eigenvector}')
    # Now try our own code
    largest_eigenvalue_power, largest_eigenvector_power = power_iteration(A,v)
    print('#########################################################')
    print('From Power Iteration we wrote.')
    print(f'Largest Eigenvalue: {largest_eigenvalue_power}')
    print(f'Largest Eigenvector: {largest_eigenvector_power}')

    abs_error = np.abs(largest_eigenvalue - largest_eigenvalue_power)
    rel_error = abs_error/largest_eigenvalue
    print('#########################################################')
    print('Eigenvalue Error Between Numpy and our implementation.')
    print(f'Absolute Error: {abs_error}')
    print(f'Relative Error: {rel_error}')

    abs_error = np.linalg.norm(largest_eigenvector-largest_eigenvector_power)
    cos_error = np.arccos(np.dot(largest_eigenvector,largest_eigenvector_power))
    print('#########################################################')
    print('Eigenvector Error Between Numpy and our implementation.')
    print(f'Absolute norm difference: {abs_error}')
    print(f'Cosign error between eigenvectors: {cos_error}')
