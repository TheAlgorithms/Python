#nCr = n! / (n - r)! https://en.wikipedia.org/wiki/Permutation
from math import factorial

#Calculate nPr (permutations)
def permutations(n, r):
     """
    >>> permutations(15,2)
    210
    >>> permutations(5,3)
    60
    >>> permutations(25,8)
    43609104000
    """
    return int(factorial(n) / (factorial(n - k)))

if __name__ == "__main__":
    from doctest import testmod

    testmod()
