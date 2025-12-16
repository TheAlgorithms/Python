"""
Longest substring without repeating characters Problem Statement: Given a string,
find the length of longest substring without repeating characters.
Example: The longest substring without repeating characters in the string
"abcabcbb" is "abc". Therefore, algorithm should return 3 as the output.
"""


def longest_substring_without_repeating_characters(string: str) -> int:
    """
    Finds the length of longest substring without repeating characters.
    >>> longest_substring_without_repeating_characters("abcabcbb")
    3
    >>> longest_substring_without_repeating_characters("bbbbb")
    1
    >>> longest_substring_without_repeating_characters("pwwkew")
    3
    >>> longest_substring_without_repeating_characters("")
    0
    >>> longest_substring_without_repeating_characters("a")
    1
    >>> longest_substring_without_repeating_characters("heaesgliengs")
    6
    >>> longest_substring_without_repeating_characters("general kenobi")
    10
    >>> longest_substring_without_repeating_characters("that's what she said")
    7
    >>> longest_substring_without_repeating_characters(69)
    Traceback (most recent call last):
        ...
    ValueError: longest_substring_without_repeating_characters() takes a string as input
    """

    if not isinstance(string, str):
        raise ValueError(
            "longest_substring_without_repeating_characters() takes a string as input"
        )

    char_set: set[str] = set()
    start = 0
    max_length = 0

    for end in range(len(string)):
        while string[end] in char_set:
            char_set.remove(string[start])
            start += 1
        char_set.add(string[end])
        if max_length < end - start + 1:
            max_length = end - start + 1

    return max_length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
