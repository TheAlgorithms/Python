"""
Author  : Alexander Pantyukhin
Date    : December 12, 2022

Task:
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused
multiple times in the segmentation.

Implementation notes: Trie + Dynamic programming up -> down.
The Trie keeps all wordDict words. It will be useful for scanning
available words for the current position in the string.

Leetcode:
https://leetcode.com/problems/word-break/description/

Runtime: O(n * n)
Space: O(n)
"""

from functools import lru_cache

def word_break(s: str, word_dict: list[str]) -> bool:
    """
    Return True if numbers have opposite signs False otherwise.

    >>> word_break("applepenapple", ["apple","pen"])
    True
    >>> word_break("catsandog", ["cats","dog","sand","and","cat"])
    False
    >>> word_break("cars", ["car","ca","rs"])
    True
    >>> word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
    False
    >>> word_break('abc', [])
    False
    >>> word_break(123, ['a'])
    Traceback (most recent call last):
        ...
    ValueError: the s should be not empty string
    >>> word_break('', ['a'])
    Traceback (most recent call last):
        ...
    ValueError: the s should be not empty string
    >>> word_break('abc', [123])
    Traceback (most recent call last):
        ...
    ValueError: the word_dict should a list of non empty string
    >>> word_break('abc', [''])
    Traceback (most recent call last):
        ...
    ValueError: the word_dict should a list of non empty string
    """

    # Validation
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError('the s should be not empty string')

    if not isinstance(word_dict, list) or not all(
        [isinstance(item, str) and len(item) > 0 for item in word_dict]):
        raise ValueError('the word_dict should a list of non empty string')

    # Build trie
    trie = {}
    WORD_KEEPER = 'WORD_KEEPER'
    for word in word_dict:
        trie_node = trie
        for c in word:
            if c not in trie_node:
                trie_node[c] = {}

            trie_node = trie_node[c]
        
        trie_node[WORD_KEEPER] = True

    len_s = len(s)

    # Dynamic programming method
    @lru_cache(maxsize=None)
    def is_breakable(index: int) -> bool:
        if index == len_s:
            return True

        trie_node = trie
        for i in range(index, len_s):
            trie_node = trie_node.get(s[i], None)

            if trie_node is None:
                return False
            
            if trie_node.get(WORD_KEEPER, False) and is_breakable(i + 1):
                return True

        return False

    return is_breakable(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
