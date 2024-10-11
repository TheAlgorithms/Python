import math

class MinimaxGame:
    def __init__(self, scores):
        """
        Initialize the MinimaxGame with a list of scores.
        
        :param scores: List of terminal node scores
        """
        self.scores = scores
        self.tree_depth = int(math.log2(len(scores)))

    def minimax(self, current_depth=0, node_index=0, is_max_turn=True):
        """
        Recursive implementation of the minimax algorithm.
        
        :param current_depth: Current depth in the game tree
        :param node_index: Index of the current node in the tree
        :param is_max_turn: Boolean indicating if it's the maximizing player's turn
        :return: The optimal value for the current player
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

    def find_optimal_value(self):
        """
        Find and return the optimal value for the maximizing player.
        
        :return: The optimal value
        """
        return self.minimax()

# Driver code
if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    game = MinimaxGame(scores)
    optimal_value = game.find_optimal_value()
    print(f"The optimal value is: {optimal_value}")