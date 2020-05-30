"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""

def solution(n: int) -> int:
    """Returns the sum of all the multiples of 3 or 5 below n.
    What unique about this solution?
    Although this solution is slower than previous solutions,
    but it is more elegant and clear.
    It uses Python features to do some logic,
    like using range's step to check for only multiples of 3 and 5
    and use set's union to remove duplication

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """
    return sum(set(range(0, n, 3)).union(set(range(0, n, 5))))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(solution(int(input().strip())))
