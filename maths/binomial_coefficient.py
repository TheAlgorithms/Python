def binomial_coefficient(n: int, r: int) -> int:
    """
    Find binomial coefficient using Pascal's triangle.

    Calculate C(n, r) using Pascal's triangle.

    :param n: The total number of items.
    :param r: The number of items to choose.
    :return: The binomial coefficient C(n, r).

    >>> binomial_coefficient(10, 5)
    252
    >>> binomial_coefficient(10, 0)
    1
    >>> binomial_coefficient(0, 10)
    1
    >>> binomial_coefficient(10, 10)
    1
    >>> binomial_coefficient(5, 2)
    10
    >>> binomial_coefficient(5, 6)
    0
    >>> binomial_coefficient(3, 5)
    0
    >>> binomial_coefficient(-2, 3)
    Traceback (most recent call last):
        ...
    ValueError: n and r must be non-negative integers
    >>> binomial_coefficient(5, -1)
    Traceback (most recent call last):
        ...
    ValueError: n and r must be non-negative integers
    >>> binomial_coefficient(10.1, 5)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binomial_coefficient(10, 5.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer

    # Additional edge cases
    >>> binomial_coefficient(0, 0)
    1
    >>> binomial_coefficient(1, 0)
    1
    >>> binomial_coefficient(1, 1)
    1
    >>> binomial_coefficient(2, 1)
    2
    >>> binomial_coefficient(3, 0)
    1
    >>> binomial_coefficient(3, 1)
    3
    >>> binomial_coefficient(3, 2)
    3
    >>> binomial_coefficient(3, 3)
    1
    >>> binomial_coefficient(4, 2)
    6

    # Test symmetry property: C(n,r) = C(n, n-r)
    >>> binomial_coefficient(8, 3) == binomial_coefficient(8, 5)
    True
    >>> binomial_coefficient(7, 2) == binomial_coefficient(7, 5)
    True
    >>> binomial_coefficient(6, 1) == binomial_coefficient(6, 5)
    True

    # Test larger numbers
    >>> binomial_coefficient(15, 3)
    455
    >>> binomial_coefficient(12, 4)
    495
    >>> binomial_coefficient(20, 2)
    190
    >>> binomial_coefficient(13, 6)
    1716

    # Test cases where r > n (should return 0)
    >>> binomial_coefficient(1, 2)
    0
    >>> binomial_coefficient(2, 5)
    0
    >>> binomial_coefficient(4, 7)
    0

    # Test Pascal's triangle identity: C(n,r) = C(n-1,r-1) + C(n-1,r)
    >>> (binomial_coefficient(5, 2) ==
    ...  binomial_coefficient(4, 1) + binomial_coefficient(4, 2))
    True
    >>> (binomial_coefficient(6, 3) ==
    ...  binomial_coefficient(5, 2) + binomial_coefficient(5, 3))
    True
    >>> (binomial_coefficient(7, 4) ==
    ...  binomial_coefficient(6, 3) + binomial_coefficient(6, 4))
    True

    # Test performance with larger numbers
    >>> binomial_coefficient(100, 2)
    4950
    >>> binomial_coefficient(50, 1)
    50
    >>> binomial_coefficient(25, 0)
    1
    >>> binomial_coefficient(30, 30)
    1

    # Test boundary conditions more thoroughly
    >>> all(binomial_coefficient(n, 0) == 1 for n in range(10))
    True
    >>> all(binomial_coefficient(n, n) == 1 for n in range(10))
    True
    >>> all(binomial_coefficient(n, 1) == n for n in range(1, 10))
    True

    # Test some well-known binomial coefficients
    >>> binomial_coefficient(4, 2)  # 4 choose 2
    6
    >>> binomial_coefficient(5, 3)  # 5 choose 3
    10
    >>> binomial_coefficient(6, 2)  # 6 choose 2
    15
    >>> binomial_coefficient(8, 4)  # 8 choose 4
    70
    >>> binomial_coefficient(9, 3)  # 9 choose 3
    84

    # Additional negative number tests
    >>> binomial_coefficient(-1, 0)
    Traceback (most recent call last):
        ...
    ValueError: n and r must be non-negative integers
    >>> binomial_coefficient(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: n and r must be non-negative integers
    >>> binomial_coefficient(-5, -3)
    Traceback (most recent call last):
        ...
    ValueError: n and r must be non-negative integers
    """
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative integers")
    if 0 in (n, r):
        return 1
    c = [0 for i in range(r + 1)]
    # nc0 = 1
    c[0] = 1
    for i in range(1, n + 1):
        # to compute current row from previous row.
        j = min(i, r)
        while j > 0:
            c[j] += c[j - 1]
            j -= 1
    return c[r]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(binomial_coefficient(n=10, r=5))
