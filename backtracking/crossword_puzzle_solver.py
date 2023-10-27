# https://www.geeksforgeeks.org/solve-crossword-puzzle/


def is_valid(puzzle: list[list[str]], word: str, row: int, col: int) -> bool:
    """
    Check if a word can be placed at the given position.

    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> is_valid(puzzle, 'word', 0, 0)
    True
    """
    for i in range(len(word)):
        if row + i >= len(puzzle) or puzzle[row + i][col] != "":
            return False
    return True


def place_word(puzzle: list[list[str]], word: str, row: int, col: int) -> None:
    """
    Place a word at the given position.

    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> place_word(puzzle, 'word', 0, 0)
    >>> puzzle
    [['w', '', '', ''], ['o', '', '', ''], ['r', '', '', ''], ['d', '', '', '']]
    """
    for i in range(len(word)):
        puzzle[row + i][col] = word[i]


def remove_word(puzzle: list[list[str]], word: str, row: int, col: int) -> None:
    """
    Remove a word from the given position.

    >>> puzzle = [
    ...     ['w', '', '', ''],
    ...     ['o', '', '', ''],
    ...     ['r', '', '', ''],
    ...     ['d', '', '', '']
    ... ]
    >>> remove_word(puzzle, 'word', 0, 0)
    >>> puzzle
    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    """
    for i in range(len(word)):
        puzzle[row + i][col] = ""


def solve_crossword(puzzle: list[list[str]], words: list[str]) -> bool:
    """
    Solve the crossword puzzle using backtracking.

    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]

    >>> words = ['word', 'another', 'more', 'last']
    >>> solve_crossword(puzzle, words)
    True
    """
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == "":
                for word in words:
                    if is_valid(puzzle, word, row, col):
                        place_word(puzzle, word, row, col)
                        words.remove(word)
                        if solve_crossword(puzzle, words):
                            return True
                        words.append(word)
                        remove_word(puzzle, word, row, col)
                return False
    return True


# Replace with your actual puzzle and words
PUZZLE = [["" for _ in range(3)] for _ in range(3)]
WORDS = ["cat", "dog", "pig"]

if solve_crossword(PUZZLE, WORDS):
    print("Solution found:")
else:
    print("No solution found:")
for row in PUZZLE:
    print(" ".join(row))
