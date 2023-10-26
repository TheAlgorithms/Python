"""
    Solve a crossword puzzle by placing words from the provided list into the puzzle.

    Args:
        puzzle (List[List[str]]): The crossword puzzle grid.
        words (List[str]): List of words to place in the puzzle.

    Returns:
        Optional[List[List[str]]]: The solved crossword puzzle, or None if no solution is found.
"""
from typing import List, Optional


def solve_crossword(
    puzzle: List[List[str]], words: List[str]
) -> Optional[List[List[str]]]:
    rows, cols = len(puzzle), len(puzzle[0])

    def is_valid_placement(word: str, row: int, col: int, direction: str) -> bool:
        """
        Check if placing a word in a specific direction at a given position is valid.

        Args:
            word (str): The word to be placed.
            row (int): The starting row position.
            col (int): The starting column position.
            direction (str): Either "across" or "down".

        Returns:
            bool: True if the placement is valid, otherwise False.
        """
        if direction == "across":
            return col + len(word) <= cols and all(
                puzzle[row][col + i] in ("", word[i]) for i in range(len(word))
            )
        else:  # direction == "down"
            return row + len(word) <= rows and all(
                puzzle[row + i][col] in ("", word[i]) for i in range(len(word))
            )

    def place_word(word: str, row: int, col: int, direction: str) -> None:
        """
        Place a word in the crossword puzzle at a specific position and direction.

        Args:
            word (str): The word to be placed.
            row (int): The starting row position.
            col (int): The starting column position.
            direction (str): Either "across" or "down".

        Returns:
            None
        """
        if direction == "across":
            for i in range(len(word)):
                puzzle[row][col + i] = word[i]
        else:  # direction == "down"
            for i in range(len(word)):
                puzzle[row + i][col] = word[i]

    def remove_word(word: str, row: int, col: int, direction: str) -> None:
        """
        Remove a word from the crossword puzzle at a specific position and direction.

        Args:
            word (str): The word to be removed.
            row (int): The starting row position.
            col (int): The starting column position.
            direction (str): Either "across" or "down".

        Returns:
            None
        """
        if direction == "across":
            for i in range(len(word)):
                puzzle[row][col + i] = ""
        else:  # direction == "down"
            for i in range(len(word)):
                puzzle[row + i][col] = ""

    def backtrack(puzzle: List[List[str]], words: List[str]) -> bool:
        """
        Recursively backtrack to solve the crossword puzzle.

        Args:
            puzzle (List[List[str]]): The crossword puzzle grid.
            words (List[str]): List of words to place in the puzzle.

        Returns:
            bool: True if a solution is found, otherwise False.
        """
        for row in range(rows):
            for col in range(cols):
                if puzzle[row][col] == "":
                    for word in words[:]:
                        for direction in ["across", "down"]:
                            if is_valid_placement(word, row, col, direction):
                                place_word(word, row, col, direction)
                                words.remove(word)
                                if not words:
                                    return True
                                if backtrack(puzzle, words):
                                    return True
                                words.append(word)
                                remove_word(word, row, col, direction)
                    return False
        return True

    # Create a copy of the puzzle to preserve the original
    copied_puzzle = [row[:] for row in puzzle]
    if backtrack(copied_puzzle, words):
        return copied_puzzle
    else:
        return None


# Example usage:
puzzle = [
    ["#", "#", "c", "#", "#", "#", "#"],
    ["#", "#", "r", "a", "c", "k", "#"],
    ["#", "#", "o", "#", "#", "#", "#"],
    ["#", "#", "r", "#", "b", "#", "#"],
    ["#", "#", "a", "a", "t", "a", "x"],
    ["#", "#", "t", "#", "i", "n", "#"],
    ["#", "#", "e", "#", "n", "#", "#"],
]
words = ["car", "rack", "bat", "cat", "rat", "in", "tax", "eat"]
solution = solve_crossword(puzzle, words)

if solution:
    for row in solution:
        print(" ".join(row))
else:
    print("No solution found.")
