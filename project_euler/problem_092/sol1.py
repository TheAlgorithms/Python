"""
Project Euler Problem 92: https://projecteuler.net/problem=92

Name: Square digit chains

A number chain is created by continuously adding the square of the digits in a number to
form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""


def add_square_digits(number: int) -> int:
    """
    Returns the sum of the squared digits of a given number, and recursively adds the
    squares until the new number reaches 89 or 1.

    >>> add_square_digits(3)
    89
    >>> add_square_digits(44)
    1
    >>> add_square_digits(145)
    89
    >>> add_square_digits(23839)
    1
    """
    squares = [int(d) ** 2 for d in str(number)]
    sum_squares = sum(squares)
    if sum_squares != 89 and sum_squares != 1:
        sum_squares = add_square_digits(sum_squares)
    return sum_squares


def solution(limit: int = 10000000) -> int:
    """
    Returns the number of starting numbers, up to a given limit, whose number chain
    arrives at 89.

    A number chain is created by continuously adding the square of the digits in a
    number to form a new number until it has been seen before.

    >>> solution(10)
    7
    >>> solution(350)
    295
    >>> solution(22222)
    18803
    >>> solution(10000000)
    8581146
    """
    eighty_nine_count = 0
    for i in range(1, limit):
        squared = add_square_digits(i)
        if squared == 89:
            eighty_nine_count += 1

    return eighty_nine_count


if __name__ == "__main__":
    print(f"{solution() = }")
