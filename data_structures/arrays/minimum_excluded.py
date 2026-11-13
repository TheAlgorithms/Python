"""Find the minimum excluded non-negative integer (MEX) of a list.

Reference: https://cp-algorithms.com/sequences/mex.html
"""


def minimum_excluded(numbers: list[int]) -> int:
    """Return the smallest non-negative integer absent from numbers.

    Negative integers and duplicates are allowed. The input is not modified.
    Non-integer elements raise TypeError.

    For n elements, the answer is in [0, n]: n elements cannot contain all
    n + 1 distinct integers in that range. Marking their presence therefore
    takes O(n) time and O(n) extra space, regardless of the largest value.

    >>> minimum_excluded([])
    0
    >>> minimum_excluded([0])
    1
    >>> minimum_excluded([1, 2, 3])
    0
    >>> minimum_excluded([0, 1, 3])
    2
    >>> minimum_excluded([3, 0, 2, 1])
    4
    >>> minimum_excluded([0, 0, 1, 1])
    2
    >>> minimum_excluded([-3, -1, 0, 2])
    1
    >>> minimum_excluded([-2, -1])
    0
    >>> minimum_excluded([0, 1, 10**100])
    2
    >>> values = [2, 0, 1]
    >>> minimum_excluded(values)
    3
    >>> values
    [2, 0, 1]
    >>> minimum_excluded([0, 1.5])
    Traceback (most recent call last):
        ...
    TypeError: numbers must contain only integers
    >>> minimum_excluded([0, "1"])
    Traceback (most recent call last):
        ...
    TypeError: numbers must contain only integers
    """
    size = len(numbers)
    present = [False] * (size + 1)
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("numbers must contain only integers")
        if 0 <= number <= size:
            present[number] = True

    missing = 0
    while present[missing]:
        missing += 1
    return missing


if __name__ == "__main__":
    import doctest

    doctest.testmod()
