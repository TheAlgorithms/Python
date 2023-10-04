"""

 The nqueens problem is of placing N queens on a N * N
 chess board such that no queen can attack any other queens placed
 on that chess board.
 This means that one queen cannot have any other queen on its horizontal, vertical and
 diagonal lines.

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


# Implementation using depth first search


r"""

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


def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    boards: list[list[str]],
    n: int,
) -> None:
    """
    >>> boards = []
    >>> depth_first_search([], [], [], boards, 4)
    >>> for board in boards:
    ...     print(board)
    ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
    ['. . Q . ', 'Q . . . ', '. . . Q ', '. Q . . ']
    """

    # Get next row in the current board (possible_board) to fill it with a queen
    row = len(possible_board)

    # If row is equal to the size of the board it means there are a queen in each row in
    # the current board (possible_board)
    if row == n:
        # We convert the variable possible_board that looks like this: [1, 3, 0, 2] to
        # this: ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
        boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])
        return

    # We iterate each column in the row to find all possible results in each row
    for col in range(n):
        # We apply that we learned previously. First we check that in the current board
        # (possible_board) there are not other same value because if there is it means
        # that there are a collision in vertical. Then we apply the two formulas we
        # learned before:
        #
        # 45º: y - x = b or 45: row - col = b
        # 135º: y + x = b or row + col = b.
        #
        # And we verify if the results of this two formulas not exist in their variables
        # respectively.  (diagonal_right_collisions, diagonal_left_collisions)
        #
        # If any or these are True it means there is a collision so we continue to the
        # next value in the for loop.
        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue

        # If it is False we call dfs function again and we update the inputs
        depth_first_search(
            [*possible_board, col],
            [*diagonal_right_collisions, row - col],
            [*diagonal_left_collisions, row + col],
            boards,
            n,
        )


def n_queens_solution(n: int) -> None:
    boards: list[list[str]] = []
    depth_first_search([], [], [], boards, n)

    # Print all the boards
    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solutions were found.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_queens_solution(4)


# Implementation of n queens in sudoku problem


"""
Given a partially filled 9×9 2D array, the objective is to fill a 9×9
square grid with digits numbered 1 to 9, so that every row, column, and
and each of the nine 3×3 sub-grids contains all of the digits.

This can be solved using Backtracking and is similar to n-queens.
We check to see if a cell is safe or not and recursively call the
function on the next column to see if it returns True. if yes, we
have solved the puzzle. else, we backtrack and place another number
in that cell and repeat this process.
"""
from __future__ import annotations

Matrix = list[list[int]]

# assigning initial values to the grid
initial_grid: Matrix = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

# a grid with no solution
no_solution: Matrix = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def is_safe(grid: Matrix, row: int, column: int, n: int) -> bool:
    """
    This function checks the grid to see if each row,
    column, and the 3x3 subgrids contain the digit 'n'.
    It returns False if it is not 'safe' (a duplicate digit
    is found) else returns True if it is 'safe'
    """
    for i in range(9):
        if n in {grid[row][i], grid[i][column]}:
            return False

    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False

    return True


def find_empty_location(grid: Matrix) -> tuple[int, int] | None:
    """
    This function finds an empty location so that we can assign a number
    for that particular row and column.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def sudoku(grid: Matrix) -> Matrix | None:
    """
    Takes a partially filled-in grid and attempts to assign values to
    all unassigned locations in such a way to meet the requirements
    for Sudoku solution (non-duplication across rows, columns, and boxes)

    >>> sudoku(initial_grid)  # doctest: +NORMALIZE_WHITESPACE
    [[3, 1, 6, 5, 7, 8, 4, 9, 2],
     [5, 2, 9, 1, 3, 4, 7, 6, 8],
     [4, 8, 7, 6, 2, 9, 5, 3, 1],
     [2, 6, 3, 4, 1, 5, 9, 8, 7],
     [9, 7, 4, 8, 6, 3, 1, 2, 5],
     [8, 5, 1, 7, 9, 2, 6, 4, 3],
     [1, 3, 8, 9, 4, 7, 2, 5, 6],
     [6, 9, 2, 3, 5, 1, 8, 7, 4],
     [7, 4, 5, 2, 8, 6, 3, 1, 9]]
     >>> sudoku(no_solution) is None
     True
    """
    if location := find_empty_location(grid):
        row, column = location
    else:
        # If the location is ``None``, then the grid is solved.
        return grid

    for digit in range(1, 10):
        if is_safe(grid, row, column, digit):
            grid[row][column] = digit

            if sudoku(grid) is not None:
                return grid

            grid[row][column] = 0

    return None


def print_solution(grid: Matrix) -> None:
    """
    A function to print the solution in the form
    of a 9x9 grid
    """
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


if __name__ == "__main__":
    # make a copy of grid so that you can compare with the unmodified grid
    for example_grid in (initial_grid, no_solution):
        print("\nExample grid:\n" + "=" * 20)
        print_solution(example_grid)
        print("\nExample grid solution:")
        solution = sudoku(example_grid)
        if solution is not None:
            print_solution(solution)
        else:
            print("Cannot find a solution.")
