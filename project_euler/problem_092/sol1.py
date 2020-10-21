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

from typing import List


def squared_sum_of_digits(num: int) -> int:
    """
    returns the sum of square of digits of num
    >>> squared_sum_of_digits(1)
    1
    >>> squared_sum_of_digits(77)
    98
    >>> squared_sum_of_digits(11067)
    87
    """
    total = 0
    while num:
        total += (num % 10) * (num % 10)
        num //= 10

    return total


def arrived_at_89(num: int) -> bool:
    """
    returns whether num will arrive at 89 or not
    >>> arrived_at_89(10)
    False
    >>> arrived_at_89(19872)
    True
    >>> arrived_at_89(55555)
    True

    """
    if num == 0:
        return False

    while num != 89 and num != 1:
        num = squared_sum_of_digits(num)

    return num == 89


def all_possible_distributions(
    all_distributions: List[List[int]],
    each_distribution: List[int],
    current: int,
    index: int,
) -> None:
    """
    Appends the List of all the possible ways in which current can
    be distributed among 9 digits at the end of a 2-d List all_distributions.
    >>> all_possible_distributions([],[0]*10,5,0) is None
    True
    >>> all_possible_distributions([],[0]*10,8,0) is None
    True

    """

    if index == 9:
        each_distribution[index] = current
        all_distributions.append(each_distribution.copy())
        return
    else:
        for j in range(0, current + 1):
            each_distribution[index] = j
            all_possible_distributions(
                all_distributions, each_distribution, current - j, index + 1
            )
            each_distribution[index] = 0


def solution(number_of_digits: int = 7) -> int:
    """
    returns all the number_of_digits digit numbers that arrive at 89
    >>> solution(6)
    856929
    >>> solution(1)
    7
    >>> solution(10)
    8507390852
    """

    factorial = [1] * (number_of_digits + 1)
    for i in range(1, number_of_digits + 1):
        factorial[i] = i * factorial[i - 1]
    all_distributions = []
    each_distribution = [0] * 10
    all_possible_distributions(
        all_distributions, each_distribution, number_of_digits, 0
    )
    count = 0
    arrived_89_list = [False] * number_of_digits * 100
    for i in range(1, number_of_digits * 100):
        arrived_89_list[i] = arrived_at_89(i)

    for each_distribution in all_distributions:
        d = 0
        for i in range(0, 10):
            d += (i * i) * each_distribution[i]

        if arrived_89_list[d]:
            total = 1
            for j in each_distribution:
                total *= factorial[j]
            count += factorial[number_of_digits] // total

    return count


if __name__ == "__main__":
    print(f"{solution() = }")
