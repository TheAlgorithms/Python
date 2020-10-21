"""
Project Euler Problem 92:https://projecteuler.net/problem=92

A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen before.

For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will
become stuck in an endless loop.
What is most amazing is that EVERY starting number
will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

For a n digit number abc..p(n digits) if it arrive at 89
then any permutation of digits like bad..p will also arrive at 89
and same in the case if it does not.
So if I check for a single permutation whether it arrives or not.
If does arrive then I will increment the count by the no of
all its permutations ((A+B+C+...)!/(A!*B!*C!*...)
where A is the no. of a's and B is the no. of b's and so on.
For n=7 7-digit no. we can use beggars method to calculate the
no. of cases we have to check which is 1C(16,9) which equals to 11440
cases which is significatly less than checking 10 million numbers.
Also for a n digit no. maximum sum of squares its digits can be 81*n.
So if we will store the result of first n*100 no.'s we can use it
every time.

"""


def squared_sum_of_digits(d: int) -> int:
    """
    returns the sum of square of digits of d
    >>> squared_sum_of_digits(1)
    1
    >>> squared_sum_of_digits(77)
    98
    >>> squared_sum_of_digits(11067)
    87
    """
    sum = 0
    while d:
        sum += (d % 10) * (d % 10)
        d //= 10

    return sum


def arrived_at_89(d: int) -> bool:
    """
    returns whether d will arrive at 89 or not
    >>> arrived_at_89(10)
    False
    >>> arrived_at_89(19872)
    True
    >>> arrived_at_89(55555)
    True

    """
    if d == 0:
        return False

    while d != 89 and d != 1:
        d = squared_sum_of_digits(d)

    if d == 89:
        return True
    else:
        return False


def all_possible_distributions(
    all_distributions: list, each_distribution: list, curr: int, i: int
) -> None:
    """
    Appends the list of all the possible ways in which an n digts can
    be distributed among 9 digits at the end of a 2-d list all_distributions.
    """

    if i == 9:
        each_distribution[i] = curr
        all_distributions.append(each_distribution.copy())
        return
    else:
        for j in range(0, curr + 1):
            each_distribution[i] = j
            all_possible_distributions(
                all_distributions, each_distribution, curr - j, i + 1
            )
            each_distribution[i] = 0


def solution(n: int = 7) -> int:
    """
    returns all the n digit numbers that arrive at 89
    >>> solution(6)
    856929
    >>> solution(1)
    7
    >>> solution(10)
    8507390852
    """

    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = i * factorial[i - 1]
    all_distributions = []
    each_distribution = [0] * 10
    all_possible_distributions(all_distributions, each_distribution, n, 0)
    count = 0
    arrived_89_list = [False] * n * 100
    for i in range(1, n * 100):
        arrived_89_list[i] = arrived_at_89(i)

    for each_distribution in all_distributions:
        d = 0
        for i in range(0, 10):
            d += (i * i) * each_distribution[i]

        if arrived_89_list[d]:
            total = 1
            for j in each_distribution:
                total *= factorial[j]
            count += factorial[n] // total

    return count


if __name__ == "__main__":
    print(f"{solution() = }")
