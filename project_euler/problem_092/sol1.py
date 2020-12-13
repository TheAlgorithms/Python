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


def sum_square_digits(number: int) -> int:
    """
    Returns the sum of squared digits given an integer.

    Base-10 allows us to obtain the last digit in order to calculate its square:
    1234 % 10 = 4

    We then use floor division to obtain 123 from 1234:
    1234 // 10 = 123

    We continue to do this until we have calulated the sum of squares for each digit.

    This function is more performant than sum(int(d)**2 for d in str(i)) because we
    avoid having to convert an integer to a string, and then back to an integer again.

    >>> sum_square_digits(1234)
    30
    >>> sum_square_digits(1000)
    1
    >>> sum_square_digits(22222)
    20
    """
    sum_squares = 0
    while number:
        sum_squares += (number % 10) ** 2
        number //= 10
    return sum_squares


def count_eighty_nine_from_chain(limit: int, squared: dict) -> int:
    """
    Returns the number of starting numbers, up to a given limit, whose number chain
    arrives at 89.

    >>> count_eighty_nine_from_chain(10, {1: 1, 89: 89})
    7
    >>> count_eighty_nine_from_chain(350, {1: 1, 89: 89})
    295
    >>> count_eighty_nine_from_chain(22222, {1: 1, 89: 89})
    18803
    """
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
                sum_squares = sum_square_digits(i)
                chain.append(sum_squares)
                i = sum_squares
    return eighty_nine_count


def solution(limit: int = 10000000) -> int:
    """
    Returns the number of starting numbers, up to a given limit, whose number chain
    arrives at 89.
    A number chain is created by continuously adding the square of the digits in a
    number to form a new number until it has been seen before.

    This solution calulates the largest possible sum of squares and stores every number
    in that range in a dictionary. The key is the number in the range, and the value is
    either 89 or 1 depending on which number the chain arrives at.

    For all numbers above that range, we can simply calculate the sum of squares which
    we know will fall within that range, and determine whether it will eventually end
    up at 89 or 1.

    For example, the largest possible sum of squares for 10,000,000 would be for
    9,999,999 and equals 567. We therefore know that all numbers will sum up between
    the range of 1 and 567, so we do not need to calculate any chains above this limit.

    >>> solution(10)
    7
    >>> solution(350)
    295
    >>> solution(22222)
    18803
    """
    squared = {1: 1, 89: 89}
    sum_squared_limit = ((9 ** 2) * len(str(limit - 1))) + 1
    if limit > sum_squared_limit:
        eighty_nine_count = count_eighty_nine_from_chain(sum_squared_limit, squared)
        for i in range(sum_squared_limit, limit):
            if squared[sum_square_digits(i)] == 89:
                eighty_nine_count += 1
    else:
        eighty_nine_count = count_eighty_nine_from_chain(limit, squared)

    return eighty_nine_count


if __name__ == "__main__":
    print(f"{solution() = }")
