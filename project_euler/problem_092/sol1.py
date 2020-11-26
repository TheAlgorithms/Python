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
    """

    squared = {1: 1, 89: 89}
    eighty_nine_count = 0
    for i in range(1, limit):
        chain = [i]
        while True:
            if i in squared:
                if squared[i] == 89:
                    squared.update(dict.fromkeys(chain, 89))
                    eighty_nine_count += 1
                else:
                    squared.update(dict.fromkeys(chain, 1))
                break
            else:
                sum_squares = sum([int(d) ** 2 for d in str(i)])
                chain.append(sum_squares)
                i = sum_squares

    return eighty_nine_count


if __name__ == "__main__":
    print(f"{solution() = }")
