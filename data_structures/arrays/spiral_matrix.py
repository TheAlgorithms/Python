class Solution:
    def generate_matrix(self, n: int) -> list[list[int]]:
        """Generate an n x n spiral matrix filled with numbers from 1 to n^2."""

        # Create an n x n matrix filled with zeros
        result = [[0] * n for _ in range(n)]

        # Start filling numbers from 1 to n^2
        value = 1

        # Define the boundaries for rows and columns
        row_start, row_end = 0, n - 1
        col_start, col_end = 0, n - 1

        # Continue filling the matrix layer by layer in spiral order
        while row_start <= row_end and col_start <= col_end:
            # Step 1: Fill the top row (left → right)
            for i in range(col_start, col_end + 1):
                result[row_start][i] = value   # assign the current value
                value += 1                    # move to next number
            row_start += 1  # move top boundary down (row filled)
            
            # Step 2: Fill the rightmost column (top → bottom)
            for row in range(row_start, row_end + 1):
                result[row][col_end] = value
                value += 1
            col_end -= 1  # move right boundary left (column filled)
            
            # Step 3: Fill the bottom row (right → left)
            # Only if there are rows remaining to fill
            if row_start <= row_end:
                for col in range(col_end, col_start - 1, -1):
                    result[row_end][col] = value
                    value += 1
                row_end -= 1  # move bottom boundary up (row filled)
            
            # Step 4: Fill the leftmost column (bottom → top)
            # Only if there are columns remaining to fill
            if col_start <= col_end:
                for row in range(row_end, row_start - 1, -1):
                    result[row][col_start] = value
                    value += 1
                
                col_start += 1

        # return the completed spiral matrix
        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 3  # Change this to any number, e.g., 4 or 5
    matrix = solution.generate_matrix(n)

    # Print the spiral matrix row by row
    for row in matrix:
        print(row)


# Output: 
'''
    [1, 2, 3]
    [8, 9, 4]
    [7, 6, 5]

'''
