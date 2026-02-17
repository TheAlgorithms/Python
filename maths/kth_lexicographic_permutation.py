def kth_permutation(k: int, n: int) -> list[int]:
    """
    Finds k'th lexicographic permutation (in increasing order) of
    0,1,2,...n-1 in O(n^2) time.

    :param k: The index of the permutation (0-based)
    :param n: The number of elements in the permutation
    :return: The k-th lexicographic permutation of size n

    Examples:
    First permutation is always 0,1,2,...n-1
    >>> kth_permutation(0, 5)
    [0, 1, 2, 3, 4]

    The order of permutation of 0,1,2,3 is [0,1,2,3], [0,1,3,2], [0,2,1,3],
    [0,2,3,1], [0,3,1,2], [0,3,2,1], [1,0,2,3], [1,0,3,2], [1,2,0,3],
    [1,2,3,0], [1,3,0,2]
    >>> kth_permutation(10, 4)
    [1, 3, 0, 2]

    >>> kth_permutation(10, 0)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive

    >>> kth_permutation(-1, 5)
    Traceback (most recent call last):
        ...
    IndexError: k must be non-negative

    >>> kth_permutation(120, 5)
    Traceback (most recent call last):
        ...
    IndexError: k out of bounds
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if k < 0:
        raise IndexError("k must be non-negative")

    # Factorials from 1! to (n-1)!
    factorials = [1]
    for i in range(2, n):
        factorials.append(factorials[-1] * i)

    if k >= factorials[-1] * n:
        raise IndexError("k out of bounds")

    permutation = []
    elements = list(range(n))

    # Find permutation
    while factorials:
        factorial = factorials.pop()
        number, k = divmod(k, factorial)
        permutation.append(elements[number])
        elements.pop(number)  # elements.remove(elements[number]) is slower and redundant
    permutation.append(elements[0])

    return permutation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
