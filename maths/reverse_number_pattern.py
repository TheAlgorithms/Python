"""
Reverse number pattern.

Example:
>>> reverse_number_pattern(4)
['1234', '123', '12', '1']
"""

from typing import List


def reverse_number_pattern(n: int) -> List[str]:
    """
    Returns a reverse number pattern.

    >>> reverse_number_pattern(3)
    ['123', '12', '1']
    >>> reverse_number_pattern(1)
    ['1']
    >>> reverse_number_pattern(0)
    []
    """
    if n <= 0:
        return []

    result = []
    for i in range(n, 0, -1):
        line = ""
        for x in range(1, i + 1):
            line += str(x)
        result.append(line)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
