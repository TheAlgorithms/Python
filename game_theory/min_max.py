import math


class MinMax:
    """
    A class to represent a game using the Minimax algorithm.

    Attributes:
    ----------
    scores : list[int]
        List of terminal node scores.
    tree_depth : int
        Depth of the minimax tree.
    """

    def __init__(self, scores: list[int]):
        """
        Initialize the MinMax game with a list of scores.

        Parameters:
        ----------
        scores : list[int]
            List of terminal node scores.
        """
        self.scores = scores
        self.tree_depth = int(math.log2(len(scores)))

    def minimax(
        self, current_depth: int = 0,
        node_index: int = 0, is_max_turn: bool = True
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
        """
        # Base case: we've reached a terminal node
        if current_depth == self.tree_depth:
            return self.scores[node_index]

        # Recursive case
        if is_max_turn:
            return max(
                self.minimax(current_depth + 1, node_index * 2, False),
                self.minimax(current_depth + 1, node_index * 2 + 1, False)
            )
        else:
            return min(
                self.minimax(current_depth + 1, node_index * 2, True),
                self.minimax(current_depth + 1, node_index * 2 + 1, True)
            )

    def find_optimal_value(self) -> int:
        """
        Find and return the optimal value for the maximizing player.

        Returns:
        -------
        int
            The optimal value.
        """
        return self.minimax()

