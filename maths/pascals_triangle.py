"""/**
 * Pascal's Triangle is an array of binomial coefficients. It can be used for unwrapping terms like
 * (a + b)^5.
 * To construct Pascal's Triangle you add the numbers above the child entry together. Here are the first five rows:
 *     1
 *    1 1
 *   1 2 1
 *  1 3 3 1
 * 1 4 6 4 1
 *
 * Time Complexity: quadratic (O(n^2)).
 * @see https://en.wikipedia.org/wiki/Pascal's_triangle
 */ """

# Importing the numpy library as np for numerical operations
import numpy as np

def pascal(n: int):
    """
    Generate Pascal's triangle up to the n-th row.
    Parameters:
    n (int): The number of rows in Pascal's triangle to generate.
    Returns:
    np.ndarray: A 2D numpy array containing the first n rows of Pascal's triangle.
    """
    # Initialize a 2D numpy array with zeros, with shape (n,n) and integer type
    pascal_array = np.zeros((n, n), dtype=np.int64)
    # Set the first column of all rows to 1 (the edge values of Pascal's triangle)
    pascal_array[:, 0] = 1
    
    # Fill the pascal_array with the correct values for Pascal's triangle
    for i in range(1, n):
        # Each element except the edges is the sum of the two directly above it
        # pascal_array[i, 1:n] = pascal_array[i-1, 1:n] + pascal_array[i-1, 0:n-1]
        pascal_array[i,1:i+1] = pascal_array[i-1,1:i+1] + pascal_array[i-1,0:i]
    
    return pascal_array

def show_pascal(pascal_array):
    """
    Print Pascal's triangle in a formatted manner.
    Parameters:
    pascal_array (np.ndarray): A 2D numpy array containing Pascal's triangle.
    """
    # Get the number of rows and columns (should be equal)
    n, m = pascal_array.shape[:2]
    # Ensure the array is square (n == m), as required for Pascal's triangle
    assert n == m
    
    # Loop through each row and print the values up to the current row index
    for i in range(n):
        for j in range(i + 1):
            print(pascal_array[i, j], end=" ")
        print()

# Main execution block
if __name__ == '__main__':
    # Display Pascal's triangle for 10 rows
    show_pascal(pascal(10))
