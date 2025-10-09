"""
Project Euler Problem 82: https://projecteuler.net/problem=82

The minimal path sum in the 5 by 5 matrix below, by starting in any cell
in the left column and finishing in any cell in the right column,
and only moving up, down, and right, is indicated in red and bold;
the sum is equal to 994.

     131    673   [234]  [103]  [18]
    [201]  [96]   [342]   965    150
     630    803    746    422    111
     537    699    497    121    956
     805    732    524    37     331

Find the minimal path sum from the left column to the right column in matrix.txt
(https://projecteuler.net/project/resources/p082_matrix.txt)
(right click and "Save Link/Target As..."),
a 31K text file containing an 80 by 80 matrix.
"""

import os


def solution(filename: str = "input.txt") -> int:
    """
    Returns the minimal path sum in the matrix from the file, by starting in any cell
    in the left column and finishing in any cell in the right column,
    and only moving up, down, and right

    >>> solution("test_matrix.txt")
    994
    """

    with open(os.path.join(os.path.dirname(__file__), filename)) as input_file:
        matrix = [
            [int(element) for element in line.split(",")]
            for line in input_file.readlines()
        ]

    rows = len(matrix)
    cols = len(matrix[0])

    minimal_path_sums = [[-1 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        minimal_path_sums[i][0] = matrix[i][0]

    for j in range(1, cols):
        for i in range(rows):
            minimal_path_sums[i][j] = minimal_path_sums[i][j - 1] + matrix[i][j]

        for i in range(1, rows):
            minimal_path_sums[i][j] = min(
                minimal_path_sums[i][j], minimal_path_sums[i - 1][j] + matrix[i][j]
            )

        for i in range(rows - 2, -1, -1):
            minimal_path_sums[i][j] = min(
                minimal_path_sums[i][j], minimal_path_sums[i + 1][j] + matrix[i][j]
            )

    return min(minimal_path_sums_row[-1] for minimal_path_sums_row in minimal_path_sums)


if __name__ == "__main__":
    print(f"{solution() = }")
