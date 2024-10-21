def setMatrixZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # To store which rows and columns are supposed to be marked with zeroes
    row = [0] * n
    col = [0] * m

    # Traverse the matrix using nested loops
    for i in range(n):
        for j in range(m):
            # If the cell contains zero, mark its row and column
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    # Update the matrix
    for i in range(n):
        for j in range(m):
            # Set cells to zero if any of the row[i] or col[j] is marked
            if row[i] or col[j]:
                matrix[i][j] = 0

    # Print the updated matrix
    for row in matrix:
        print(" ".join(map(str, row)))


# Driver Code
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Initialize matrix from user input
matrix = []
print("Enter the elements row-wise (space-separated):")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Function call
setMatrixZeroes(matrix)
