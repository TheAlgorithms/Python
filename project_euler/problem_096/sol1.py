"""
Project Euler Problem 96: https://projecteuler.net/problem=96

Problem Statement:
Su Doku (Japanese meaning number place) is the name given to a popular puzzle
concept. Its origin is unclear, but credit must be attributed to Leonhard
Euler who invented a similar, and much more difficult, puzzle idea called
Latin Squares. The objective of Su Doku puzzles, however, is to replace
the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and
3 by 3 box contains each of the digits 1 to 9. Below is an example of a
typical starting puzzle grid and its solution grid.

003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300

483921657
967345821
251876493
548132976
729564138
136798245
372689514
814253769
695417382

A well constructed Su Doku puzzle has a unique solution and can be
solved by logic, although it may be necessary to employ "guess and test"
methods in order to eliminate options (there is much contested opinion over this).
The complexity of the search determines the difficulty of the puzzle; the
example above is considered easy because it can be solved by straight
forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
contains fifty different Su Doku puzzles ranging in difficulty, but all
with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in
the top left corner of each solution grid; for example, 483 is the 3-digit
number found in the top left corner of the solution grid above.

Solution:
We keep a track of the digits that are already present in each row,
column and box, and use that to check which digits can be used to fill an unfilled
cell. This process is then repeated recursively until the puzzle is solved, after
which the 3 digit numbers formed by the top left corner of each puzzle are added.

References:
https://en.wikipedia.org/wiki/Sudoku
https://en.wikipedia.org/wiki/Backtracking
"""

import os


def solve(
    unfilled: list[tuple[int, int]],
    row: list[int],
    col: list[int],
    box: list[int],
    board: list[list[str]],
    index: int,
    total: int,
) -> bool:
    """
    Recursive backtracking function to solve the sudoku

    >>> solve(
    ... [(0, 0)],
    ... [0b111110111, 0b111111111, 0b111111111, 0b111111111,
    ... 0b111111111, 0b111111111, 0b111111111, 0b111111111, 0b111111111],
    ... [0b111110111, 0b111111111, 0b111111111, 0b111111111,
    ... 0b111111111, 0b111111111, 0b111111111, 0b111111111, 0b111111111],
    ... [0b111110111, 0b111111111, 0b111111111, 0b111111111,
    ... 0b111111111, 0b111111111, 0b111111111, 0b111111111, 0b111111111],
    ... [["0","8","3","9","2","1","6","5","7"],
    ... ["9","6","7","3","4","5","8","2","1"],
    ... ["2","5","1","8","7","6","4","9","3"],
    ... ["5","4","8","1","3","2","9","7","6"],
    ... ["7","2","9","5","6","4","1","3","8"],
    ... ["1","3","6","7","9","8","2","4","5"],
    ... ["3","7","2","6","8","9","5","1","4"],
    ... ["8","1","4","2","5","3","7","6","9"],
    ... ["6","9","5","4","1","7","3","8","2"]],
    ... 0,
    ... 1)
    True
    """
    if index == total:
        return True

    # Get the row and column numbers for the current unfilled cell
    r, c = unfilled[index]

    for val in range(9):
        # Check if value (val+1) can be placed at position (r, c)
        if (
            ((row[r] & (1 << val)) == 0)
            and ((col[c] & (1 << val)) == 0)
            and ((box[r // 3 * 3 + c // 3] & (1 << val)) == 0)
        ):
            # Place the value
            row[r] ^= 1 << val
            col[c] ^= 1 << val
            box[r // 3 * 3 + c // 3] ^= 1 << val
            board[r][c] = str(val + 1)

            # Recursively solve
            if solve(unfilled, row, col, box, board, index + 1, total):
                return True

            # Backtrack
            row[r] ^= 1 << val
            col[c] ^= 1 << val
            box[r // 3 * 3 + c // 3] ^= 1 << val
            board[r][c] = "0"

    return False


def solve_sudoku(board: list[list[str]]) -> int:
    """
    Solve a single sudoku puzzle and return the first 3 digits

    >>> solve_sudoku(
    ... [["0","0","3","0","2","0","6","0","0"],
    ... ["9","0","0","3","0","5","0","0","1"],
    ... ["0","0","1","8","0","6","4","0","0"],
    ... ["0","0","8","1","0","2","9","0","0"],
    ... ["7","0","0","0","0","0","0","0","8"],
    ... ["0","0","6","7","0","8","2","0","0"],
    ... ["0","0","2","6","0","9","5","0","0"],
    ... ["8","0","0","2","0","3","0","0","9"],
    ... ["0","0","5","0","1","0","3","0","0"]])
    483
    """
    unfilled = []
    row = [0] * 9
    col = [0] * 9
    box = [0] * 9

    # Initialize the state and find unfilled positions
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for ii in range(3):
                for jj in range(3):
                    r = i + ii
                    c = j + jj
                    if board[r][c] == "0":
                        unfilled.append((r, c))
                    else:
                        val = int(board[r][c]) - 1
                        row[r] |= 1 << val
                        col[c] |= 1 << val
                        box[i + j // 3] |= 1 << val

    # Solve the puzzle
    solve(unfilled, row, col, box, board, 0, len(unfilled))

    # Return the first 3 digits as a number
    return int(board[0][0]) * 100 + int(board[0][1]) * 10 + int(board[0][2])


def solution() -> int:
    """
    Finds the sum of the 3 digit numbers formed by the 3 digits in the
    top left corner of the solved sudoku puzzles as described by the problem statement.

    >>> solution()
    24702
    """
    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        sudoku = os.path.join(script_dir, "sudoku.txt")
        with open(sudoku) as file:
            lines = file.readlines()

    except FileNotFoundError:
        print("Error: Could not find sudoku.txt file")
        return 0

    res = 0
    count = 0
    board = []

    for line in lines:
        line = line.strip()
        if line.startswith("G"):
            continue

        board.append(list(line))
        count = (count + 1) % 9

        if count == 0:
            solution = solve_sudoku(board)
            res += solution
            board = []

    return res


if __name__ == "__main__":
    print(f"{solution()=}")
