"""
This program calculates the nth Fibonacci number in O(log(n)).
It's possible to calculate F(1000000) in less than a second.
"""
from __future__ import print_function
import sys


# returns F(n)
def fibonacci(n: int):
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _fib(n)[0]


# returns (F(n), F(n-1))
def _fib(n: int):
    if n == 0:
        # (F(0), F(1))
        return (0, 1)
    else:
        # F(2n) = F(n)[2F(n+1) − F(n)]
        # F(2n+1) = F(n+1)^2+F(n)^2
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Too few or too much parameters given.")
        exit(1)
    try:
        n = int(args[0])
    except ValueError:
        print("Could not convert data to an integer.")
        exit(1)
    print("F(%d) = %d" % (n, fibonacci(n)))
