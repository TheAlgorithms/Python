"""
Minimax helps to achieve maximum score in a game by checking all possible moves.

"""
from __future__ import annotations

import math


def minimax(
    depth: int, node_index: int, is_max: bool, scores: list[int], height: float
) -> int:
    """
    depth is current depth in game tree.
    node_index is index of current node in scores[].
    scores[] contains the leaves of game tree.
    height is maximum height of game tree.

    >>> scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    65
    >>> minimax(-1, 0, True, scores, height)
    Traceback (most recent call last):
        ...
    ValueError: Depth cannot be less than 0
    >>> minimax(0, 0, True, [], 2)
    Traceback (most recent call last):
        ...
    ValueError: Scores cannot be empty
    >>> scores = [3, 5, 2, 9, 12, 5, 23, 23]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    12
    """

    if depth < 0:
        raise ValueError("Depth cannot be less than 0")

    if not scores:
        raise ValueError("Scores cannot be empty")

    if depth == height:
        return scores[node_index]

    return (
        max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
        )
        if is_max
        else min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height),
        )
    )


def main() -> None:
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)
    print(f"Optimal value : {minimax(0, 0, True, scores, height)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
