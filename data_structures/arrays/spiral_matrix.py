class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]
        value = 1
        
        colStart, colEnd = 0, n - 1
        rowStart, rowEnd = 0, n - 1

        while colStart <= colEnd and rowStart <= rowEnd:
            # Left to Right
            for i in range(colStart, colEnd + 1):
                result[rowStart][i] = value
                value += 1
            rowStart += 1
            
            # Up to Down
            for j in range(rowStart, rowEnd + 1):
                result[j][colEnd] = value
                value += 1
            colEnd -= 1
            
            # Right to Left
            if rowStart <= rowEnd:
                for k in range(colEnd, colStart - 1, -1):
                    result[rowEnd][k] = value
                    value += 1
                rowEnd -= 1
            
            # Down to Up
            if colStart <= colEnd:
                for l in range(rowEnd, rowStart - 1, -1):
                    result[l][colStart] = value
                    value += 1
                colStart += 1

        return result


# Test
solution = Solution()

n = 3

matrix = solution.generateMatrix(n)

# Print the matrix
for row in matrix:
    print(row)
