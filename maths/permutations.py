"""
Reference: https://en.wikipedia.org/wiki/Permutation
"""

from math import factorial

def permutations(n: int, r: int) -> int:
    """
    Returns the number of different ways of r length which can
    be made from n values where relative order of choice matters 
    and n >= k.

    Examples:
    >>> permutations(10, 5)
    30240
    
    >>> permutations(6, 3)
    120
    
    >>> permutations(20, 1)
    20

    >>> permutations(0, 0)
    1

    >>> permutations(-4, -5)
     ...
    Traceback (most recent call last):
    ValueError: Please enter positive integers for n and k where n >= k
    """

    # If either of the conditions are true, the function is being asked
    # to calculate a factorial of a negative number, which is not possible
    if n < k or k < 0:
        raise ValueError("Please enter positive integers for n and k where n >= k")
    return int(factorial(n) / (factorial(n - k)))

if __name__ == "__main__":
    print(permutations(10, 5))
    print(permutations(6, 3))
    print(permutations(20, 1))
    print(permutations(0, 0))
    print(permutations(-4, -5))
    
