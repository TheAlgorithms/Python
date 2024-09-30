"""
Word Ladder is

Wikipedia: https://en.wikipedia.org/wiki/Word_ladder
"""


from collections import deque


def word_ladder(beginWord: str, endWord: str, wordList: list[str]) -> int:
    """
    Solve the Word Ladder problem using Breadth-First Search (BFS).

    Parameters:
    beginWord (str): The word from which the transformation starts.
    endWord (str): The target word for transformation.
    wordList (list[str]): The list of valid words for transformation.

    Returns:
    int: The minimum number of transformations required to reach endWord from beginWord.
         Returns 0 if there is no valid transformation.

    Example:
    >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    5

    >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    0

    >>> word_ladder("lead", "gold", ["load", "goad", "gold", "lead", "lord"])
    4

    >>> word_ladder("game", "code", ["came", "cage", "code", "cade", "gave"])
    4
    """

    # Step 1: Convert the wordList to a set for faster lookup
    word_set = set(wordList)

    # Step 2: If endWord is not in the wordList, return 0 (impossible transformation)
    if endWord not in word_set:
        return 0

    # Step 3: Initialize the BFS queue
    # Each element in the queue will be a tuple: (current_word, current_depth)
    # The depth starts at 1 (including the initial word)
    queue = deque([(beginWord, 1)])

    # Step 4: Perform BFS
    while queue:
        current_word, depth = queue.popleft()

        # If the current word is the endWord, return the current depth
        if current_word == endWord:
            return depth

        # Generate all possible transformations of the current_word
        for i in range(len(current_word)):
            for c in "abcdefghijklmnopqrstuvwxyz":  # Try changing each letter
                transformed_word = current_word[:i] + c + current_word[i + 1:]

                # If the transformed word is in the word set, it's a valid transformation
                if transformed_word in word_set:
                    # Remove from the set to prevent revisiting
                    word_set.remove(transformed_word)
                    # Add the transformed word to the queue with an incremented depth
                    queue.append((transformed_word, depth + 1))

    # If no transformation is found, return 0
    return 0
