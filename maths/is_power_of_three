"""
Check if an integer is a power of three.

Time Complexity: O(log₃ n)
Space Complexity: O(1)
"""

def is_power_of_three(n: int) -> bool:
    """Return True if n is a power of three (n > 0).

    >>> is_power_of_three(1)
    True
    >>> is_power_of_three(3)
    True
    >>> is_power_of_three(9)
    True
    >>> is_power_of_three(27)
    True
    >>> is_power_of_three(2)
    False
    >>> is_power_of_three(0)
    False
    >>> is_power_of_three(-3)
    False
    >>> is_power_of_three(81)
    True
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
