def kth_permutation(k, n):
    """
    Finds k'th lexicographic permutation (in increasing order) of
    0,1,2,...,n-1 in O(n^2) time.

    Examples:
    First permutation is always 0,1,2,...,n-1
    >>> kth_permutation(0,5)
    [0, 1, 2, 3, 4]

    The order of permutation of 0,1,2,3 is [0,1,2,3], [0,1,3,2], [0,2,1,3],
    [0,2,3,1], [0,3,1,2], [0,3,2,1], [1,0,2,3], [1,0,3,2], [1,2,0,3],
    [1,2,3,0], [1,3,0,2]
    >>> kth_permutation(10,4)
    [1, 3, 0, 2]
    """
    # Factorials from 1! to (n-1)!
    if not isinstance(k, int) or not isinstance(n, int):
        raise TypeError("k and n must be integers")

    if n < 1:
        raise ValueError("n must be a positive integer")

    factorials = [1]
    for i in range(2, n):
        factorials.append(factorials[-1] * i)

    max_k = factorials[-1] * n  # equals n!
    if not (0 <= k < max_k):
        raise ValueError("k out of bounds")

    permutation = []
    elements = list(range(n))

    # Find permutation
    while factorials:
        factorial = factorials.pop()
        index, k = divmod(k, factorial)
        permutation.append(elements[index])
        elements.pop(index)

    permutation.append(elements[0])
    return permutation



if __name__ == "__main__":
    import doctest

    doctest.testmod()
