"""
This is an implementation for finding all possible paths of a
non symmetrical matrix between given start and end points including
consideration of obstacles using depth first search approach

For doctests run following command:
python3 -m doctest -v all_possible_paths_between_two_points_in_matrix_using_dfs.py

For manual testing run:
python3 all_possible_paths_between_two_points_in_matrix_using_dfs.py
"""

OBSTACLE_POS = -1
VALID_POS = 1
START_POS = "s"
END_POS = "e"
VISITED_POS = None


def find_all_possible_paths(matrix: list, row: int, col: int) -> int:
    """
    Pure implementation of recursive depth first search algorithm to find out
    all the possible paths of a given symmetrical/non-symmetrical matrix

    :param matrix: symmetrical or non-symmetrical matrix which contains
    start, end, valid and obstacle positions
    :param row: currently traversing row index of the matrix in a given point of time
    :param col: currently traversing column index of the matrix in a given point of time

    Examples:
    >>> find_all_possible_paths([['s', 1, 1], [1, -1, 1], [-1, 1, 'e']], 0, 0)
    1
    >>> find_all_possible_paths([[1, 'e', -1], [-1, 1, 1], [-1, 1, 's']], 2, 2)
    2
    >>> find_all_possible_paths([['s'], [1, 1], [1, 1, 1], [1, 1, 'e', 1]], 0, 0)
    7
    >>> find_all_possible_paths([[-1, 1], ['s', 1], [-1, -1], [-1, 'e']], 1, 0)
    0
    >>> find_all_possible_paths([[-1, 's'], [-1, -1, 1], [1, -1], ['e', 1, 1]], 0, 1)
    0
    """
    if (
        row < 0
        or row >= len(matrix)
        or col < 0
        or col >= len(matrix[row])
        or matrix[row][col] == OBSTACLE_POS
        or matrix[row][col] == VISITED_POS
    ):
        return 0
    if matrix[row][col] == END_POS:
        return 1

    visited = matrix[row][col]
    matrix[row][col] = VISITED_POS

    result = (
        find_all_possible_paths(matrix, row + 1, col)
        + find_all_possible_paths(matrix, row - 1, col)
        + find_all_possible_paths(matrix, row, col + 1)
        + find_all_possible_paths(matrix, row, col - 1)
    )
    matrix[row][col] = visited

    return result


def helper(matrix: list) -> int:
    """
    Examples:
    >>> helper([['s', 1, 1], [1, -1, 1], [-1, 1, 'e']])
    1
    >>> helper([[1, 'e', -1], [-1, 1, 1], [-1, 1, 's']])
    2
    >>> helper([['s'], [1, 1], [1, 1, 1], [1, 1, 'e', 1]])
    7
    >>> helper([[-1, 1], ['s', 1], [-1, -1], [-1, 'e']])
    0
    >>> helper([[-1, 's'], [-1, -1, 1], [1, -1], ['e', 1, 1]])
    0
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == START_POS:
                return find_all_possible_paths(matrix, i, j)
    return -1


if __name__ == "__main__":
    matrix = [
        [START_POS, VALID_POS, VALID_POS],
        [VALID_POS, VALID_POS, VALID_POS],
        [END_POS, VALID_POS, VALID_POS],
        [OBSTACLE_POS, OBSTACLE_POS, OBSTACLE_POS],
    ]

    shortest_path_distance = helper(matrix)
    print(shortest_path_distance)
