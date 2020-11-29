"""

 The nqueens problem is of placing N queens on a N * N
 chess board such that no queen can attack any other queens placed
 on that chess board.
 This means that one queen cannot have any other queen on its horizontal, vertical and
 diagonal lines.

"""
solution = []


def isSafe(board: [[int]], row: int, column: int) -> bool:
    """
    This function returns a boolean value True if it is safe to place a queen there
    considering the current state of the board.

    Parameters :
    board(2D matrix) : board
    row ,column : coordinates of the cell on a board

    Returns :
    Boolean Value

    """
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True


def solve(board: [[int]], row: int) -> bool:
    """
    It creates a state space tree and calls the safe function until it receives a
    False Boolean and terminates that branch and backtracks to the next
    possible solution branch.
    """
    if row >= len(board):
        """
        If the row number exceeds N we have board with a successful combination
        and that combination is appended to the solution list and the board is printed.

        """
        solution.append(board)
        printboard(board)
        print()
        return
    for i in range(len(board)):
        """
        For every row it iterates through each column to check if it is feasible to
        place a queen there.
        If all the combinations for that particular branch are successful the board is
        reinitialized for the next possible combination.
        """
        if isSafe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False


def printboard(board: [[int]]) -> None:
    """
    Prints the boards that have a successful combination.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# n=int(input("The no. of queens"))
n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))
