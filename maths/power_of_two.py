"""
Check if an integer is a power of two.

Time Complexity: O(1)
Space Complexity: O(1)
"""


def is_power_of_two(n: int) -> bool:
    """Return True if n is a power of two (n > 0).

    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(3)
    False
    >>> is_power_of_two(0)
    False
    >>> is_power_of_two(-4)
    False
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
