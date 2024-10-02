"""
Word Break Problem is a well-known problem in computer science.
Given a string and a dictionary of words, the task is to determine if
the string can be segmented into a sequence of one or more dictionary words.

Wikipedia: https://en.wikipedia.org/wiki/Word_break_problem
"""


def backtrack(s: str, word_dict: set[str], start: int) -> bool:
    """
    Helper function that uses backtracking to determine if a valid
    word segmentation is possible starting from index 'start'.

    Parameters:
    s (str): The input string.
    word_dict (set[str]): A set of valid dictionary words.
    start (int): The starting index of the substring to be checked.

    Returns:
    bool: True if a valid segmentation is possible, otherwise False.

    Example:
    >>> backtrack("leetcode", {"leet", "code"}, 0)
    True

    >>> backtrack("applepenapple", {"apple", "pen"}, 0)
    True

    >>> backtrack("catsandog", {"cats", "dog", "sand", "and", "cat"}, 0)
    False
    """

    # Base case: if the starting index has reached the end of the string
    if start == len(s):
        return True

    # Try every possible substring from 'start' to 'end'
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in word_dict and backtrack(s, word_dict, end):
            return True

    return False


def word_break(s: str, word_dict: set[str]) -> bool:
    """
    Determines if the input string can be segmented into a sequence of
    one or more dictionary words using backtracking.

    Parameters:
    s (str): The input string to segment.
    word_dict (set[str]): The set of valid words.

    Returns:
    bool: True if the string can be segmented into valid words, otherwise False.

    Example:
    >>> word_break("leetcode", {"leet", "code"})
    True

    >>> word_break("applepenapple", {"apple", "pen"})
    True

    >>> word_break("catsandog", {"cats", "dog", "sand", "and", "cat"})
    False
    """

    return backtrack(s, word_dict, 0)
