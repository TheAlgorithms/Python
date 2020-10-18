"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""


def solution(N: int = 1000) -> int:
    """Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    total = 0
    N=N-1
    r=[3,5,15]
    total=0
    for x in r:
        t=(N//x)+1
        if x==15:
            x=-x
        if t%2!=0:
            total=total+(x*(t*(t//2)))
        else:
            total=total+(x*((t*(t/2-1)+t/2)))
    return int(total)
        


if __name__ == "__main__":
    print(solution(int(input().strip())))
