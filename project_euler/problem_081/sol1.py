"""
Project Euler Problem 81: https://projecteuler.net/problem=81

-----------------------------------------------------------------------------

PROBLEM STATEMENT

n the 5 by 5 matrix below, the minimal path sum from the top left
to the bottom right, by only moving to the right and down, is indicated
in bold red and is equal to 2427.

[
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331],
]


Find the minimal path sum from the top left to the bottom right by only moving
right and down in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing an 80 by 80 matrix.

-----------------------------------------------------------------------------

SOLUTION

Let's approach this problem by using dynamic programming (DP)

* let matrix[i][j] = the value at line i and column j in the input matrix
* let min_sum[i][j] = the minimal path sum that can be obtained from the
  origin (0, 0) to (i, j), by only moving to the right or down
* we notice that min_sum[0][0] = the value in the origin = matrix[0][0]
* the relation of recursion is
  min_sum[i][j] = min(min_sum[i - 1][j], min_sum[i][j - 1])
  for i >= 0 and j >= 0
* the solution will be min_sum[n - 1][m - 1]

In my implementation I took a 'forward' approach and calculated
future states of the DP using the current state, instead of using
a 'backwards' approach by calculating the current state from past states.


TIME 0.22s

"""


def solve_matrix(lines: int, columns: int, matrix: list) -> int:
    """
    Find the answer for an input matrix

    >>> solve_matrix(5, 5, \
        [ [131, 673, 234, 103, 18], \
          [201, 96, 342, 965, 150], \
          [630, 803, 746, 422, 111], \
          [537, 699, 497, 121, 956], \
          [805, 732, 524, 37, 331], ])
    2427
    >>> solve_matrix(1, 1, [[27]])
    27
    """

    infinity = float("inf")
    min_sum = [[infinity for j in range(columns)] for i in range(lines)]
    min_sum[0][0] = matrix[0][0]

    # compute the DP and the answer
    for i in range(lines):
        for j in range(columns):
            if i + 1 < lines:
                new_sum = min_sum[i][j] + matrix[i + 1][j]
                min_sum[i + 1][j] = min(min_sum[i + 1][j], new_sum)
            if j + 1 < columns:
                new_sum = min_sum[i][j] + matrix[i][j + 1]
                min_sum[i][j + 1] = min(min_sum[i][j + 1], new_sum)

    return min_sum[lines - 1][columns - 1]


def solution() -> int:
    """
    open the input file, read and parse the matrix data,
    solve the problem by applying the above algorithm
    and return the answer

    >>> solution()
    2427
    """

    matrix = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    # the code below solves the upstream problem but I cannot use it
    # since an additional file is needed to read from

    # with open("./p081_matrix.txt", "r") as file:
    #     matrix = file.readlines()
    #     for i, line in enumerate(matrix):
    #         line[i].strip("\n")
    #         matrix[i] = [int(x) for x in line.split(",")]

    return solve_matrix(len(matrix), len(matrix[-1]), matrix)


if __name__ == "__main__":
    print(solution())
