"""
Recursive Double Linear Search Algorithm

Searches for a target element in a list 
by recursively checking both ends simultaneously.
"""


def double_linear_search_recursion(
    sequence: list[int], target: int, start: int = 0, end: int | None = None
) -> int:
    """
    Recursively searches for target in sequence from both ends.

    Time Complexity: O(n)
    Space Complexity: O(n) due to recursive call stack

    :param sequence: A list of integers.
    :param target: The integer value to search for.
    :param start: Starting index for search window.
    :param end: Ending index for search window.
    :return: Index of target if found, else -1.

    >>> double_linear_search_recursion([1, 2, 3, 4, 5], 1)
    0
    >>> double_linear_search_recursion([1, 2, 3, 4, 5], 5)
    4
    >>> double_linear_search_recursion([1, 2, 3, 4, 5], 3)
    2
    >>> double_linear_search_recursion([1, 2, 3, 4, 5], 6)
    -1
    >>> double_linear_search_recursion([], 3)
    -1
    """
    if end is None:
        end = len(sequence) - 1

    if start > end:
        return -1

    if sequence[start] == target:
        return start
    if sequence[end] == target:
        return end

    return double_linear_search_recursion(sequence, target, start + 1, end - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
