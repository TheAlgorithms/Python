"""
Regex matching check if a text matches wildcard pattern or not.
Pattern:
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
"""


def recursive_match(text: str, pattern: str) -> bool:
    """
    Recursive matching algorithm.

    Time complexity: O(2 ^ (m + n)), where m is the length of text and n is the length of pattern.
    Space complexity: Recursion depth is O(m + n).

    :param text: Text to match.
    :param pattern: Pattern to match.
    :return: True if text matches pattern, False otherwise.

    >>> recursive_match('abc', 'a.c')
    True
    >>> recursive_match('abc', 'af*.c')
    True
    >>> recursive_match('abc', 'a.c*')
    True
    >>> recursive_match('abc', 'a.c*d')
    False
    """
    if not text and not pattern:
        return True

    if text and not pattern:
        return False

    if not text and pattern and pattern[-1] != '*':
        return False

    if not text and pattern and pattern[-1] == '*':
        return recursive_match(text, pattern[:-2])

    if text[-1] == pattern[-1] or pattern[-1] == '.':
        return recursive_match(text[:-1], pattern[:-1])

    if pattern[-1] == '*':
        return recursive_match(text[:-1], pattern) or recursive_match(text, pattern[:-2])

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
