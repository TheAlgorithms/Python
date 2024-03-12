"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""

from collections.abc import Generator


def fibonacci_generator() -> Generator[int, None, None]:
    """
    A generator that produces numbers in the Fibonacci sequence

    >>> generator = fibonacci_generator()
    >>> next(generator)
    1
    >>> next(generator)
    2
    >>> next(generator)
    3
    >>> next(generator)
    5
    >>> next(generator)
    8
    """
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


def solution(n: int = 1000) -> int:
    """Returns the index of the first term in the Fibonacci sequence to contain
    n digits.

    >>> solution(1000)
    4782
    >>> solution(100)
    476
    >>> solution(50)
    237
    >>> solution(3)
    12
    """
    answer = 1
    gen = fibonacci_generator()
    while len(str(next(gen))) < n:
        answer += 1
    return answer + 1


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
