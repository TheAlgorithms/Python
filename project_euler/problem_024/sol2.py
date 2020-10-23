"""A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
from itertools import permutations


def solution():
    """
    >>> solution()
    '2783915460'
    """
    lexi_perm = "".join(list(permutations("0123456789"))[999999])
    return lexi_perm


if __name__ == "__main__":
    print(solution())


