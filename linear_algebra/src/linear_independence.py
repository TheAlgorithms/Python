# Tablestacks problem for me to convert math logic into code
# Will update with specifications for library if I want to merge, later. Want to optimize too. 
# Done: November 20, 2023 (30 min - 15 math review, 10 programming, 5 test cases)
import numpy as np
import sympy as sp


def is_linIndependent(array):
    # np.any checks if any element is zero, columns or rows. 
    if np.any(np.all(array == 0, axis = 0)):
        return 'Matrix contains a zero vector, is linearly dependent.'
    
    # Checks to make sure we don't have a vector as input. 
    if len(array.shape) != 2:
        return 'Invalid input.'

    # Convert the NumPy array to SymPy matrix so I can use sympy functions
    sympy_matrix = sp.Matrix(array)

    # row reduce matrix, use _ because we don't care about the tuple that's apart of the .rref() return value
    reduced_matrix, _ = sympy_matrix.rref()

    # we can use rank-nullity theorem dim(a) = rank(a) + null(a) to see if the input array returns full rank (all columns (and rows) are linearly independent) or if we have a dimension misalignment
    rank = reduced_matrix.rank()

    # extract column shape since columns are vectors in the matrix
    num_vectors = array.shape[1]

    if rank == num_vectors:
        return 'Matrix is full rank/linearly independent.'
        
    else:
        return 'Matrix is linearly dependent.'


#### Test Cases

test_case_1 = np.array([[1, 2], [3, 4]])  # Linearly independent
test_case_2 = np.array([[1, 2], [2, 4]])  # Linearly dependent
test_case_3 = np.array([[1, 0], [0, 0]])  # Contains zero vector (dependent)
test_case_4 = np.array([1, 2, 3])         # Invalid input (1D array)

# Running the test cases
result_1 = is_linIndependent(test_case_1)
result_2 = is_linIndependent(test_case_2)
result_3 = is_linIndependent(test_case_3)
result_4 = is_linIndependent(test_case_4)

# Additional Test Cases with higher dimensions

# 3D - Linearly independent vectors
test_case_5 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) 

# 4D - Linearly dependent vectors (last vector is a sum of first three)
test_case_6 = np.array([[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]])

# 6D - Linearly independent vectors
test_case_7 = np.array([[1, 0, 0, 0, 0, 0], 
                        [0, 1, 0, 0, 0, 0], 
                        [0, 0, 1, 0, 0, 0], 
                        [0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1]])

# Running the test cases
result_5 = is_linIndependent(test_case_5)
result_6 = is_linIndependent(test_case_6)
result_7 = is_linIndependent(test_case_7)