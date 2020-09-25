from __future__ import annotations
import math

""" Minimax helps to achieve maximum score in a game by checking all possible moves
    depth is current depth in game tree.
    nodeIndex is index of current node in scores[].
    if move is of maximizer return true else false
    leaves of game tree is stored in scores[]
    height is maximum height of Game tree
"""


def minimax(depth: int, node_index: int, is_max: bool,
            scores: list[int], height: float) -> int:
    """
    >>> import math
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
    >>> minimax('1', 2, True, [], 2 )
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """

    if depth < 0:
        raise ValueError("Depth cannot be less than 0")

    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

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


def main():
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)
    print("Optimal value : ", end="")
    print(minimax(0, 0, True, scores, height))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
