from typing import List

def get_matrix_input() -> List[List[float]]:
    """
    Gets input for the coefficient matrix augmented with constants.

    Returns:
        A list of lists representing the matrix.
        
    Example:
    >>> input_data = "2\\n2 -1 1 8\\n-3 3 2 1"
    >>> from io import StringIO
    >>> import sys
    >>> sys.stdin = StringIO(input_data)
    >>> matrix = get_matrix_input()
    >>> matrix
    [[2.0, -1.0, 1.0, 8.0], [-3.0, 3.0, 2.0, 1.0]]
    """
    print("Enter the number of equations:", end=" ")
    num_eq = int(input())
    print(f"Enter coefficients for {num_eq} equations (one row at a time):")
    
    matrix = []
    for _ in range(num_eq):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    return matrix

def gaussian_elimination(matrix: List[List[float]]) -> List[float]:
    """
    This function applies the Gaussian Elimination method to solve a system of linear equations.

    Args:
        matrix: Coefficient matrix augmented with constants.

    Returns:
        A list containing the solutions to the system of equations.
        
    Example:
    >>> matrix = [[2.0, -1.0, 1.0, 8.0], [-3.0, 3.0, 2.0, 1.0]]
    >>> solutions = gaussian_elimination(matrix)
    >>> solutions
    [3.8888888888888875, 2.4444444444444438]
    """
    n = len(matrix)

    # Gaussian Elimination
    for i in range(n):
        # Make the diagonal element 1
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        # Make other elements in the column zero
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    # Extract solutions
    solutions = [row[-1] for row in matrix]

    return solutions

if __name__ == "__main__":
    matrix = get_matrix_input()
    solutions = gaussian_elimination(matrix)
    print("Solutions:", [round(sol, 3) for sol in solutions])
