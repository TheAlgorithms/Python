import numpy as np

# Create two matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result_multiply = np.dot(matrix_a, matrix_b)

# Matrix addition
result_add = matrix_a + matrix_b

# Calculate the determinant of matrix_a
determinant_a = np.linalg.det(matrix_a)

# Print the results
print("Matrix A:")
print(matrix_a)

print("Matrix B:")
print(matrix_b)

print("Matrix Multiplication (A * B):")
print(result_multiply)

print("Matrix Addition (A + B):")
print(result_add)

print("Determinant of Matrix A:")
print(determinant_a)
