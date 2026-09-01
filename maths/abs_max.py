"""Find the absolute maximum element in a list."""


def abs_max(arr: list[int]) -> int:
    """
    Find the element with maximum absolute value.

    >>> abs_max([-10, 20, -30, 40])
    -30
    >>> abs_max([1, 2, 3])
    3
    """
    if not arr:
        raise ValueError("List is empty")
    return max(arr, key=abs)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
