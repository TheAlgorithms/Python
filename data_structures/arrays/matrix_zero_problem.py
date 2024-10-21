def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # To keep track if we need to zero out the first row and first column
    first_row_zero = False
    first_col_zero = False
    
    # Check if the first column should be zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
    
    # Check if the first row should be zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
    
    # Mark zero rows and columns by using the first row and first column
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set matrix cells to zero based on marks
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Zero out the first row if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Zero out the first column if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

# Example input
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# Call the function
setZeroes(matrix)

# Print the result
for row in matrix:
    print(row)
