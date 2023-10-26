# https://www.geeksforgeeks.org/solve-crossword-puzzle/
def solve_crossword(puzzle, words) -> None:
    rows, cols = len(puzzle), len(puzzle[0])

    def is_valid(word, r, c, direction):
        if direction == "across":
            return c + len(word) <= cols and all(
                puzzle[r][c + i] in ("", word[i]) for i in range(len(word))
            )
        else:  # direction == "down"
            return r + len(word) <= rows and all(
                puzzle[r + i][c] in ("", word[i]) for i in range(len(word))
            )

    def place_word(word, r, c, direction) -> None:
        if direction == "across":
            for i in range(len(word)):
                puzzle[r][c + i] = word[i]
        else:  # direction == "down"
            for i in range(len(word)):
                puzzle[r + i][c] = word[i]

    def remove_word(word, r, c, direction) -> None:
        if direction == "across":
            for i in range(len(word)):
                puzzle[r][c + i] = ""
        else:  # direction == "down"
            for i in range(len(word)):
                puzzle[r + i][c] = ""

    def backtrack(puzzle, words):
        for r in range(rows):
            for c in range(cols):
                if puzzle[r][c] == "":
                    for word in words[:]:
                        for direction in ["across", "down"]:
                            if is_valid(word, r, c, direction):
                                place_word(word, r, c, direction)
                                words.remove(word)
                                if not words:
                                    return True
                                if backtrack(puzzle, words):
                                    return True
                                words.append(word)
                                remove_word(word, r, c, direction)
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
    ["#", "#", "c", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "a", "t", "#", "t", "r", "a", "#"],
    ["#", "#", "o", "#", "#", "#", "o", "#", "#"],
    ["#", "#", "w", "#", "c", "a", "r", "#", "#"],
    ["#", "#", "#", "#", "#", "a", "#", "#", "#"],
    ["#", "#", "t", "#", "t", "a", "x", "i", "#"],
    ["#", "#", "e", "#", "#", "n", "#", "#", "#"],
    ["#", "#", "n", "#", "a", "t", "e", "x", "#"],
    ["#", "#", "#", "#", "x", "#", "#", "#", "#"],
]

words = ["car", "cat", "tax", "rat", "ate", "axe", "won"]
solution = solve_crossword(puzzle, words)

if solution:
    for row in solution:
        print(" ".join(row))
else:
    print("No solution found.")
