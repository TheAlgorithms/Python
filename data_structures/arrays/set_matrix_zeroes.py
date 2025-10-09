class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        col0 = 1

        # Step 1: Use first row and column as markers
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Update cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: Handle first column
        if col0 == 0:
            for i in range(rows):
                matrix[i][0] = 0
