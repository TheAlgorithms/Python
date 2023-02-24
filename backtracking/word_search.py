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

Implementation notes: Use backtracking approach.
At each point, check all neighbors to try to find the next letter of the word.

leetcode: https://leetcode.com/problems/word-search/

"""


def word_exists(board: list[list[str]], word: str) -> bool:
    """
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    True
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    False
    >>> word_exists([["A"]], "A")
    True
    >>> word_exists([["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","B"],
    ...              ["A","A","A","A","B","A"]],
    ...             "AAAAAAAAAAAAABB")
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
    ValueError: The board should be a non empty matrix of single chars strings.
    >>> word_exists([], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    >>> word_exists([["A"], [21]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    """

    # Validate board
    board_error_message = (
        "The board should be a non empty matrix of single chars strings."
    )
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError(board_error_message)

    for row in board:
        if not isinstance(row, list) or len(row) == 0:
            raise ValueError(board_error_message)

        for item in row:
            if not isinstance(item, str) or len(item) != 1:
                raise ValueError(board_error_message)

    # Validate word
    if not isinstance(word, str) or len(word) == 0:
        raise ValueError(
            "The word parameter should be a string of length greater than 0."
        )

    traverts_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    len_word = len(word)
    len_board = len(board)
    len_board_column = len(board[0])

    # Returns the hash key of matrix indexes.
    def get_point_key(row: int, column: int) -> int:
        """
        >>> len_board=10
        >>> len_board_column=20
        >>> get_point_key(0, 0)
        200
        """

        return len_board * len_board_column * row + column

    # Return True if it's possible to search the word suffix
    # starting from the word_index.
    def exits_word(
        row: int, column: int, word_index: int, visited_points_set: set[int]
    ) -> bool:
        """
        >>> board=[["A"]]
        >>> word="B"
        >>> exits_word(0, 0, 0, set())
        False
        """

        if board[row][column] != word[word_index]:
            return False

        if word_index == len_word - 1:
            return True

        for direction in traverts_directions:
            next_i = row + direction[0]
            next_j = column + direction[1]
            if not (0 <= next_i < len_board and 0 <= next_j < len_board_column):
                continue

            key = get_point_key(next_i, next_j)
            if key in visited_points_set:
                continue

            visited_points_set.add(key)
            if exits_word(next_i, next_j, word_index + 1, visited_points_set):
                return True

            visited_points_set.remove(key)

        return False

    for i in range(len_board):
        for j in range(len_board_column):
            if exits_word(i, j, 0, {get_point_key(i, j)}):
                return True

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
