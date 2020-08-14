import math
from typing import List

""" Minimax helps to achieve maximum score in a game by checking all possible moves
    depth is current depth in game tree.
    nodeIndex is index of current node in scores[].
    if move is of maximizer return true else false
    leaves of game tree is stored in scores[]
    height is maximum height of Game tree
"""


def minimax(depth: int, node_index: int, is_max: bool,
            scores: List[int], height: float) -> int:
    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
        )

    return min(
        minimax(depth + 1, node_index * 2, True, scores, height),
        minimax(depth + 1, node_index * 2 + 1, True, scores, height),
    )


if __name__ == "__main__":
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)

    print("Optimal value : ", end="")
    print(minimax(0, 0, True, scores, height))
