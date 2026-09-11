"""
Author  : Alexander Pantyukhin
Date    : November 24, 2022

Task:
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

Matrix:
---------
|A|B|C|E|
|S|F|C|S|
|A|D|E|E|
---------

Word:
"ABCCED"

Result:
True

Implementation notes: Use a backtracking approach.
At each point, check all neighbors to try to find the next letter of the word.

leetcode: https://leetcode.com/problems/word-search/

"""


def get_point_key(len_board: int, len_board_column: int, row: int, column: int) -> int:
    """
    Returns the hash key of matrix indexes.

    >>> get_point_key(10, 20, 1, 0)
    200
    """

    return len_board * len_board_column * row + column


def exits_word(
    board: list[list[str]],
    word: str,
    row: int,
    column: int,
    word_index: int,
    visited_points_set: set[int],
) -> bool:
    """
    Return True if it's possible to search for the word suffix
    starting from the word_index.

    >>> exits_word([["A"]], "B", 0, 0, 0, set())
    False
    """

    if board[row][column] != word[word_index]:
        return False

    if word_index == len(word) - 1:
        return True

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
        if exits_word(board, word, next_i, next_j, word_index + 1, visited_points_set):
            return True

        visited_points_set.remove(key)

    return False


def validate_board_and_word(board: list[list[str]], word: str) -> None:
    """
    >>> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    >>> validate_board_and_word(board, "ABCCED")
    >>> validate_board_and_word(board, "SEE")
    >>> validate_board_and_word(board, "ABCB")
    >>> validate_board_and_word([["A"]], "A")
    >>> validate_board_and_word([["B", "A", "A"], ["A", "A", "A"], ["A", "B", "A"]], "ABB")
    >>> validate_board_and_word([["A"]], 123)
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> validate_board_and_word([["A"]], "")
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> validate_board_and_word([[]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non-empty matrix of single-character strings.
    >>> validate_board_and_word([], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non-empty matrix of single-character strings.
    >>> validate_board_and_word([["A"], [21]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non-empty matrix of single-character strings.
    """

    # Validate board
    msg = "The board should be a non-empty matrix of single-character strings."
    if not board or not isinstance(board, list):
        raise ValueError(msg)

    for row in board:
        if not row or not isinstance(row, list):
            raise ValueError(msg)

        for item in row:
            if not item or not isinstance(item, str):
                raise ValueError(msg)

    # Validate word
    if not isinstance(word, str) or len(word) == 0:
        msg = "The word parameter should be a string of length greater than 0."
        raise ValueError(msg)


def get_word_path(board: list[list[str]], word: str) -> list[tuple[int, int]] | None:
    """
    Return the path of the word in the board if it exists; otherwise, return None.

    >>> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    >>> get_word_path(board, "ABCCED")
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1)]
    >>> get_word_path(board, "SEE")
    [(1, 3), (2, 3), (2, 2)]
    >>> get_word_path(board, "ABCB") is None
    True
    >>> get_word_path([["A"]], 123)
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    """
    validate_board_and_word(board, word)
    rows, cols = len(board), len(board[0])

    def backtrack(
        r: int,
        c: int,
        index: int,
        path: list[tuple[int, int]],
        visited: set[tuple[int, int]],
    ) -> list[tuple[int, int]] | None:
        if board[r][c] != word[index]:
            return None

        path.append((r, c))
        visited.add((r, c))

        if index == len(word) - 1:
            return path.copy()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                result = backtrack(nr, nc, index + 1, path, visited)
                if result:
                    return result

        path.pop()
        visited.remove((r, c))
        return None

    for i in range(rows):
        for j in range(cols):
            result = backtrack(i, j, 0, [], set())
            if result:
                return result

    return None


def word_exists(board: list[list[str]], word: str) -> bool:
    """
    >>> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    >>> word_exists(board, "ABCCED")
    True
    >>> word_exists(board, "SEE")
    True
    >>> word_exists(board, "ABCB")
    False
    >>> word_exists([["A"]], "A")
    True
    >>> word_exists([["B", "A", "A"], ["A", "A", "A"], ["A", "B", "A"]], "ABB")
    False
    >>> word_exists([["A"]], 123)
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> word_exists([["A"]], "")
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> word_exists([[]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non-empty matrix of single-character strings.
    >>> word_exists([], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non-empty matrix of single-character strings.
    >>> word_exists([["A"], [21]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non-empty matrix of single-character strings.
    """
    validate_board_and_word(board, word)
    len_board = len(board)
    len_board_column = len(board[0])
    for i in range(len_board):
        for j in range(len_board_column):
            if exits_word(
                board, word, i, j, 0, {get_point_key(len_board, len_board_column, i, j)}
            ):
                return True

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
