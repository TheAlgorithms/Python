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
For each point need to check neigh neighbours
and try to find left suffix of the word.

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
    >>> word_exists([["A","A","A","A","A","A"],\
                     ["A","A","A","A","A","A"],\
                     ["A","A","A","A","A","A"],\
                     ["A","A","A","A","A","A"],\
                     ["A","A","A","A","A","B"],\
                     ["A","A","A","A","B","A"]],\
                    "AAAAAAAAAAAAABB")
    False
    """

    traverts_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    len_word = len(word)
    len_board = len(board)
    len_board_column = 0 if len_board == 0 else len(board[0])

    # Returns the hash key of matrix indexes.
    def get_point_key(i: int, j: int) -> int:
        return len_board * len_board_column * i + j

    # Return True if it's possible to search the word suffix
    # starting from the word_index.
    def exits_word(i: int,
                    j: int,
                    word_index:int,
                    visited_points_set: set[int]) -> bool:

        if board[i][j] != word[word_index]:
            return False

        if word_index == len_word - 1:
            return True
        
        for direction in traverts_directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if next_i < 0 or \
                next_i >= len_board or \
                next_j < 0 or \
                next_j >= len_board_column:
                continue

            key = get_point_key(next_i, next_j)
            if key in visited_points_set:
                continue
            
            visited_points_set.add(key)
            if exits_word(next_i,
                          next_j,
                          word_index + 1,
                          visited_points_set):
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
