"""
Word Ladder is a classic problem in computer science.
The problem is to transform a start word into an end word
by changing one letter at a time.
Each intermediate word must be a valid word from a given list of words.
The goal is to find a transformation sequence
from the start word to the end word.

Wikipedia: https://en.wikipedia.org/wiki/Word_ladder
"""

import string


def backtrack(
    current_word: str, path: list[str], end_word: str, word_set: set[str]
) -> list[str]:
    """
    Helper function to perform backtracking to find the transformation
    from the current_word to the end_word.

    Parameters:
    current_word (str): The current word in the transformation sequence.
    path (list[str]): The list of transformations from begin_word to current_word.
    end_word (str): The target word for transformation.
    word_set (set[str]): The set of valid words for transformation.

    Returns:
    list[str]: The list of transformations from begin_word to end_word.
               Returns an empty list if there is no valid
                transformation from current_word to end_word.

    Example:
    >>> backtrack("hit", ["hit"], "cog", {"hot", "dot", "dog", "lot", "log", "cog"})
    ['hit', 'hot', 'dot', 'lot', 'log', 'cog']

    >>> backtrack("hit", ["hit"], "cog", {"hot", "dot", "dog", "lot", "log"})
    []

    >>> backtrack("lead", ["lead"], "gold", {"load", "goad", "gold", "lead", "lord"})
    ['lead', 'lead', 'load', 'goad', 'gold']

    >>> backtrack("game", ["game"], "code", {"came", "cage", "code", "cade", "gave"})
    ['game', 'came', 'cade', 'code']
    """

    # Base case: If the current word is the end word, return the path
    if current_word == end_word:
        return path

    # Try all possible single-letter transformations
    for i in range(len(current_word)):
        for c in string.ascii_lowercase:  # Try changing each letter
            transformed_word = current_word[:i] + c + current_word[i + 1 :]
            if transformed_word in word_set:
                word_set.remove(transformed_word)
                # Recur with the new word added to the path
                result = backtrack(
                    transformed_word, [*path, transformed_word], end_word, word_set
                )
                if result:  # valid transformation found
                    return result
                word_set.add(transformed_word)  # backtrack

    return []  # No valid transformation found


def word_ladder(begin_word: str, end_word: str, word_set: set[str]) -> list[str]:
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
    >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    ['hit', 'hot', 'dot', 'lot', 'log', 'cog']

    >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    []

    >>> word_ladder("lead", "gold", ["load", "goad", "gold", "lead", "lord"])
    ['lead', 'lead', 'load', 'goad', 'gold']

    >>> word_ladder("game", "code", ["came", "cage", "code", "cade", "gave"])
    ['game', 'came', 'cade', 'code']
    """

    if end_word not in word_set:  # no valid transformation possible
        return []

    # Perform backtracking starting from the begin_word
    return backtrack(begin_word, [begin_word], end_word, word_set)
