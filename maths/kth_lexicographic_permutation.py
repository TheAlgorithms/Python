def kthPermutation(k, n):
    """
    Finds k'th lexicographic permutation (in increasing order) of
    0,1,2,...n-1 in O(n^2) time.

    Examples:
    First permutation is always 0,1,2,...n
    >>> kthPermutation(0,5)
    [0, 1, 2, 3, 4]

    The order of permutation of 0,1,2,3 is [0,1,2,3], [0,1,3,2], [0,2,1,3],
    [0,2,3,1], [0,3,1,2], [0,3,2,1], [1,0,2,3], [1,0,3,2], [1,2,0,3],
    [1,2,3,0], [1,3,0,2]
    >>> kthPermutation(10,4)
    [1, 3, 0, 2]
    """
    # Factorails from 1! to (n-1)!
    factorials = [1]
    for i in range(2, n):
        factorials.append(factorials[-1] * i)
    assert 0 <= k < factorials[-1] * n, "k out of bounds"

    permutation = []
    elements = list(range(n))

    # Find permutation
    while factorials:
        factorial = factorials.pop()
        number, k = divmod(k, factorial)
        permutation.append(elements[number])
        elements.remove(elements[number])
    permutation.append(elements[0])

    return permutation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
