"""
Project Euler Problem 137: https://projecteuler.net/problem=137

Fibonacci Golden Nuggets

The polynomial sequence can be rewritten in the finite form:

A_F(x) = x / (1 - x - x^2)

And then the problem is to solve for it for rational x that give A_F(x) as positive
integer. It turns out that the solution is for the n-th golden nugget is given by
F(2n) * F(2n + 1), where F(k) is the k'th Fibonacci number.

Reference: https://oeis.org/A081018

"""


def solution(n: int = 15) -> int:
    """
    It calculates fibonachi numbers 2n and 2n+1, and returns their product.

    >>> solution(3)
    104
    >>> solution(10)
    74049690
    """

    k = 2 * n

    fib1 = fib2 = 1
    for _ in range(k - 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib1 * fib2


if __name__ == "__main__":
    print(f"{solution() = }")
