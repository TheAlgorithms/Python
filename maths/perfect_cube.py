def perfect_cube(n: int) -> bool:
    """
    Check if a number is a perfect cube or not.

    The float cube root is rounded to the nearest integer, which is then cubed and
    compared with the number. Cubing the float itself is not exact: ``64 ** (1 / 3)``
    is ``3.9999999999999996``.

    >>> perfect_cube(27)
    True
    >>> perfect_cube(64)
    True
    >>> perfect_cube(4)
    False
    >>> perfect_cube(0)
    True
    >>> perfect_cube(-27)
    True
    >>> perfect_cube(-64)
    True
    >>> perfect_cube(-24)
    False
    >>> all(perfect_cube(i**3) for i in range(-100, 101))
    True
    >>> perfect_cube(10**18)
    True
    >>> perfect_cube(10**18 + 1)
    False
    """
    n = abs(n)
    return round(n ** (1 / 3)) ** 3 == n


def perfect_cube_binary_search(n: int) -> bool:
    """
    Check if a number is a perfect cube or not using binary search.
    Time complexity : O(Log(n))
    Space complexity: O(1)

    >>> perfect_cube_binary_search(27)
    True
    >>> perfect_cube_binary_search(64)
    True
    >>> perfect_cube_binary_search(4)
    False
    >>> perfect_cube_binary_search("a")
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    >>> perfect_cube_binary_search(0.1)
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    """
    if not isinstance(n, int):
        raise TypeError("perfect_cube_binary_search() only accepts integers")
    if n < 0:
        n = -n
    left = 0
    right = n
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid * mid == n:
            return True
        elif mid * mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
