"""
Simple addition function.
"""


def add_numbers(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    >>> add_numbers(2, 3)
    5
    """
    return a + b


if __name__ == "__main__":
    print(add_numbers(5, 7))
