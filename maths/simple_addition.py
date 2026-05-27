"""
Simple addition function.
https://en.wikipedia.org/wiki/Addition
"""


def add_numbers(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-1, 1)
    0
    """
    return a + b


if __name__ == "__main__":
    print(add_numbers(5, 7))
