"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""
def solution(n):
    """
    This solution is based on the pattern that the successive numbers in the
    series follow: 0+3,+2,+1,+3,+1,+2,+3.
    Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    sum = 0
    num = 0
    while 1:
        num += 3
        if num >= n:
            break
        sum += num
        num += 2
        if num >= n:
            break
        sum += num
        num += 1
        if num >= n:
            break
        sum += num
        num += 3
        if num >= n:
            break
        sum += num
        num += 1
        if num >= n:
            break
        sum += num
        num += 2
        if num >= n:
            break
        sum += num
        num += 3
        if num >= n:
            break
        sum += num
    return sum


if __name__ == "__main__":
    print(solution(int(input().strip())))
