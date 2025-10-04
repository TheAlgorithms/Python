# created by Mayank

"""
Sliding Window Algorithm: Longest Substring Without Repeating Characters
https://en.wikipedia.org/wiki/Sliding_window

This algorithm finds the length of the longest substring within a given string
that does not contain any repeating characters. It uses a "sliding window"
approach with two pointers to efficiently track the current substring.

Complexity: O(n) where n is the length of the string.

For doctests run following command:
python3 -m doctest -v longest_substring_without_repeating_characters.py
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    :param s: The input string.
    :return: The length of the longest substring.

    Examples:
    >>> longest_substring_without_repeating_characters("abcabcbb")
    3
    >>> longest_substring_without_repeating_characters("bbbbb")
    1
    >>> longest_substring_without_repeating_characters("pwwkew")
    3
    >>> longest_substring_without_repeating_characters("")
    0
    >>> longest_substring_without_repeating_characters("abcdef")
    6
    >>> longest_substring_without_repeating_characters("tmmzuxt")
    5
    """
    char_set = set()
    left_pointer = 0
    max_length = 0

    for right_pointer in range(len(s)):
        # If the character is already in the set, shrink the window from the left
        while s[right_pointer] in char_set:
            char_set.remove(s[left_pointer])
            left_pointer += 1

        # Add the new character to the set (expanding the window)
        char_set.add(s[right_pointer])

        # Update the maximum length found so far
        max_length = max(max_length, right_pointer - left_pointer + 1)

    return max_length


if __name__ == "__main__":
    import doctest

    doctest.testmod()