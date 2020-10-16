def binomialCoeff(n, k):
    res = 1

    """
    Since C(n, k) = C(n, n-k)

    >>> binomialCoeff(4,2)
    2
    >>> binomialCoeff(8,4)
    6
    """
    if k > n - k:
        k = n - k
    """
    Calculate value of [n*(n-1)*---
    (n-k+1)] / [k*(k-1)*---*1]
    """
    for i in range(k):
        res *= n - i
        res /= i + 1

    return int(res)


"""

A Binomial coefficient based function to find nth catalan number in O(n) time

"""


def catalan(n):

    """Calculate value of 2nCn """
    """
    >>> catalan(1)
    1
    >>> catalan(2)
    2
    """
    c = binomialCoeff(2 * n, n)

    """ return 2nCn/(n+1) """

    return int(c / (n + 1))


def number_validparanthesis(n):

    """
    Function to find possible ways to put balanced
    parenthesis in an expression of length n

    If n is odd, not possible to create any valid parentheses

    >>> number_validparanthesis(2)
    1
    >>> number_validparanthesis(4)
    2
    >>> number_validparanthesis(10)
    42

    """
    if n & 1:
        return 0

    """Otherwise return n/2'th Catalan Number """
    return catalan(int(n / 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n = int(input("Enter number = "))
    print(f"number of valid expression is {number_validparanthesis(n)}")
