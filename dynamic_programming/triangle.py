from __future__ import annotations


def minimum_total(triangle: list[list[int]]) -> int:
    """
    Return the minimum path sum from top to bottom of a triangle.

    Each step you may move to adjacent numbers on the row below.
    The input must be a proper triangle: len(row i) == i + 1.

    >>> minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]])
    11
    >>> minimum_total([[-10]])
    -10
    >>> minimum_total([[1],[2,3]])
    3
    >>> minimum_total([])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: triangle must be non-empty and well-formed
    >>> minimum_total([[1],[2]])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: triangle must be non-empty and well-formed
    """
    # Basic validation: non-empty and proper "triangle" shape
    if not triangle or any(len(row) != i + 1 for i, row in enumerate(triangle)):
        raise ValueError("triangle must be non-empty and well-formed")

    # Start from the last row and fold upwards. dp[j] stores the minimum path
    # sum from row r to the bottom starting at column j.
    dp = triangle[-1][:]  # copy so we don't mutate the input

    for r in range(len(triangle) - 2, -1, -1):
        for c in range(r + 1):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])

    return dp[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
