"""
Given a 2D array, print it in spiral form.

Examples:

Input:  {{1,    2,   3,   4},
              {5,    6,   7,   8},
             {9,   10,  11,  12},
            {13,  14,  15,  16 }}
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation: The output is matrix in spiral format.
"""


def spiralorder(matrix):
    ans = []

    if len(matrix) == 0:
        return ans

    m = len(matrix)
    n = len(matrix[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0

    # Iterate from 0 to R * C - 1
    for i in range(m * n):
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]

        if cr >= 0 and cr < m and cc >= 0 and cc < n and not (seen[cr][cc]):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return ans


# Driver code
if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    # Function call
    for x in spiralorder(a):
        print(x, end=" ")
    print()
