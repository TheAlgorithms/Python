"""
String abbreviation problem solved using dynamic programming.

Given two strings 'a' and 'b', determine if 'a' can be transformed to 'b' by:
1. Capitalizing zero or more of 'a's lowercase letters at any index.
2. Deleting all remaining lowercase letters.

Reference: https://www.hackerrank.com/challenges/Abbr/problem

Example:
    a = "daBcd" and b = "ABC"
    "daBcd" -> capitalize 'a' and 'c' to get "dABCd" -> delete 'd' to get "ABC"
"""


def abbreviation(a: str, b: str) -> bool:
    """Check if string 'a' can be transformed to 'b'.

    Uses dynamic programming where dp[i][j] indicates whether the first i
    characters of 'a' can be transformed to the first j characters of 'b'.

    Args:
        a: The source string containing lowercase and uppercase letters.
        b: The target string containing only uppercase letters.

    Returns:
        True if 'a' can be transformed to 'b', False otherwise.

    Examples:
    >>> abbreviation("daBcd", "ABC")
    True
    >>> abbreviation("dBcd", "ABC")
    False
    >>> abbreviation("ABC", "ABC")
    True
    >>> abbreviation("abc", "ABC")
    False
    >>> abbreviation("abCD", "ABCD")
    True
    """
    n = len(a)
    m = len(b)

    # Early exit: if 'b' has lowercase letters, it can never match
    if b != b.upper():
        return False

    # Early exit: if 'a' has more uppercase letters than the length of 'b'
    a_upper_count = sum(1 for c in a if c.isupper())
    if a_upper_count > m:
        return False

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(m + 1):
            if not dp[i][j]:
                continue

            if j < m and a[i].upper() == b[j]:
                dp[i + 1][j + 1] = True

            if a[i].islower():
                dp[i + 1][j] = True

    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
