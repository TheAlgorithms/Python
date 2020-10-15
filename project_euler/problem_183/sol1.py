"""
Problem 183: https://projecteuler.net/problem=183
Wikipedia Reference: https://en.wikipedia.org/wiki/Project_Euler

Name: Maximum product of parts

Let N be a positive integer and let N be split into k equal parts, r = N/k, so that
N = r + r + ... + r. Let P be the product of these parts, P = r × r × ... × r = rk.
For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2,
then P = 2.25 = 51.53632. Let M(N) = Pmax for a given value of N. It turns out that
the maximum for N = 11 is found by splitting eleven into four equal parts which leads
to Pmax = (11/4)4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating
decimal. However, for N = 8 the maximum is achieved by splitting it into three equal
parts, so M(8) = 512/27, which is a non-terminating decimal. Let D(N) = N if M(N) is
a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal. For example,
∑ D(N) for 5 ≤ N ≤ 100 is 2438. Find ∑ D(N) for 5 ≤ N ≤ 10000.

"""
Limit = 10000


def solution(n):
    """
    Returns a fixed number.

    >>> print(sum(solution(n) for n in range(5, 10000 + 1)))
    48861552
    """
    rounded_int = round(n / 2.718281828)
    while rounded_int % 2 == 0:
        rounded_int //= 2
    while rounded_int % 5 == 0:
        rounded_int //= 5
    if n % rounded_int:
        return n
    return -n
