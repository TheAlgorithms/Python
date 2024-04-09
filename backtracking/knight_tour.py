from __future__ import annotations


class KnightTour:
    """
    Represents a Knight's Tour problem solver.
    """

    @staticmethod
    def get_valid_moves(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
        """
        Find all the valid positions a knight can move to from the current position.

        >>> KnightTour.get_valid_moves((1, 3), 4)
        [(2, 1), (0, 1), (3, 2)]
        """
        y, x = position
        moves = [
            (y + 1, x + 2),
            (y - 1, x + 2),
            (y + 1, x - 2),
            (y - 1, x - 2),
            (y + 2, x + 1),
            (y + 2, x - 1),
            (y - 2, x + 1),
            (y - 2, x - 1),
        ]
        valid_moves = [(y, x) for y, x in moves if 0 <= y < n and 0 <= x < n]
        return valid_moves

    @staticmethod
    def is_board_complete(board: list[list[int]]) -> bool:
        """
        Check if the board (matrix) has been completely filled with non-zero values.

        >>> KnightTour.is_board_complete([[1]])
        True
        >>> KnightTour.is_board_complete([[1, 2], [3, 0]])
        False
        """
        return not any(elem == 0 for row in board for elem in row)

    @staticmethod
    def solve_knight_tour(
        board: list[list[int]], pos: tuple[int, int], curr: int
    ) -> bool:
        """
        Helper function to solve knight tour problem.
        """

        if KnightTour.is_board_complete(board):
            return True

        n = len(board)
        for move in KnightTour.get_valid_moves(pos, n):
            y, x = move
            if board[y][x] == 0:
                board[y][x] = curr + 1
                if KnightTour.solve_knight_tour(board, move, curr + 1):
                    return True
                board[y][x] = 0

        return False

    @staticmethod
    def find_knight_tour(n: int) -> list[list[int]]:
        """
        Find the solution for the knight tour problem for a board of size n. Raises
        ValueError if the tour cannot be performed for the given size.

        >>> KnightTour.find_knight_tour(1)
        [[1]]
        >>> KnightTour.find_knight_tour(2)
        Traceback (most recent call last):
            ...
        ValueError: Knight's tour cannot be performed on a board of size 2
        """
        if n < 1:
            raise ValueError("Board size must be at least 1")

        board = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                board[i][j] = 1
                if KnightTour.solve_knight_tour(board, (i, j), 1):
                    return board
                board[i][j] = 0
        error_message = f"Knight's tour cannot be performed on a board of size {n}"
        raise ValueError(error_message)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
