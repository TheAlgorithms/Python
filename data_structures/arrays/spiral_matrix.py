class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Create an n x n matrix filled with zeros
        result = [[0] * n for _ in range(n)]
        
        # Start filling numbers from 1 to n^2
        value = 1
        
        # Define the boundaries for rows and columns
        rowStart, rowEnd = 0, n - 1
        colStart, colEnd = 0, n - 1

        # Continue filling the matrix layer by layer in spiral order
        while rowStart <= rowEnd and colStart <= colEnd:
            
            # Step 1: Fill the top row (left → right)
            for i in range(colStart, colEnd + 1):
                result[rowStart][i] = value   # assign the current value
                value += 1                    # move to next number
            rowStart += 1  # move top boundary down (row filled)
            
            # Step 2: Fill the rightmost column (top → bottom)
            for j in range(rowStart, rowEnd + 1):
                result[j][colEnd] = value
                value += 1
            colEnd -= 1  # move right boundary left (column filled)
            
            # Step 3: Fill the bottom row (right → left)
            # Only if there are rows remaining to fill
            if rowStart <= rowEnd:
                for k in range(colEnd, colStart - 1, -1):
                    result[rowEnd][k] = value
                    value += 1
                rowEnd -= 1  # move bottom boundary up (row filled)
            
            # Step 4: Fill the leftmost column (bottom → top)
            # Only if there are columns remaining to fill
            if colStart <= colEnd:
                for l in range(rowEnd, rowStart - 1, -1):
                    result[l][colStart] = value
                    value += 1
                colStart += 1  # move left boundary right (column filled)

        # Return the completed spiral matrix
        return result


# Example usage:
solution = Solution()

n = 3  # You can change this to any number, e.g. 4 or 5
matrix = solution.generateMatrix(n)

# Print the spiral matrix row by row
for row in matrix:
    print(row)


# Output: 
'''
    [1, 2, 3]
    [8, 9, 4]
    [7, 6, 5]

'''