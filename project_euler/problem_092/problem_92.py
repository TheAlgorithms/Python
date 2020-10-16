"""
Project Euler Problem 92: https://projecteuler.net/problem=92

A number chain is created by continuously adding the
square of the digits in a number to form a new number
until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will
become stuck in an endless loop. What is most
amazing is that EVERY starting number will
eventually arrive at 1 or 89.

How many starting numbers below ten
million will arrive at 89?
"""


def solution(limit: int = 10_000_000) -> int:
    """
    https://projecteuler.net/problem=92
    >>> solution()
    8581146
    """
    known_solutions = {}
    known_solutions[89] = 1
    known_solutions[1] = 0

    def helper(x: int) -> int:
        """
        Return the sum of the squares of each digit.
        >>> helper(13)
        10
        """
        return sum([int(c) ** 2 for c in list(str(x))])

    def f(x: int) -> int:
        """
        Return 1 if the number chain ends up in 89
        before looping infinitely.
        Return 0 if the number chain ends up in 1
        before looping infinitely.
        Uses memoization.

        >>> f(44)
        0
        >>> f(145)
        1
        """
        if x in known_solutions:
            return known_solutions[x]
        else:
            result = f(helper(x))
            known_solutions[x] = result
            return result

    count = 0

    for i in range(1, 10_000_000):
        if i in known_solutions:
            count += known_solutions[i]
        else:
            count += f(i)
        # if i%100_000==0: print(i)
    return count


if __name__ == "__main__":
    print(solution())
