"""
Author  : Alexander Pantyukhin
Date    : December 16, 2022

Task:

Given a string text. You should split it to k substrings
(subtext1, subtext2, ..., subtextk) such that:

 - subtexti is a non-empty string.

 - The concatenation of all the substrings is equal to text
 (i.e., subtext1 + subtext2 + ... + subtextk == text).

 - subtexti == subtextk - i + 1 for all valid values
 of i (i.e., 1 <= i <= k).

Return the largest possible value of k.

Leetcode reference:
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/

Implementation notes:
Use greedy approach. If it's possible to find the palindrome
chunk for the current text start, then use it and apply recursion
for the left path of string.

Runtime: O(n*n)
Space: O(1)
"""


def longest_decomposition(text: str) -> int:
    """
    >>> longest_decomposition('ghiabcdefhelloadamhelloabcdefghi')
    7
    >>> longest_decomposition('merchant')
    1
    >>> longest_decomposition('m')
    1
    >>> longest_decomposition('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    46
    >>> longest_decomposition('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc')
    15
    """

    if not text:
        raise ValueError("The text must be a non-empty string.")

    len_text = len(text)

    def substrings_are_equal(
        first_substring_index: int, second_substring_index: int, length: int
    ) -> bool:
        for i in range(length):
            if text[first_substring_index + i] != text[second_substring_index + i]:
                return False

        return True

    def longest_decomposition(index: int) -> int:
        if 2 * index >= len_text:
            return 0

        ch = text[index]
        result = 1

        for i in range((len_text - 2 * index) // 2):
            if ch == text[len_text - 1 - index - i] and substrings_are_equal(
                index, len_text - 1 - index - i, i + 1
            ):
                return max(result, 2 + longest_decomposition(index + i + 1))

        return result

    return longest_decomposition(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
