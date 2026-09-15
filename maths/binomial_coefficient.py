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
