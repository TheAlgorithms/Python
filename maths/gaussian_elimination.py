def get_matrix_input():
    rows = int(input("Enter the number of equations: "))
    cols = rows + 1  # One additional column for constants

    matrix = []
    for i in range(rows):
        equation = list(map(float, input(f"Enter coefficients for equation {i+1} (space-separated): ").split()))
        matrix.append(equation)

    return matrix

def gaussian_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        # Make the diagonal contain 1
        divisor = matrix[i][i]
        for j in range(i, n+1):
            matrix[i][j] /= divisor

        # Make the other rows contain 0 in this column
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n+1):
                    matrix[k][j] -= factor * matrix[i][j]

    # Extract solutions
    solutions = [row[-1] for row in matrix]
    return solutions

# Get matrix input from user
matrix = get_matrix_input()

# Perform Gaussian elimination
solutions = gaussian_elimination(matrix)

print("Solutions:", solutions)
