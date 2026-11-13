"""
Longest Common Prefix

Find the longest string that is shared as a prefix by every string in a list.

The list is sorted first and only the lexicographically smallest and the
largest string are compared: a prefix shared by the whole list is necessarily
a prefix of both extremes, so no other pair has to be examined.

Reference: https://en.wikipedia.org/wiki/Longest_common_prefix
"""


def longest_common_prefix_of_two(first: str, second: str) -> str:
    """
    Return the longest prefix shared by ``first`` and ``second``.

    >>> longest_common_prefix_of_two("flower", "flow")
    'flow'
    >>> longest_common_prefix_of_two("abc", "xyz")
    ''
    >>> longest_common_prefix_of_two("", "anything")
    ''
    >>> longest_common_prefix_of_two("same", "same")
    'same'
    """
    index = 0
    shortest_length = min(len(first), len(second))
    while index < shortest_length and first[index] == second[index]:
        index += 1
    return first[:index]


def longest_common_prefix(strings: list[str]) -> str:
    """
    Return the longest string that is a prefix of every element of ``strings``.

    An empty list, or a list whose strings diverge at the first character,
    yields the empty string.

    >>> longest_common_prefix(["flower", "flow", "flight"])
    'fl'
    >>> longest_common_prefix(["dog", "racecar", "car"])
    ''
    >>> longest_common_prefix(["interview"])
    'interview'
    >>> longest_common_prefix(["", "banana"])
    ''
    >>> longest_common_prefix(["prefix", "prefix", "prefix"])
    'prefix'
    >>> longest_common_prefix(["ab", "abc", "abcd"])
    'ab'
    >>> longest_common_prefix([])
    ''

    A non-string element is rejected:

    >>> longest_common_prefix(["flow", 42])
    Traceback (most recent call last):
        ...
    ValueError: all elements of `strings` must be strings
    """
    for word in strings:
        if not isinstance(word, str):
            raise ValueError("all elements of `strings` must be strings")

    if not strings:
        return ""

    ordered = sorted(strings)
    return longest_common_prefix_of_two(ordered[0], ordered[-1])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
