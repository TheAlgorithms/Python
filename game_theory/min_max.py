import math

class MinMax:
    def __init__(self, scores):
        """
        Initialize the MinMax game with a list of scores.

        This class implements the minimax algorithm to determine the optimal score 
        that can be achieved by the maximizing player in a two-player turn-based game.

        :param scores: List of terminal node scores, where each score represents the 
                       value of a terminal state in the game tree. The length of the 
                       scores list must be a power of two, as it represents a complete 
                       binary tree.
        """
        self.scores = scores
        self.tree_depth = int(math.log2(len(scores)))

    def minimax(self, current_depth=0, node_index=0, is_max_turn=True):
        """
        Recursively calculate the optimal score using the minimax algorithm.

        This method traverses the game tree to determine the best possible outcome 
        for the maximizing player. It uses depth-first search to evaluate all possible 
        moves and their outcomes.

        :param current_depth: Current depth in the game tree, which helps track how 
                              far down the tree we are. Defaults to 0 for the root node.
        :param node_index: Index of the current node in the scores list. This is used 
                           to access the corresponding score in the scores list.
        :param is_max_turn: Boolean indicating if it is the maximizing player's turn. 
                            If True, the maximizing player will choose the maximum score; 
                            otherwise, the minimizing player will choose the minimum score.

        :return: The optimal value for the current player at this node. If it's the 
                 maximizing player's turn, it returns the highest score obtainable; 
                 if it's the minimizing player's turn, it returns the lowest score obtainable.
        """
        if current_depth == self.tree_depth:
            return self.scores[node_index]

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

        This method initiates the minimax algorithm from the root node (depth 0) 
        and returns the best score that can be achieved by the maximizing player.

        :return: The optimal value (score) for the maximizing player based on the 
                 provided terminal node scores. This represents the best possible 
                 outcome given optimal play from both players.
        """
        return self.minimax()

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    game = MinMax(scores)
    optimal_value = game.find_optimal_value()
    print(f"The optimal value is: {optimal_value}")

