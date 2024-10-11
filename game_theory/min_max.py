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
<<<<<<< HEAD
        self, current_depth: int = 0,
        node_index: int = 0, is_max_turn: bool = True
=======
        self, current_depth: int = 0, node_index: int = 0, is_max_turn: bool = True
>>>>>>> 8497aa531c8636d5735e3df3d7583d9c05a323b5
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

<<<<<<< HEAD
        # Recursive case
=======
>>>>>>> 8497aa531c8636d5735e3df3d7583d9c05a323b5
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
        """
        return self.minimax()

<<<<<<< HEAD
=======

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    game = MinMax(scores)
    optimal_value = game.find_optimal_value()
    print(f"The optimal value is: {optimal_value}")
>>>>>>> 8497aa531c8636d5735e3df3d7583d9c05a323b5
