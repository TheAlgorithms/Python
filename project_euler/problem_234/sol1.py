"""
https://projecteuler.net/problem=234

For an integer n ≥ 4, we define the lower prime square root of n, denoted by
lps(n), as the largest prime ≤ √n and the upper prime square root of n, ups(n),
as the smallest prime ≥ √n.

So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37. Let us
call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n) divides n,
but not both.

The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are 8,
10 and 12. 15 is not semidivisible because it is a multiple of both lps(15) = 3
and ups(15) = 5. As a further example, the sum of the 92 semidivisible numbers
up to 1000 is 34825.

What is the sum of all semidivisible numbers not exceeding 999966663333 ?
"""


def fib(a, b, n):

    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return str(a) + str(b)

    temp = 0
    for x in range(2, n):
        c = str(a) + str(b)
        temp = b
        b = c
        a = temp
    return c


def solution(n):
    """Returns the sum of all semidivisible numbers not exceeding n."""
    semidivisible = []
    for x in range(n):
        l = [i for i in input().split()]
        c2 = 1
        while 1:
            if len(fib(l[0], l[1], c2)) < int(l[2]):
                c2 += 1
            else:
                break
        semidivisible.append(fib(l[0], l[1], c2 + 1)[int(l[2]) - 1])
    return semidivisible


if __name__ == "__main__":
    for i in solution(int(str(input()).strip())):
        print(i)
