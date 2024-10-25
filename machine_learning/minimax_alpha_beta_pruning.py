import math


def minimax_with_pruning(
    depth: int,
    node_index: int,
    is_maximizing_player: bool,
    scores: list,
    height: int,
    alpha: int,
    beta: int,
) -> int:
    """
    Minimax algorithm with alpha-beta pruning to determine the optimal
    move with improved efficiency.

    Parameters:
    - depth (int): Current depth in the game tree, used to track recursion level.
    - node_index (int): Index of the current node in the scores array, representing
    leaf nodes.
    - is_maximizing_player (bool): True if the current player is the maximizing player
    , False otherwise.
    - scores (list): A list of integers representing the scores at the
    leaf nodes of the game tree.
    - height (int): The maximum depth of the game tree, based on the number of
    leaf nodes in a binary structure.
    - alpha (int): The best value that the maximizer can guarantee at the
    current level or above.
    - beta (int): The best value that the minimizer can guarantee at the
    current level or above.

    Returns:
    - int: The best score that the current player can achieve from this node.
    """
    # Base case: If we reach the leaf node level, return its score
    if depth == height:
        return scores[node_index]

    # Maximizing player's move
    if is_maximizing_player:
        best_score = -math.inf  # Start with the worst possible score for maximizer
        for i in range(2):  # Two branches at each level in binary tree
            val = minimax_with_pruning(
                depth + 1, node_index * 2 + i, False, scores, height, alpha, beta
            )
            best_score = max(best_score, val)  # Maximizer selects the maximum value
            alpha = max(alpha, best_score)  # Update alpha (best option for maximizer)
            if beta <= alpha:
                break  # Beta cut-off
        return best_score

    # Minimizing player's move
    else:
        best_score = math.inf  # Start with the worst possible score for minimizer
        for i in range(2):
            val = minimax_with_pruning(
                depth + 1, node_index * 2 + i, True, scores, height, alpha, beta
            )
            best_score = min(best_score, val)  # Minimizer selects the minimum value
            beta = min(beta, best_score)  # Update beta (best option for minimizer)
            if beta <= alpha:
                break  # Alpha cut-off
        return best_score


def main() -> None:
    # Scores array representing the leaf nodes of a binary tree (depth = 3)
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    # Calculate the height of the binary tree based on the number of leaf nodes
    height = math.ceil(math.log2(len(scores)))

    # Print the optimal outcome for the maximizing player with alpha-beta pruning
    print(
        "Optimal value for the maximizing player with pruning:",
        minimax_with_pruning(0, 0, True, scores, height, -math.inf, math.inf),
    )


if __name__ == "__main__":
    main()
