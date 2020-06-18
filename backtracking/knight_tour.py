# Knight Tour Intro: https://www.youtube.com/watch?v=ab_dY3dZFHM

from typing import List, Tuple


def get_valid_pos(position: Tuple[int], n: int) -> List[Tuple[int]]:
    '''
    Find all the valid positions a knight can move to from the current position

    >>> get_valid_pos((1, 3), 4)
    [(2, 1), (0, 1), (3, 2)]
    '''

    y, x = position
    positions = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1)
    ]
    permissible_positions = []

    for position in positions:
        y_test, x_test = position
        if (y_test < n and y_test >= 0) and (x_test < n and x_test >= 0):
            permissible_positions.append(position)

    return permissible_positions


def is_complete(board: List[List[int]]) -> bool:
    '''
    Check if the board (matrix) has been completely filled with non-zero values

    >>> is_complete([[1]])
    True

    >>> is_complete([[1, 2], [3, 0]])
    False
    '''

    for row in board:
        for elem in row:
            if (elem == 0):
                return False
    return True


def open_knight_tour_helper(board: List[List[int]], pos: Tuple[int], curr: int) -> bool:
    '''
    Helper function to solve knight tour problem
    '''

    if is_complete(board):
        return True

    for position in get_valid_pos(pos, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr + 1
            if open_knight_tour_helper(board, position, curr + 1):
                return True
            board[y][x] = 0

    return False


def open_knight_tour(n: int) -> List[List[int]]:
    '''
    Find the solution for the knight tour problem for a board of size n

    >>> open_knight_tour(1)
    [[1]]

    >>> open_knight_tour(2) # None returned
    '''

    board = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            board[i][j] = 1
            if open_knight_tour_helper(board, (i, j), 1):
                return board
            board[i][j] = 0

    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
