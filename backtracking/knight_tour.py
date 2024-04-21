from __future__ import annotations

from typing import ClassVar


class KnightTourSolver:
    """
    Represents a solver for the Knight's Tour problem.
    """

    MOVES: ClassVar[list[tuple[int, int]]] = [
        (1, 2),
        (-1, 2),
        (1, -2),
        (-1, -2),
        (2, 1),
        (-2, 1),
        (2, -1),
        (-2, -1),
    ]

    def __init__(self, board_size: int):
        """
        Initializes the KnightTourSolver with the specified board size.
        """
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]

    def _is_valid_move(self, position: tuple[int, int], move: tuple[int, int]) -> bool:
        """
        Checks if a move is valid from the current position.
        """
        y, x = position
        dy, dx = move
        new_y, new_x = y + dy, x + dx
        return 0 <= new_y < self.board_size and 0 <= new_x < self.board_size

    def _get_valid_moves(self, position: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Find all the valid positions a knight can move to from the current position.
        """
        return [
            (position[0] + dy, position[1] + dx)
            for dy, dx in self.MOVES
            if self._is_valid_move(position, (dy, dx))
        ]

    def _solve_knight_tour(self, position: tuple[int, int], move_number: int) -> bool:
        """
        Helper function to solve the Knight's Tour problem recursively.
        """
        if move_number == self.board_size * self.board_size + 1:
            # Base case: all cells visited
            return True

        for next_position in self._get_valid_moves(position):
            # Move is valid and cell is not visited yet
            new_y, new_x = next_position
            if self.board[new_y][new_x] == 0:
                self.board[new_y][new_x] = move_number
                if self._solve_knight_tour(next_position, move_number + 1):
                    # Recursive call for the next move
                    return True
                # Backtrack if no solution found
                self.board[new_y][new_x] = 0

        return False

    def find_knight_tour(self) -> list[list[int]]:
        """
        Find a solution for the Knight's Tour problem for the initialized board size.
        Raises ValueError if the tour cannot be performed for the given size.

        >>> solver = KnightTourSolver(1)
        >>> solver.find_knight_tour()
        [[1]]
        >>> solver = KnightTourSolver(2)
        >>> solver.find_knight_tour()
        Traceback (most recent call last):
            ...
        ValueError: Knight's tour cannot be performed on a board of size 2
        """
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board[i][j] = 1
                if self._solve_knight_tour((i, j), 2):
                    return self.board
                self.board[i][j] = 0
        error_message = (
            f"Knight's tour cannot be performed on a board of size {self.board_size}"
        )
        raise ValueError(error_message)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
