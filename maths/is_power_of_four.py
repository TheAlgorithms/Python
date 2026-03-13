"""
Check if an integer is a power of four.

Time Complexity: O(log₄ n)
Space Complexity: O(1)
"""


def is_power_of_four(n: int) -> bool:
    """Return True if n is a power of four (n > 0).

    >>> is_power_of_four(1)
    True
    >>> is_power_of_four(4)
    True
    >>> is_power_of_four(16)
    True
    >>> is_power_of_four(64)
    True
    >>> is_power_of_four(8)
    False
    >>> is_power_of_four(0)
    False
    >>> is_power_of_four(-4)
    False
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
