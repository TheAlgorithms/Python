 def is_valid(puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool) -> bool:
    """
    Check if a word can be placed at the given position without conflicts.

    Parameters:
    ----------
    puzzle : list[list[str]]
        The crossword grid represented as a list of lists.
    word : str
        The word to be placed.
    row : int
        The starting row position.
    col : int
        The starting column position.
    vertical : bool
        Whether the word is placed vertically or horizontally.

    Returns:
    -------
    bool
        True if the word can be placed, False otherwise.
    """
    for i in range(len(word)):
        if vertical:
            if row + i >= len(puzzle) or (puzzle[row + i][col] not in ["", word[i]]):
                return False
        else:
            if col + i >= len(puzzle[0]) or (puzzle[row][col + i] not in ["", word[i]]):
                return False
    return True

def place_word(puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool) -> None:
    """
    Place a word at the given position in the puzzle.

    Parameters:
    ----------
    puzzle : list[list[str]]
        The crossword grid represented as a list of lists.
    word : str
        The word to be placed.
    row : int
        The starting row position.
    col : int
        The starting column position.
    vertical : bool
        Whether the word is placed vertically or horizontally.

    Returns:
    -------
    None
    """
    for i, char in enumerate(word):
        if vertical:
            puzzle[row + i][col] = char
        else:
            puzzle[row][col + i] = char

def remove_word(puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool) -> None:
    """
    Remove a word from the given position in the puzzle.

    Parameters:
    ----------
    puzzle : list[list[str]]
        The crossword grid represented as a list of lists.
    word : str
        The word to be removed.
    row : int
        The starting row position.
    col : int
        The starting column position.
    vertical : bool
        Whether the word was placed vertically or horizontally.

    Returns:
    -------
    None
    """
    for i in range(len(word)):
        if vertical:
            puzzle[row + i][col] = ""
        else:
            puzzle[row][col + i] = ""

def solve_crossword(puzzle: list[list[str]], words: list[str]) -> bool:
    """
    Solve the crossword puzzle using backtracking.

    Parameters:
    ----------
    puzzle : list[list[str]]
        The crossword grid represented as a list of lists.
    words : list[str]
        A list of words to be placed in the puzzle.

    Returns:
    -------
    bool
        True if the puzzle is solved, False otherwise.
    """
    if not words:
        return True  # All words have been placed successfully

    word = words[0]
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            for vertical in [True, False]:
                if is_valid(puzzle, word, row, col, vertical):
                    place_word(puzzle, word, row, col, vertical)
                    if solve_crossword(puzzle, words[1:]):
                        return True
                    remove_word(puzzle, word, row, col, vertical)
    return False

def display_puzzle(puzzle: list[list[str]]) -> None:
    """
    Display the crossword puzzle grid.

    Parameters:
    ----------
    puzzle : list[list[str]]
        The crossword grid represented as a list of lists.

    Returns:
    -------
    None
    """
    for row in puzzle:
        print(" ".join(cell if cell else "." for cell in row))

if __name__ == "__main__":
    # Example puzzle and words
    PUZZLE = [[""] * 5 for _ in range(5)]
    WORDS = ["cat", "dog", "car"]

    if solve_crossword(PUZZLE, WORDS):
        print("Solution found:")
        display_puzzle(PUZZLE)
    else:
        print("No solution found.")
