"""
Problem source: https://www.hackerrank.com/challenges/the-power-sum/problem
Find the number of ways that a given integer X, can be expressed as the sum
of the Nth powers of unique, natural numbers. For example, if X=13 and N=2.
We have to find all combinations of unique squares adding up to 13.
The only solution is 2^2+3^2. Constraints: 1<=X<=1000, 2<=N<=10.
"""

from math import pow

sum_ = count_ = 0


def backtrack(needed_sum: int, power: int, current_number: int) -> None:
    """
    DO NOT CALL THIS METHOD DIRECTLY, USE solve() INSTEAD.

    >>> backtrack(13, 2, 1) is None
    True
    >>> backtrack(1000, 10, 2) is None
    True
    """
    global sum_, count_
    i_to_n = int(pow(current_number, power))
    if sum_ == needed_sum:
        # If the sum of the powers is equal to needed_sum, then we have found a solution.
        count_ += 1
        return
    elif sum_ + i_to_n <= needed_sum:
        # If the sum of the powers is less than needed_sum, then we can continue adding powers.
        sum_ += i_to_n
        backtrack(needed_sum, power, current_number + 1)
        sum_ -= i_to_n
    if i_to_n < needed_sum:
        # If the power of i is less than needed_sum, then we can try with the next power.
        backtrack(needed_sum, power, current_number + 1)
    return


def solve(needed_sum: int, power: int) -> int:
    """
    >>> solve(13, 2)
    1
    >>> solve(100, 2)
    3
    >>> solve(100, 3)
    1
    >>> solve(800, 2)
    561
    >>> solve(1000, 10)
    0
    >>> solve(400, 2)
    55
    >>> solve(50, 1)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input, needed_sum must be between 1 and 1000, power between 2 and 10.
    >>> solve(-10, 5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input, needed_sum must be between 1 and 1000, power between 2 and 10.
    """
    if not (1 <= needed_sum <= 1000 and 2 <= power <= 10):
        raise ValueError(
            "Invalid input, needed_sum must be between 1 and 1000, power between 2 and 10."
        )

    global sum_, count_
    sum_, count_ = 0, 0
    backtrack(needed_sum, power, 1)
    return count_


if __name__ == "__main__":
    import doctest

    doctest.testmod()
