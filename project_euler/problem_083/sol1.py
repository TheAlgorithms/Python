"""
Project Euler Problem 83: https://projecteuler.net/problem=83

-----------------------------------------------------------------------------

PROBLEM STATEMENT

In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by moving left, right, up, and down, is indicated
in bold red and is equal to 2297.

[131]  673 [234] [103] [18]
[201] [96] [342]  965  [150]
 630   803  746  [422] [111]
 537   699  497  [121]  956
 865   732  524  [37]  [331]


Find the minimal path sum from the top left to the bottom right by
moving left, right, up, and down in matrix.txt (right click and
"Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

-----------------------------------------------------------------------------

SOLUTION

We can interpret the input matrix as being a undirected graph, where
each cell is a vertex connected to its neighbours.

The solution is based on the Bellman-Ford Algorithm

Reference: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

"""

import os
import queue


def solve_matrix(lines: int, columns: int, matrix: list) -> int:
    """
    Find the answer for an input matrix

    >>> solve_matrix(5, 5, \
        [ [131, 673, 234, 103, 18], \
          [201, 96, 342, 965, 150], \
          [630, 803, 746, 422, 111], \
          [537, 699, 497, 121, 956], \
          [865, 732, 524, 37, 331], ])
    2297
    >>> solve_matrix(1, 1, [[27]])
    27
    """

    infinity = float("inf")
    # tuples corresponding to a more up, down, left or right on the grid
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # min_sum[i][j] = minimal path sum from origin to (i, j)
    min_sum = [[infinity for j in range(columns)] for i in range(lines)]
    min_sum[0][0] = matrix[0][0]

    # insert the origin in the queue as a starting point
    que = queue.Queue()
    que.put((0, 0))

    # mark coordinates that are alreqdy present in the queue to avoid
    # inserting them multiple times
    in_queue = {(0, 0): True}

    while not que.empty():
        line, column = que.get()
        in_queue[(line, column)] = False

        for d_i, d_j in directions:
            # for each possible move check if it improves the
            # already present answer and update if necessary
            new_line, new_column = line + d_i, column + d_j
            if (
                new_line < 0
                or new_line >= lines
                or new_column < 0
                or new_column >= columns
            ):
                continue

            new_sum = min_sum[line][column] + matrix[new_line][new_column]
            if min_sum[new_line][new_column] > new_sum:
                min_sum[new_line][new_column] = new_sum
                if not in_queue.get((new_line, new_column), False):
                    in_queue[(new_line, new_column)] = True
                    que.put((new_line, new_column))

    return min_sum[lines - 1][columns - 1]


def solution() -> int:
    """
    open the input file, read and parse the matrix data,
    solve the problem by applying the above algorithm
    and return the answer

    >>> solution()
    425185
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, "p083_matrix.txt")

    matrix = []
    with open(os.path.join(input_file_path), "r") as file:
        matrix = file.readlines()
        for i, line in enumerate(matrix):
            line[i].strip("\n")
            matrix[i] = [int(x) for x in line.split(",")]

    return solve_matrix(len(matrix), len(matrix[-1]), matrix)


if __name__ == "__main__":
    print(solution())
