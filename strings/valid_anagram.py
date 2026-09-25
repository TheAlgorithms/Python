"""
Checks whether two strings are valid anagrams of each other.

An anagram is a word formed by rearranging the letters of another word,
using all the original letters exactly once.

For example:
listen → silent
evil → live

This can be done efficiently using Python's collections.Counter
to compare character frequencies in both strings.

Example:
>>> is_anagram("listen", "silent")
True
>>> is_anagram("evil", "vile")
True
>>> is_anagram("hello", "bello")
False
>>> is_anagram("", "")
True
>>> is_anagram("a", "aa")
False
"""

from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    """
    Returns True if the two input strings are anagrams of each other.

    The comparison is case-sensitive and ignores no characters.

    >>> is_anagram("listen", "silent")
    True
    >>> is_anagram("triangle", "integral")
    True
    >>> is_anagram("apple", "papel")
    True
    >>> is_anagram("rat", "car")
    False
    >>> is_anagram("a", "aa")
    False
    """
    return Counter(s1) == Counter(s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
