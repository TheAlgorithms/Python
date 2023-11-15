"""

 The nqueens problem is of placing N queens on a N * N
 chess board such that no queen can attack any other queens placed
 on that chess board.
 This means that one queen cannot have any other queen on its horizontal, vertical and
 diagonal lines.

"""
"""

The N Queens puzzle is a classic problem in computer science and mathematics.
It involves placing N chess queens on an N×N chessboard so that no two queens threaten each other.
The challenge comes from the way queens move in chess: they can move any number of squares vertically, horizontally, or diagonally.
Therefore, the solution to the puzzle requires that no two queens share the same row, column, or diagonal.

"""


def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col, solutions):
    if col >= len(board):
        solutions.append([row[:] for row in board])
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve(board, col + 1, solutions) or res
            board[i][col] = 0

    return res


def printboard(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


# Main code
n = 8
board = [[0] * n for _ in range(n)]
solutions = []
solve(board, 0, solutions)

for sol in solutions:
    printboard(sol)
    print()

print("The total number of solutions are:", len(solutions))
