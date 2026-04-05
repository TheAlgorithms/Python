"""
Author  : Nelson Mak
Date    : April 5, 2026

Task:
Given an m x n grid of characters board and a string word,
return the first valid path of coordinates found that matches
return the first valid path of coordinates found that matches
the word in the grid. If the word does not exist, return None.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

Matrix:
---------
|C|A|T|
|X|Y|S|
|A|B|C|
---------

Word: "CATS"

Result: [(0, 0), (0, 1), (0, 2), (1, 2)]

Implementation notes:
1. Use a backtracking (DFS) approach to explore all possible paths.
2. At each cell, recursively check neighbors.
    case, check: Up, Down, Left, Right.
3. Maintain a 'visited' set for each coordinate
   to ensure cells are not reused within the same search branch.
4. If a path matches the word, return the list of coordinates.
5. If a branch fails, 'backtrack' by removing the current cell from
   the visited set and the path list to allow for other potential matches.

Similar leetcode question that returns a bool: https://leetcode.com/problems/word-search/
"""


def get_point_key(len_board: int, len_board_column: int, row: int, column: int) -> int:
    """
    Returns the hash key of matrix indexes.

    >>> get_point_key(10, 20, 1, 0)
    200
    """

    return len_board * len_board_column * row + column


def get_word_path(
    board: list[list[str]],
    word: str,
    row: int,
    column: int,
    word_index: int,
    visited_points_set: set[int],
    current_path: list[tuple[int, int]],
) -> list[tuple[int, int]] | None:
    """
    Return the coordinate path if it's possible to find the word in the grid.
    """

    if board[row][column] != word[word_index]:
        return None

    # Track current progress
    new_path = [*current_path, (row, column)]

    # Base case
    if word_index == len(word) - 1:
        return new_path

    traverts_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    len_board = len(board)
    len_board_column = len(board[0])
    for direction in traverts_directions:
        next_i = row + direction[0]
        next_j = column + direction[1]

        if not (0 <= next_i < len_board and 0 <= next_j < len_board_column):
            continue

        key = get_point_key(len_board, len_board_column, next_i, next_j)
        if key in visited_points_set:
            continue
        visited_points_set.add(key)
        result = get_word_path(
            board, word, next_i, next_j, word_index + 1, visited_points_set, new_path
        )
        if result is not None:
            return result
        # Backtrack: remove key to try other paths
        visited_points_set.remove(key)

    return None


def word_search_path(board: list[list[str]], word: str) -> list[tuple[int, int]] | None:
    """
    >>> # 1. Word is found case
    >>> word_search_path([["C","A","T"],["X","Y","S"],["A","B","C"]], "CATS")
    [(0, 0), (0, 1), (0, 2), (1, 2)]

    >>> # 2. Word is not found case
    >>> word_search_path([["A","B"],["C","D"]], "ABCD") is None
    True

    >>> #  3. Word is a single char
    >>> word_search_path([["A"]], "A")
    [(0, 0)]

    >>> # 4. Invalid board error (empty list)
    >>> word_search_path([], "CAT")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.

    >>> # 5. Invalid word error
    >>> word_search_path([["A"]], 123)
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    """
    # Validation
    board_error_message = (
        "The board should be a non empty matrix of single chars strings."
    )

    # Validate board input
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError(board_error_message)
    for row in board:
        if not isinstance(row, list) or len(row) == 0:
            raise ValueError(board_error_message)
        for item in row:
            if not isinstance(item, str) or len(item) != 1:
                raise ValueError(board_error_message)

    # Validate word input
    if not isinstance(word, str) or len(word) == 0:
        raise ValueError(
            "The word parameter should be a string of length greater than 0."
        )

    rows = len(board)
    cols = len(board[0])
    # Main entry point
    for r in range(rows):
        for c in range(cols):
            # Optimization: only trigger recursion if first
            # char in board matches with first char in word.
            if board[r][c] == word[0]:
                key = get_point_key(rows, cols, r, c)
                path_result = get_word_path(board, word, r, c, 0, {key}, [])
                if path_result is not None:
                    return path_result

    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
