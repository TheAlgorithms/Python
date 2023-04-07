"""
Author  : Alexander Pantyukhin
Date    : December 12, 2022

Task:
Given a string and a list of words, return true if the string can be
segmented into a space-separated sequence of one or more words.

Note that the same word may be reused
multiple times in the segmentation.

Implementation notes: Trie + Dynamic programming up -> down.
The Trie will be used to store the words. It will be useful for scanning
available words for the current position in the string.

Leetcode:
https://leetcode.com/problems/word-break/description/

Runtime: O(n * n)
Space: O(n)
"""

import functools
from typing import Any


def word_break(string: str, words: list[str]) -> bool:
    """
    Return True if numbers have opposite signs False otherwise.

    >>> word_break("applepenapple", ["apple","pen"])
    True
    >>> word_break("catsandog", ["cats","dog","sand","and","cat"])
    False
    >>> word_break("cars", ["car","ca","rs"])
    True
    >>> word_break('abc', [])
    False
    >>> word_break(123, ['a'])
    Traceback (most recent call last):
        ...
    ValueError: the string should be not empty string
    >>> word_break('', ['a'])
    Traceback (most recent call last):
        ...
    ValueError: the string should be not empty string
    >>> word_break('abc', [123])
    Traceback (most recent call last):
        ...
    ValueError: the words should be a list of non-empty strings
    >>> word_break('abc', [''])
    Traceback (most recent call last):
        ...
    ValueError: the words should be a list of non-empty strings
    """

    # Validation
    if not isinstance(string, str) or len(string) == 0:
        raise ValueError("the string should be not empty string")

    if not isinstance(words, list) or not all(
        isinstance(item, str) and len(item) > 0 for item in words
    ):
        raise ValueError("the words should be a list of non-empty strings")

    # Build trie
    trie: dict[str, Any] = {}
    word_keeper_key = "WORD_KEEPER"

    for word in words:
        trie_node = trie
        for c in word:
            if c not in trie_node:
                trie_node[c] = {}

            trie_node = trie_node[c]

        trie_node[word_keeper_key] = True

    len_string = len(string)

    # Dynamic programming method
    @functools.cache
    def is_breakable(index: int) -> bool:
        """
        >>> string = 'a'
        >>> is_breakable(1)
        True
        """
        if index == len_string:
            return True

        trie_node = trie
        for i in range(index, len_string):
            trie_node = trie_node.get(string[i], None)

            if trie_node is None:
                return False

            if trie_node.get(word_keeper_key, False) and is_breakable(i + 1):
                return True

        return False

    return is_breakable(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
