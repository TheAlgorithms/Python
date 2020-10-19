def binomial_coefficient(n, r):
    """
    Find binomial coefficient using pascals triangle.

    >>> binomial_coefficient(10, 5)
    252
    """
    C = [0 for i in range(r + 1)]
    # nc0 = 1
    C[0] = 1
    for i in range(1, n + 1):
        # to compute current row from previous row.
        j = min(i, r)
        while j > 0:
            C[j] += C[j - 1]
            j -= 1
    return C[r]

print(binomial_coefficient(n=10, r=5))

  
def binomial_coefficient_faster(n, r):
    """
    A faster way to calculate binomial coefficients 

    >>> binomian_coeffieient_faster(10,5)
    252
    """
    if 0 <= r <= n:
        #initializing two variables as 1
        ntok = 1
        rtok = 1
        #we use the formula nCr = n!/(n-r)!r!
        for t in range(1, min(r, n - r) + 1):
            ntok *= n
            rtok *= t
            n -= 1
        return ntok // rtok
    else:
        return 0

print(binomial_coefficient_faster(n=10, r=5))
