"""
Word Ladder is a classic problem in computer science.
The problem is to transform a start word into an end word
by changing one letter at a time.
Each intermediate word must be a valid word from a given list of words.
The goal is to find a transformation sequence
from the start word to the end word.

Wikipedia: https://en.wikipedia.org/wiki/Word_ladder
"""


def word_ladder_backtrack(
    begin_word: str, end_word: str, word_list: list[str]
) -> list[str]:
    """
    Solve the Word Ladder problem using Backtracking and return
    the list of transformations from begin_word to end_word.

    Parameters:
    begin_word (str): The word from which the transformation starts.
    end_word (str): The target word for transformation.
    word_list (list[str]): The list of valid words for transformation.

    Returns:
    list[str]: The list of transformations from begin_word to end_word.
               Returns an empty list if there is no valid transformation.

    Example:
    >>> word_ladder_backtrack("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    ['hit', 'hot', 'dot', 'lot', 'log', 'cog']

    >>> word_ladder_backtrack("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    []

    >>> word_ladder_backtrack("lead", "gold", ["load", "goad", "gold", "lead", "lord"])
    ['lead', 'lead', 'load', 'goad', 'gold']

    >>> word_ladder_backtrack("game", "code", ["came", "cage", "code", "cade", "gave"])
    ['game', 'came', 'cade', 'code']
    """

    # Step 1: Convert the word_list to a set for faster lookup
    word_set = set(word_list)

    # Step 2: If end_word is not in the word_list, return an empty list
    if end_word not in word_set:
        return []

    # Step 3: Backtracking function to find the word ladder
    def backtrack(current_word, path):
        # Base case: If the current word is the end word, return the path
        if current_word == end_word:
            return path

        # Try all possible single-letter transformations
        for i in range(len(current_word)):
            for c in "abcdefghijklmnopqrstuvwxyz":  # Try changing each letter
                transformed_word = current_word[:i] + c + current_word[i + 1 :]

                # If the transformed word is valid and has not been visited
                if transformed_word in word_set:
                    # Remove it from the set to avoid revisiting
                    word_set.remove(transformed_word)
                    # Recur with the new word added to the path
                    result = backtrack(transformed_word, [*path, transformed_word])
                    if result:  # If we found a valid result, return it
                        return result
                    # Add it back to the set after exploring this path (backtrack)
                    word_set.add(transformed_word)

        # If no valid path is found, return an empty list
        return []

    # Step 4: Start backtracking from the begin_word
    return backtrack(begin_word, [begin_word])
