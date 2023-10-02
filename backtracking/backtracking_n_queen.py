def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            solutions.append(["".join("Q" if cell == 1 else "." for cell in row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions

# Example: Solve the N-Queens problem for N = 4
n = 4
solutions = solve_n_queens(n)

for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
