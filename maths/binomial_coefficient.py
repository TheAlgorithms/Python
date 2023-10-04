def binomial_coefficient(n: int, r: int) -> int:
    """
    Find binomial coefficient using pascals triangle.

    >>> binomial_coefficient(10, 5)
    252
    """
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


print(binomial_coefficient(n=10, r=5))
