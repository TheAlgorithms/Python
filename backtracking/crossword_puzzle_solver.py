# https://www.geeksforgeeks.org/solve-crossword-puzzle/


def is_valid(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> bool:
    """
    Check if a word can be placed at the given position.
    A cell is valid if it is empty or already contains the correct letter
    (enabling crossing/intersection between words).

    >>> puzzle = [['', '', '', ''], ['', '', '', ''],
    ...           ['', '', '', ''], ['', '', '', '']]
    >>> is_valid(puzzle, 'word', 0, 0, True)
    True
    >>> is_valid(puzzle, 'word', 0, 0, False)
    True
    >>> puzzle2 = [['w', '', ''], ['o', '', ''], ['r', '', ''], ['d', '', '']]
    >>> is_valid(puzzle2, 'word', 0, 0, True)
    True
    >>> is_valid(puzzle2, 'cat', 0, 0, True)
    False
    """
    rows, cols = len(puzzle), len(puzzle[0])
    for i, ch in enumerate(word):
        r, c = (row + i, col) if vertical else (row, col + i)
        if r >= rows or c >= cols:
            return False
        cell = puzzle[r][c]
        if cell != "" and cell != ch:
            return False
    return True


def place_word(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> None:
    """
    Place a word at the given position in the puzzle.

    >>> puzzle = [['', '', '', ''], ['', '', '', ''],
    ...           ['', '', '', ''], ['', '', '', '']]
    >>> place_word(puzzle, 'word', 0, 0, True)
    >>> puzzle
    [['w', '', '', ''], ['o', '', '', ''], ['r', '', '', ''], ['d', '', '', '']]
    """
    for i, ch in enumerate(word):
        if vertical:
            puzzle[row + i][col] = ch
        else:
            puzzle[row][col + i] = ch


def remove_word(
    puzzle: list[list[str]],
    word: str,
    row: int,
    col: int,
    vertical: bool,
    snapshot: list[list[str]],
) -> None:
    """
    Remove a word from the puzzle, restoring only cells that were empty
    before placement. Cells shared with crossing words are preserved.

    >>> puzzle = [['w', 'o', 'r', 'd'], ['', '', '', ''],
    ...           ['', '', '', ''], ['', '', '', '']]
    >>> snap = [['', 'o', 'r', 'd'], ['', '', '', ''],
    ...         ['', '', '', ''], ['', '', '', '']]
    >>> remove_word(puzzle, 'word', 0, 0, False, snap)
    >>> puzzle
    [['', 'o', 'r', 'd'], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    """
    for i in range(len(word)):
        r, c = (row + i, col) if vertical else (row, col + i)
        if snapshot[r][c] == "":
            puzzle[r][c] = ""


def solve_crossword(puzzle: list[list[str]], words: list[str]) -> bool:
    """
    Solve the crossword puzzle using backtracking.
    Words are tried longest-first to prune the search space early.
    Intersections between words (shared letters) are supported.

    >>> puzzle = [['', '', '', ''], ['', '', '', ''],
    ...           ['', '', '', ''], ['', '', '', '']]
    >>> solve_crossword(puzzle, ['word', 'four', 'more', 'last'])
    True
    >>> puzzle2 = [['', '', '', ''], ['', '', '', ''],
    ...            ['', '', '', ''], ['', '', '', '']]
    >>> solve_crossword(puzzle2, ['word', 'four', 'more', 'paragraphs'])
    False
    """
    if not words:
        return True

    remaining = sorted(words, key=len, reverse=True)
    word, rest = remaining[0], remaining[1:]

    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            for vertical in (True, False):
                if is_valid(puzzle, word, row, col, vertical):
                    snapshot = [r[:] for r in puzzle]
                    place_word(puzzle, word, row, col, vertical)
                    if solve_crossword(puzzle, rest):
                        return True
                    remove_word(puzzle, word, row, col, vertical, snapshot)

    return False


if __name__ == "__main__":
    PUZZLE = [[""] * 3 for _ in range(3)]
    WORDS = ["cat", "dog", "car"]
    if solve_crossword(PUZZLE, WORDS):
        print("Solution found:")
        for row in PUZZLE:
            print(" ".join(cell or "." for cell in row))
    else:
        print("No solution found.")
