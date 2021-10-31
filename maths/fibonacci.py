# fibonacci.py
"""
Calculates the Fibonacci sequence using iteration and a simplified form of
Binet's formula

NOTE 1: the iterative function is more accurate than the Binet's formula
function because the iterative function doesn't use floats

NOTE 2: the Binet's formula function is much more limited in the size of inputs
that it can handle due to the size limitations of Python floats
"""

import functools
import time
from math import sqrt


def timer_decorator(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        if int(end - start) > 0:
            print(f"{func.__name__} runtime: {(end - start):0.4f} s")
        else:
            print(f"{func.__name__} runtime: {(end - start) * 1000:0.4f} ms")
        return func(*args, **kwargs)

    return timer_wrapper


@timer_decorator
def fib_iterative(n: int) -> list[int]:
    """
    Calculates the first n (0-indexed) Fibonacci numbers using iteration
    """
    if n < 0:
        raise Exception("n is negative")
    if n == 0:
        return [0]
    fib = [0, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return fib


@timer_decorator
def fib_binet(n: int) -> list[int]:
    """
    Calculates the first n (0-indexed) Fibonacci numbers using a simplified form
    of Binet's formula:
    https://en.m.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding

    NOTE 1: this function diverges from fib_iterative at around n = 71, likely
    due to compounding floating-point arithmetic errors

    NOTE 2: this function doesn't accept n >= 1475 because it overflows
    thereafter due to the size limitations of Python floats
    """
    if n < 0:
        raise Exception("n is negative")
    if n >= 1475:
        raise Exception("n is too large")
    sqrt_5 = sqrt(5)
    phi = (1 + sqrt_5) / 2
    return [round(phi ** i / sqrt_5) for i in range(n + 1)]


if __name__ == "__main__":
    num = 50
    fib_iterative(num)
    fib_binet(num)
