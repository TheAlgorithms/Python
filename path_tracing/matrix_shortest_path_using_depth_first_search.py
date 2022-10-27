"""
This is an implementation for finding the shortest path of a
non symmetrical matrix between given start and end points including
consideration of obstacles using depth first search approach

For doctests run following command:
python3 -m doctest -v matrix_shortest_path_using_depth_first_search.py

For manual testing run:
python3 matrix_shortest_path_using_depth_first_search.py
"""

import math

OBSTACLE_POS = -1
VALID_POS = 1
START_POS = "s"
END_POS = "e"
VISITED_POS = None
current_shortest_path_distance = math.inf


def find_shortest_path_using_dfs(
    matrix: list, row: int, col: int, distance: int
) -> None:
    """
    Pure implementation of recursive depth first search algorithm to find out
    the shortest path distance of a given symmetrical/non-symmetrical
    matrix
    First recursion should be started with assigning 0 for the distance
    parameter
    :param matrix: symmetrical or non-symmetrical matrix which contains
    start, end, valid and obstacle positions
    :param row: currently traversing row index of the matrix in a given point of time
    :param col: currently traversing column index of the matrix in a given point of time
    :param distance: calculated distance through out a particular path of the matrix
    :return: None
    """
    global current_shortest_path_distance

    if (
        row < 0
        or row >= len(matrix)
        or col < 0
        or col >= len(matrix[row])
        or matrix[row][col] == OBSTACLE_POS
        or matrix[row][col] == VISITED_POS
    ):
        return
    if matrix[row][col] == END_POS:
        current_shortest_path_distance = min(current_shortest_path_distance, distance)
        return

    visited = matrix[row][col]
    matrix[row][col] = VISITED_POS

    find_shortest_path_using_dfs(matrix, row + 1, col, distance + 1)
    find_shortest_path_using_dfs(matrix, row - 1, col, distance + 1)
    find_shortest_path_using_dfs(matrix, row, col + 1, distance + 1)
    find_shortest_path_using_dfs(matrix, row, col - 1, distance + 1)

    matrix[row][col] = visited


def helper(matrix: list) -> int:
    """
    Examples:
    >>> helper([['s', 1, 1], [1, -1, 1], [-1, 1, 'e']])
    4
    >>> helper([[-1, 1, 1, 'e'], [1, -1, 1, 1], [1, 's', -1, 1], [-1, 1, 1, 1]])
    6
    >>> helper([[-1, 1], ['s', 1], [-1, 1], [1, 'e']])
    3
    >>> helper([['s'], [1, 1], [-1, 1, 1], [-1, -1, 'e', -1]])
    5
    >>> helper([[-1, -1, 1, 1, 's'], [-1, 1, 1, -1], [1, 1, -1], [1, -1], ['e']])
    8
    >>> helper([['s', 1, 1], [1, 1, -1], [1, -1, 'e']])
    inf
    >>> helper([[1, 1, -1, 1], [1, -1, 's', -1], [1, 1, -1, 1]])
    inf
    """
    global current_shortest_path_distance

    found = False
    current_shortest_path_distance = math.inf

    for i in range(len(matrix)):
        if not found:
            for j in range(len(matrix[i])):
                if matrix[i][j] == START_POS:
                    find_shortest_path_using_dfs(matrix, i, j, 0)
                    found = True
                    break
        else:
            break

    return current_shortest_path_distance


matrix = [
    [START_POS, VALID_POS, OBSTACLE_POS],
    [VALID_POS, VALID_POS, VALID_POS],
    [END_POS, OBSTACLE_POS, VALID_POS],
    [OBSTACLE_POS, OBSTACLE_POS, OBSTACLE_POS],
]

if __name__ == "__main__":
    shortest_path_distance = helper(matrix)

    print(shortest_path_distance)
