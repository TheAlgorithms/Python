import math
from typing import List


class MinMax:
    """
    A class to represent a game using the Minimax algorithm.

    Attributes:
    ----------
    scores : List[int]
        List of terminal node scores.
    tree_depth : int
        Depth of the game tree.

    Methods:
    -------
    minimax(current_depth: int = 0, node_index: int = 0, is_max_turn: bool = True) -> int:
        Recursive implementation of the minimax algorithm.
    find_optimal_value() -> int:
        Find and return the optimal value for the maximizing player.

    Examples:
    ---------
    >>> game = MinMax([3, 5, 2, 9, 12, 5, 23, 23])
    >>> game.find_optimal_value()
    12
    """

    def __init__(self, scores: List[int]) -> None:
        """
        Initialize the MinMax game with a list of scores.

        Parameters:
        ----------
        scores : List[int]
            List of terminal node scores.
        """
        self.scores = scores
        self.tree_depth = int(math.log2(len(scores)))

    def minimax(
        self, current_depth: int = 0, node_index: int = 0, is_max_turn: bool = True
    ) -> int:
        """
        Recursive implementation of the minimax algorithm.

        Parameters:
        ----------
        current_depth : int
            Current depth in the game tree.
        node_index : int
            Index of the current node in the tree.
        is_max_turn : bool
            Boolean indicating if it's the maximizing player's turn.

        Returns:
        -------
        int
            The optimal value for the current player.

        Examples:
        ---------
        >>> game = MinMax([3, 5, 2, 9, 12, 5, 23, 23])
        >>> game.minimax(0, 0, True)
        12
        """

        if current_depth == self.tree_depth:
            return self.scores[node_index]

        if is_max_turn:
            return max(
                self.minimax(current_depth + 1, node_index * 2, False),
                self.minimax(current_depth + 1, node_index * 2 + 1, False),
            )
        else:
            return min(
                self.minimax(current_depth + 1, node_index * 2, True),
                self.minimax(current_depth + 1, node_index * 2 + 1, True),
            )

    def find_optimal_value(self) -> int:
        """
        Find and return the optimal value for the maximizing player.

        Returns:
        -------
        int
            The optimal value.

        Examples:
        ---------
        >>> game = MinMax([3, 5, 2, 9, 12, 5, 23, 23])
        >>> game.find_optimal_value()
        12
        """
        return self.minimax()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    game = MinMax(scores)
    optimal_value = game.find_optimal_value()
    print(f"The optimal value is: {optimal_value}")
