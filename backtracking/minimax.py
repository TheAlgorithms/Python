"""
Minimax Algorithm with Alpha-Beta Pruning
==========================================

Minimax is a decision-rule algorithm used in two-player, zero-sum games. It
explores all possible moves recursively and picks the optimal one for the
"maximising" player while assuming the opponent plays optimally (minimises
the score).

Alpha-Beta Pruning is an optimisation that cuts off branches in the search
tree that cannot influence the final decision, reducing the effective branching
factor from O(b^d) towards O(b^(d/2)).

References:
    - https://en.wikipedia.org/wiki/Minimax
    - https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    - Russell, S. & Norvig, P. (2020). Artificial Intelligence: A Modern
      Approach (4th ed.), Chapter 5.
"""

from __future__ import annotations

import math


def minimax(
    depth: int,
    node_index: int,
    is_maximising: bool,
    scores: list[int],
    alpha: float = -math.inf,
    beta: float = math.inf,
    height: int | None = None,
) -> int:
    """
    Return the optimal score for the current player using Minimax with
    Alpha-Beta Pruning on a complete binary game tree whose leaf values are
    given by *scores*.

    The tree is stored implicitly: leaf nodes are at depth 0, and internal
    nodes are addressed by *node_index* at each *depth* level.

    Parameters
    ----------
    depth       : Remaining depth to explore (0 = leaf node).
    node_index  : Index of the current node within its level.
    is_maximising : True if the current player wants to maximise the score.
    scores      : List of scores at the leaf level (length must be a power of 2).
    alpha       : Best (highest) value the maximiser can guarantee so far.
    beta        : Best (lowest) value the minimiser can guarantee so far.
    height      : Total height of the tree (computed automatically on first call).

    Returns
    -------
    int : The optimal score reachable from this node.

    Examples
    --------
    >>> scores = [3, 5, 2, 9, 12, 5, 23, 23]
    >>> minimax(3, 0, True, scores)
    12

    >>> scores = [3, 5, 2, 9]
    >>> minimax(2, 0, True, scores)
    3

    >>> scores = [-1, 4, 2, 6, -3, -5, 0, 7]
    >>> minimax(3, 0, False, scores)
    0

    >>> minimax(0, 0, True, [42])
    42

    >>> minimax(0, 0, False, [7])
    7
    """
    if height is None:
        height = int(math.log2(len(scores)))

    # Base case: we are at a leaf node
    if depth == 0:
        return scores[node_index]

    left_child = 2 * node_index
    right_child = 2 * node_index + 1

    if is_maximising:
        best = -math.inf
        for child in (left_child, right_child):
            value = minimax(depth - 1, child, False, scores, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off: minimiser will never allow this branch
        return int(best)
    else:
        best = math.inf
        for child in (left_child, right_child):
            value = minimax(depth - 1, child, True, scores, alpha, beta, height)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off: maximiser will never allow this branch
        return int(best)


# ---------------------------------------------------------------------------
# Tic-Tac-Toe: a concrete, runnable demonstration of Minimax
# ---------------------------------------------------------------------------

Board = list[list[str]]

_HUMAN = "O"
_AI = "X"
_EMPTY = "_"


def _winning_player(board: Board) -> str | None:
    """
    Return the winner symbol if any row, column, or diagonal is complete,
    otherwise return None.

    Examples
    --------
    >>> b = [['X','X','X'],['O','_','_'],['O','_','_']]
    >>> _winning_player(b)
    'X'
    >>> b = [['O','X','X'],['X','O','_'],['O','_','O']]
    >>> _winning_player(b)
    'O'
    >>> b = [['X','O','X'],['O','X','O'],['O','X','_']]
    >>> _winning_player(b) is None
    True
    """
    lines = (
        # rows
        board[0], board[1], board[2],
        # columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    )
    for line in lines:
        if line[0] != _EMPTY and len(set(line)) == 1:
            return line[0]
    return None


def _is_board_full(board: Board) -> bool:
    """
    Return True if there are no empty cells left.

    Examples
    --------
    >>> _is_board_full([['X','O','X'],['O','X','O'],['O','X','O']])
    True
    >>> _is_board_full([['X','O','X'],['O','_','O'],['O','X','O']])
    False
    """
    return all(cell != _EMPTY for row in board for cell in row)


def _evaluate(board: Board) -> int:
    """
    Heuristic score: +10 if AI wins, -10 if human wins, 0 otherwise.

    Examples
    --------
    >>> b = [['X','X','X'],['O','_','_'],['O','_','_']]
    >>> _evaluate(b)
    10
    >>> b = [['O','O','O'],['X','_','_'],['X','_','_']]
    >>> _evaluate(b)
    -10
    >>> b = [['X','O','X'],['O','X','O'],['O','X','O']]
    >>> _evaluate(b)
    0
    """
    winner = _winning_player(board)
    if winner == _AI:
        return 10
    if winner == _HUMAN:
        return -10
    return 0


def minimax_ttt(board: Board, depth: int, is_maximising: bool) -> int:
    """
    Minimax (without alpha-beta, for clarity) applied to Tic-Tac-Toe.
    Returns the best achievable score from *board* for the current player.

    Parameters
    ----------
    board         : 3×3 grid; cells are '_', 'X', or 'O'.
    depth         : Remaining search depth (used to prefer shorter wins).
    is_maximising : True when it is the AI's (X's) turn.

    Examples
    --------
    >>> b = [['X','X','_'],['O','O','_'],['_','_','_']]
    >>> minimax_ttt(b, 9, True)   # AI should win by playing (0,2)
    10
    >>> b = [['O','O','_'],['X','X','_'],['_','_','_']]
    >>> minimax_ttt(b, 9, False)  # Human should win by playing (1,2)
    -10
    """
    score = _evaluate(board)
    if score in (10, -10):
        return score
    if _is_board_full(board):
        return 0

    if is_maximising:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == _EMPTY:
                    board[i][j] = _AI
                    best = max(best, minimax_ttt(board, depth - 1, False))
                    board[i][j] = _EMPTY
        return int(best)
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == _EMPTY:
                    board[i][j] = _HUMAN
                    best = min(best, minimax_ttt(board, depth - 1, True))
                    board[i][j] = _EMPTY
        return int(best)


def best_move(board: Board) -> tuple[int, int]:
    """
    Return the board position (row, col) of the AI's best next move.

    Examples
    --------
    >>> b = [['X','O','X'],['O','X','_'],['_','_','O']]
    >>> best_move(b)
    (2, 0)
    """
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == _EMPTY:
                board[i][j] = _AI
                move_val = minimax_ttt(board, 9, False)
                board[i][j] = _EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move


def _print_board(board: Board) -> None:
    """Pretty-print the Tic-Tac-Toe board."""
    print("\n  0 1 2")
    for idx, row in enumerate(board):
        print(f"{idx} {' '.join(row)}")
    print()


def _play_game() -> None:
    """Interactive Tic-Tac-Toe: Human (O) vs. AI (X)."""
    board: Board = [[_EMPTY] * 3 for _ in range(3)]
    print("=== Tic-Tac-Toe: Human (O) vs AI (X) ===")
    print("Enter moves as 'row col' (e.g., '1 2').\n")

    for turn in range(9):
        _print_board(board)
        if turn % 2 == 0:
            # Human's turn
            try:
                raw = input("Your move (row col): ").strip().split()
                r, c = int(raw[0]), int(raw[1])
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue
            if not (0 <= r < 3 and 0 <= c < 3) or board[r][c] != _EMPTY:
                print("Cell unavailable. Try again.")
                continue
            board[r][c] = _HUMAN
        else:
            # AI's turn
            r, c = best_move(board)
            board[r][c] = _AI
            print(f"AI plays at ({r}, {c})")

        winner = _winning_player(board)
        if winner:
            _print_board(board)
            print(f"{'You win! 🎉' if winner == _HUMAN else 'AI wins! 🤖'}")
            return

    _print_board(board)
    print("It's a draw! 🤝")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # --- Demo: generic game tree ---
    print("=== Generic Minimax Demo ===")
    demo_scores = [3, 5, 2, 9, 12, 5, 23, 23]
    result = minimax(3, 0, True, demo_scores)
    print(f"Scores      : {demo_scores}")
    print(f"Optimal val : {result}")   # Expected: 12

    # --- Demo: Tic-Tac-Toe interactive ---
    print("\nLaunching Tic-Tac-Toe …")
    _play_game()