r"""
Problem:

The n queens problem is: placing N queens on a N * N chess board such that no queen
can attack any other queens placed on that chess board.  This means that one queen
cannot have any other queen on its horizontal, vertical and diagonal lines.

Solution:

To solve this problem we will use simple math. First we know the queen can move in all
the possible ways, we can simplify it in this: vertical, horizontal, diagonal left and
 diagonal right.

We can visualize it like this:

left diagonal = \
right diagonal = /

On a chessboard vertical movement could be the rows and horizontal movement could be
the columns.

In programming we can use an array, and in this array each index could be the rows and
each value in the array could be the column. For example:

    . Q . .     We have this chessboard with one queen in each column and each queen
    . . . Q     can't attack to each other.
    Q . . .     The array for this example would look like this: [1, 3, 0, 2]
    . . Q .

So if we use an array and we verify that each value in the array is different to each
other we know that at least the queens can't attack each other in horizontal and
vertical.

At this point we have it halfway completed and we will treat the chessboard as a
Cartesian plane.  Hereinafter we are going to remember basic math, so in the school we
learned this formula:

    Slope of a line:

           y2 - y1
     m = ----------
          x2 - x1

This formula allow us to get the slope. For the angles 45º (right diagonal) and 135º
(left diagonal) this formula gives us m = 1, and m = -1 respectively.

See::
https://www.enotes.com/homework-help/write-equation-line-that-hits-origin-45-degree-1474860

Then we have this other formula:

Slope intercept:

y = mx + b

b is where the line crosses the Y axis (to get more information see:
https://www.mathsisfun.com/y_intercept.html), if we change the formula to solve for b
we would have:

y - mx = b

And since we already have the m values for the angles 45º and 135º, this formula would
look like this:

45º: y - (1)x = b
45º: y - x = b

135º: y - (-1)x = b
135º: y + x = b

y = row
x = column

Applying these two formulas we can check if a queen in some position is being attacked
for another one or vice versa.

"""
from __future__ import annotations

solution = []


def is_safe(board: list[list[int]], row: int, column: int) -> bool:
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


def solve(board: list[list[int]], row: int) -> bool:
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
        return True
    for i in range(len(board)):
        """
        For every row it iterates through each column to check if it is feasible to
        place a queen there.
        If all the combinations for that particular branch are successful the board is
        reinitialized for the next possible combination.
        """
        if is_safe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False


def printboard(board: list[list[int]]) -> None:
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
