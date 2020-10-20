"""
Project Euler Problem 096 : https://projecteuler.net/problem=96

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. 
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented 
a similar, and much more difficult, puzzle idea called Latin Squares. The objective of
Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such
that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an
example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, 
although it may be necessary to employ "guess and test" methods in order to eliminate 
options (there is much contested opinion over this). The complexity of the search 
determines the difficulty of the puzzle; the example above is considered easy because 
it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty
different Su Doku puzzles ranging in difficulty, but all with unique solutions 
(the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left
corner of each solution grid; for example, 483 is the 3-digit number found in the top
left corner of the solution grid above.
"""


def nextUnsolvedBoard(file_lines_array: list, last_grid: int = 0) -> tuple:

    r"""
    Search a list containing the lines of the sudoku input for the next unsolved board
    based on the number of the last solved one
    Parameters:
        file_lines_array -> string list containing the input file lines;
        last_grid -> integer for the last solved board, default 0
    Returns tuple with, a 9x9 integer matrix containing the next unsolved board in the 
        array and the number of the new board as labeled by the list

    >>> nextUnsolvedBoard(['Grid 01\n', '003020600\n', '900305001\n', '001806400\n', '008102900\n', '700000008\n', '006708200\n', '002609500\n', '800203009\n', '005010300\n'])
    ([[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]], 1)
    >>> nextUnsolvedBoard(['Grid 01\n', '003020600\n', '900305001\n', '001806400\n', '008102900\n', '700000008\n', '006708200\n', '002609500\n', '800203009\n', '005010300\n', 'Grid 02\n', '200080300\n', '060070084\n', '030500209\n', '000105408\n', '000000000\n', '402706000\n', '301007040\n', '720040060\n', '004010003\n'], 1)
    ([[2, 0, 0, 0, 8, 0, 3, 0, 0], [0, 6, 0, 0, 7, 0, 0, 8, 4], [0, 3, 0, 5, 0, 0, 2, 0, 9], [0, 0, 0, 1, 0, 5, 4, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 2, 7, 0, 6, 0, 0, 0], [3, 0, 1, 0, 0, 7, 0, 4, 0], [7, 2, 0, 0, 4, 0, 0, 6, 0], [0, 0, 4, 0, 1, 0, 0, 0, 3]], 2)
    """

    # Iterate the list of lines starting from the number
    # of the last solved sudoku*10, thus the index of the line where it starts,
    # since the first one starts at 0 and there is 10 lines per sudoku
    for line in range(last_grid * 10, len(file_lines_array)):
        # Verify if the current line is the head of the sudoku
        if file_lines_array[line][0] == "G":

            # Read the next 9 lines and cast each of it's digits and integers
            return (
                [
                    [int(file_lines_array[line + j][i]) for i in range(0, 9)]
                    for j in range(1, 10)
                ]
                # Cast the last two digits of the sudoku's head line, aka the sudoku's
                # board number, as integer(the last character is \n, so we
                # desconsider it)
                ,
                int(file_lines_array[line][-3] + file_lines_array[line][-2]),
            )
    return [], last_grid


def nextUnsolvedCell(board: list, row: int, col: int) -> tuple:

    """
    Search the sudoku matrix for the next unsolved position, represented by 0
    Parameters:
        board -> 9x9 integer matrix;
        row -> integer refering the row of the last modified value in the matrix;
        col -> integer refering the column of the last modified value in the matrix
    Returns tuple containing the row and column of the first found 0 in the matrix

    >>> nextUnsolvedCell([[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]], 0, 0)
    (0, 0)
    >>> nextUnsolvedCell([[2, 0, 0, 0, 8, 0, 3, 0, 0], [0, 6, 0, 0, 7, 0, 0, 8, 4], [0, 3, 0, 5, 0, 0, 2, 0, 9], [0, 0, 0, 1, 0, 5, 4, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 2, 7, 0, 6, 0, 0, 0], [3, 0, 1, 0, 0, 7, 0, 4, 0], [7, 2, 0, 0, 4, 0, 0, 6, 0], [0, 0, 4, 0, 1, 0, 0, 0, 3]], 0, 0)
    (0, 1)
    """

    # Search for next unsolved cell on the proximities
    for y in range(row, 9):
        for x in range(col, 9):
            if board[y][x] == 0:
                return y, x
    # Search for next unsolved cell on the whole board
    for y in range(0, 9):
        for x in range(0, 9):
            if board[y][x] == 0:
                return y, x
    return -1, -1


def isValid(board: list, row: int, col: int, val: int) -> bool:

    """
    Verify if val parameter is repeated either in the row, column or 3x3 section 
        of the sudoku matrix
    Parameters:
        board -> 9x9 integer matrix;
        row -> integer refering the row of the value to be verified in the matrix;
        col -> integer refering the column of the value to be verified in the matrix;
        val -> integer refering the value to be verified
    Returns True if no doble of the value was found and False otherwise

    >>> isValid([[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]], 0, 0, 4)
    True
    >>> isValid([[2, 0, 0, 0, 8, 0, 3, 0, 0], [2, 6, 0, 0, 7, 0, 0, 8, 4], [0, 3, 0, 5, 0, 0, 2, 0, 9], [0, 0, 0, 1, 0, 5, 4, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 2, 7, 0, 6, 0, 0, 0], [3, 0, 1, 0, 0, 7, 0, 4, 0], [7, 2, 0, 0, 4, 0, 0, 6, 0], [0, 0, 4, 0, 1, 0, 0, 0, 3]], 1, 0, 2)
    False
    """

    # Verify if all values in the row and the column are different from val
    if all([val != board[row][x] for x in range(9)]) and all(
        [val != board[y][col] for y in range(9)]
    ):

        # Find the X and Y position of the top left corner of the current sector
        secTopLeftX, secTopLeftY = col - col % 3, row - row % 3

        # Iterate the sudoku 3x3 sector
        for i in range(secTopLeftY, secTopLeftY + 3):
            for j in range(secTopLeftX, secTopLeftX + 3):
                if board[i][j] == val:
                    return False

        # Everything OK
        return True
    return False


def solveBoard(board: list, row: int = 0, col: int = 0) -> list:

    """
    Recursively solve a sudoku given in a 9x9 integer matrix format
    Parameters:
        board -> 9x9 integer matrix,
        row: integer ->  the row of the last modified value in the matrix, default 0
        col: integer ->  the column of the last modified value in the matrix, default 0
    Returns a 9x9 integer solved sudoku matrix or 
        a empty list in case it couldn't be solved

    >>> solveBoard([[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]])
    [[4, 8, 3, 9, 2, 1, 6, 5, 7], [9, 6, 7, 3, 4, 5, 8, 2, 1], [2, 5, 1, 8, 7, 6, 4, 9, 3], [5, 4, 8, 1, 3, 2, 9, 7, 6], [7, 2, 9, 5, 6, 4, 1, 3, 8], [1, 3, 6, 7, 9, 8, 2, 4, 5], [3, 7, 2, 6, 8, 9, 5, 1, 4], [8, 1, 4, 2, 5, 3, 7, 6, 9], [6, 9, 5, 4, 1, 7, 3, 8, 2]]
    >>> solveBoard([[2, 0, 0, 0, 8, 0, 3, 0, 0], [0, 6, 0, 0, 7, 0, 0, 8, 4], [0, 3, 0, 5, 0, 0, 2, 0, 9], [0, 0, 0, 1, 0, 5, 4, 0, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 2, 7, 0, 6, 0, 0, 0], [3, 0, 1, 0, 0, 7, 0, 4, 0], [7, 2, 0, 0, 4, 0, 0, 6, 0], [0, 0, 4, 0, 1, 0, 0, 0, 3]])
    [[2, 4, 5, 9, 8, 1, 3, 7, 6], [1, 6, 9, 2, 7, 3, 5, 8, 4], [8, 3, 7, 5, 6, 4, 2, 1, 9], [9, 7, 6, 1, 2, 5, 4, 3, 8], [5, 1, 3, 4, 9, 8, 6, 2, 7], [4, 8, 2, 7, 3, 6, 9, 5, 1], [3, 9, 1, 6, 5, 7, 8, 4, 2], [7, 2, 8, 3, 4, 9, 1, 6, 5], [6, 5, 4, 8, 1, 2, 7, 9, 3]]
    """

    # Search for next unsolved position
    y, x = nextUnsolvedCell(board, row, col)

    # End the function in case we checked the whole board
    if y == -1:
        return board

    # Start guessing values from 1 to 10 and verify if valid
    for v in range(1, 10):
        if isValid(board, y, x, v):
            board[y][x] = v
            # Try to solve the next unsolved cell recursively
            if solveBoard(board, y, x):
                return board

            board[y][x] = 0
    return []


def solution(path: str = "p096_sudoku.txt") -> list:

    """
    Solve the Eulers Challenge #096 by solving each one of the 50 sudokus in the file
    provided by the official website
    Parameters:
        path:string -> the path for the .txt file containing the
    Returns list containing the concatenated three first values of
        each solved sudoku matrix

    >>> solution()
    [483, 245, 462, 137, 523, 176, 143, 487, 814, 761, 976, 962, 397, 639, 697, 361, 359, 786, 743, 782, 428, 425, 348, 124, 361, 581, 387, 345, 235, 298, 761, 132, 698, 852, 453, 516, 945, 365, 134, 193, 814, 384, 469, 316, 586, 954, 159, 861, 294, 351]
    """

    # Array for storing each one of the sudoku's solutions
    sums = []
    # Number of the last solved sudoku according to the file
    grid_n = 0
    try:
        with open(path, "r") as f:
            # Store all file's lines in a list
            lines = f.readlines()
            while grid_n < 50:
                # Retrieve board and board number from lines list
                board, grid_n = nextUnsolvedBoard(lines, grid_n)
                if board:
                    solution = solveBoard(board)
                # If solution was found, append the first 3 digits of the solution 
                # to the sums array
                if solution:
                    sums.append(int("".join([str(i) for i in solution[0][:3]])))
    except FileNotFoundError:
        return("Input file not found or couldn't be opened")

    return sums


if __name__ == "__main__":
    print(solution())
