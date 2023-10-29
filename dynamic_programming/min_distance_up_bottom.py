"""
Author  : Alexander Pantyukhin
Date    : October 14, 2022
This is an implementation of the up-bottom approach to find edit distance.
The implementation was tested on Leetcode: https://leetcode.com/problems/edit-distance/

Levinstein distance
Dynamic Programming: up -> down.
"""

import functools


def min_distance_up_bottom(word1: str, word2: str) -> int:
    """
    >>> min_distance_up_bottom("intention", "execution")
    5
    >>> min_distance_up_bottom("intention", "")
    9
    >>> min_distance_up_bottom("", "")
    0
    >>> min_distance_up_bottom("zooicoarchaeologist", "zoologist")
    10
    """
    len_word1 = len(word1)
    len_word2 = len(word2)

    @functools.cache
    def min_distance(index1: int, index2: int) -> int:
        # if first word index overflows - delete all from the second word
        if index1 >= len_word1:
            return len_word2 - index2
        # if second word index overflows - delete all from the first word
        if index2 >= len_word2:
            return len_word1 - index1
        diff = int(word1[index1] != word2[index2])  # current letters not identical
        return min(
            1 + min_distance(index1 + 1, index2),
            1 + min_distance(index1, index2 + 1),
            diff + min_distance(index1 + 1, index2 + 1),
        )

    return min_distance(0, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
