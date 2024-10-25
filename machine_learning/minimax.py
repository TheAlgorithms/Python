import math


def minimax(
    depth: int, node_index: int, is_maximizing_player: bool, scores: list, height: int
) -> float:
    """
    Minimax algorithm to determine the optimal move for a player in a two-player
    zero-sum game.

    Parameters:
    - depth (int): Current depth in the game tree. Used to track recursion level.
    - node_index (int): Index of the current node in the scores array, representing
    leaf nodes.
    - is_maximizing_player (bool): True if the current player is the maximizing player
    , False otherwise.
    - scores (list): A list of integers representing the scores at the leaf nodes
    of the game tree.
    - height (int): The maximum depth of the game tree, based on the number of leaf
    nodes in a binary structure.

    Returns:
    - int: The best score that the current player can achieve from this node.
    """
    # Base case: If the maximum depth is reached, return the score at this node.
    if depth == height:
        return scores[node_index]

    # Maximizing player's move
    if is_maximizing_player:
        best_score = -math.inf  # Start with the worst possible score for maximizer
        # Simulate two possible moves (binary tree branches)
        for i in range(2):
            # Recursive call for the next level of depth
            val = minimax(depth + 1, node_index * 2 + i, False, scores, height)
            best_score = max(
                best_score, val
            )  # Maximizer chooses the highest score available
        return best_score

    # Minimizing player's move
    else:
        best_score = math.inf  # Start with the worst possible score for minimizer
        for i in range(2):
            # Recursive call for the next level of depth
            val = minimax(depth + 1, node_index * 2 + i, True, scores, height)
            best_score = min(
                best_score, val
            )  # Minimizer chooses the lowest score available
        return best_score


def main() -> None:
    # Scores array representing the leaf nodes of a binary tree (depth = 3)
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    # Calculate the height of the binary tree based on the number of leaf nodes
    height = math.ceil(math.log2(len(scores)))

    # Print the optimal outcome for the maximizing player
    print(
        "Optimal value for the maximizing player:", minimax(0, 0, True, scores, height)
    )


if __name__ == "__main__":
    main()
