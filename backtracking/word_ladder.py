"""
Word Ladder is a classic problem in computer science.
The problem is to transform a start word into an end word
by changing one letter at a time.
Each intermediate word must be a valid word from a given list of words.
The goal is to find the minimum length transformation sequence
from the start word to the end word.

Wikipedia: https://en.wikipedia.org/wiki/Word_ladder
"""

from collections import deque


def word_ladder(begin_word: str, end_word: str, word_list: list[str]) -> list[str]:
    """
    Solve the Word Ladder problem using Breadth-First Search (BFS) and return
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
    ['hit', 'hot', 'dot', 'dog', 'cog']

    >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    []

    >>> word_ladder("lead", "gold", ["load", "goad", "gold", "lead", "lord"])
    ['lead', 'load', 'goad', 'gold']

    >>> word_ladder("game", "code", ["came", "cage", "code", "cade", "gave"])
    ['game', 'came', 'cade', 'code']
    """

    # Step 1: Convert the word_list to a set for faster lookup
    word_set = set(word_list)

    # Step 2: If end_word is not in the word_list, return an empty list
    if end_word not in word_set:
        return []

    # Step 3: Initialize the BFS queue
    # Each element in the queue will be a tuple: (current_word, current_path)
    # current_path tracks the sequence of transformations
    queue = deque([(begin_word, [begin_word])])

    # Step 4: Perform BFS
    while queue:
        current_word, path = queue.popleft()

        # If the current word is the end_word, return the path
        if current_word == end_word:
            return path

        # Generate all possible transformations of the current_word
        for i in range(len(current_word)):
            for c in "abcdefghijklmnopqrstuvwxyz":  # Try changing each letter
                transformed_word = current_word[:i] + c + current_word[i + 1:]

                # valid transformation: If the transformed word is in the word set
                if transformed_word in word_set:
                    # Remove from the set to prevent revisiting
                    word_set.remove(transformed_word)
                    # Add the transformed word to the queue with the updated path
                    queue.append((transformed_word, [*path, transformed_word]))

    # If no transformation is found, return an empty list
    return []
