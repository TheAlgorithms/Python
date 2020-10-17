"""
Project Euler Problem 81: https://projecteuler.net/problem=81
Author: Ivan Ivanov
Problem statement: Find the minimal path sum from the top left to
the bottom right by only moving right and down in matrix.txt (a 31K file
containing a 80x80 matrix)
Solution: This is the standard Dynamic Programming problem
of finding minimal cost path in a 2D matrix
Time: 17 October 2020, 00:34
"""
import os


def solution() -> int:
    """
    Return the minimum path sum from the top left to the bottom right corner

    >>> solution()
    427337
    """

    # We read the input file
    file_path = os.path.join(os.path.dirname(__file__), "p081_matrix.txt")
    matrix_file = open(file_path, "r")

    # Initialize minimal cost matrix (with additional column
    # on the left and on the top for padding)
    # We also fill these with 2^32 as an arbitrary large number
    # which is much larger than the expected answer
    min_path = [[2 ** 32] * 81 for _ in range(81)]

    # Initialize the place where we will store the matrix
    matrix = [[0] * 80 for _ in range(80)]

    # Read the matrix
    line_number = 0
    for line in matrix_file:
        matrix[line_number] = list(map(int, line.split(",")))
        line_number = line_number + 1

    # Initialize the minimal cost matrix (add 0s in the padding
    # to the left and top of the top left cell)
    min_path[0][1] = 0
    min_path[1][0] = 0

    # Update the minimal cost matrix among the matrix
    for line_number in range(1, 81):
        for column_number in range(1, 81):
            # The minimal cost to the current cell is the minimal costs
            # from coming form the top (moving down) or coming from
            # the left (moving right) plus the value in the current cell
            # additional -1s for the padding
            min_path[line_number][column_number] = (
                min(
                    min_path[line_number - 1][column_number],
                    min_path[line_number][column_number - 1],
                )
                + matrix[line_number - 1][column_number - 1]
            )

    # Return the value in the bottom right cell
    return min_path[80][80]


if __name__ == "__main__":
    print(f"{solution() = }")
