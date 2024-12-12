 from __future__ import annotations

def get_valid_moves(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    Find all the valid positions a knight can move to from the current position.

    >>> get_valid_moves((1, 3), 4)
    [(2, 1), (0, 1), (3, 2), (3, 4)]
    """
    y, x = position
    moves = [
        (y + 1, x + 2), (y - 1, x + 2),
        (y + 1, x - 2), (y - 1, x - 2),
        (y + 2, x + 1), (y + 2, x - 1),
        (y - 2, x + 1), (y - 2, x - 1),
    ]
    return [(ny, nx) for ny, nx in moves if 0 <= ny < n and 0 <= nx < n]

def is_board_filled(board: list[list[int]]) -> bool:
    """
    Check if the board has been completely filled with non-zero values.

    >>> is_board_filled([[1]])
    True

    >>> is_board_filled([[1, 2], [3, 0]])
    False
    """
    return all(cell != 0 for row in board for cell in row)

def knight_tour_helper(
    board: list[list[int]], position: tuple[int, int], move_count: int
) -> bool:
    """
    Recursive helper function to solve the Knight's Tour problem using backtracking.
    """
    if is_board_filled(board):
        return True

    for next_position in get_valid_moves(position, len(board)):
        y, x = next_position

        if board[y][x] == 0:  # Check if the position is unvisited
            board[y][x] = move_count + 1
            if knight_tour_helper(board, next_position, move_count + 1):
                return True
            board[y][x] = 0  # Backtrack

    return False

def knight_tour(n: int) -> list[list[int]]:
    """
    Solve the Knight's Tour problem for a board of size n x n.
    Raises a ValueError if the tour cannot be performed for the given size.

    >>> knight_tour(1)
    [[1]]

    >>> knight_tour(2)
    Traceback (most recent call last):
        ...
    ValueError: Knight's Tour cannot be performed on a board of size 2
    """
    board = [[0 for _ in range(n)] for _ in range(n)]

    for start_y in range(n):
        for start_x in range(n):
            board[start_y][start_x] = 1
            if knight_tour_helper(board, (start_y, start_x), 1):
                return board
            board[start_y][start_x] = 0  # Reset the board

    raise ValueError(f"Knight's Tour cannot be performed on a board of size {n}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
