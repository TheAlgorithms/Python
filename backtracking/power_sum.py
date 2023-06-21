"""
Problem source: https://www.hackerrank.com/challenges/the-power-sum/problem
Find the number of ways that a given integer X, can be expressed as the sum
of the Nth powers of unique, natural numbers. For example, if X=13 and N=2.
We have to find all combinations of unique squares adding up to 13.
The only solution is 2^2+3^2.
"""

from math import pow

sum_ = 0
count_ = 0


def backtrack(x: int, n: int, i: int) -> None:
    """
    Backtracking function to find all the possible combinations
    of powers of natural numbers that add up to x.
    Parameters:
        x: The number to be expressed as the sum of
        the nth powers of unique, natural numbers.
        n: The power of the natural numbers.
        i: The current natural number.

    Returns:
        None

    >>> backtrack(13, 2, 1)

    """
    global sum_, count_
    i_to_n = int(pow(i, n))
    if sum_ == x:
        # If the sum of the powers is equal to x, then we have found a solution.
        global count_
        count_ += 1
        return
    elif sum_ + i_to_n <= x:
        # If the sum of the powers is less than x, then we can continue adding powers.
        sum_ += i_to_n
        backtrack(x, n, i + 1)
        sum_ -= i_to_n
    if i_to_n < x:
        # If the power of i is less than x, then we can try with the next power.
        backtrack(x, n, i + 1)
    return


def solve(x: int, n: int) -> int:
    """
    Calculates the number of ways that x can be expressed as the sum of
    the nth powers of unique, natural numbers.
    Parameters:
        x: The number to be expressed as the sum of
        the nth powers of unique, natural numbers.
        n: The power of the natural numbers.

    Returns:
        The number of ways that x can be expressed as the sum of
        the nth powers of unique, natural numbers.

    >>> solve(13, 2)
    1
    """
    global sum_, count_
    sum_, count_ = 0, 0
    backtrack(x, n, 1)
    return count_


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # x = 100
    # n = 3
    # output = f"The number of ways that {x} can be expressed as the sum of"
    # output += f" the {n}th powers of unique, natural numbers is {solve(x, n)}"
    # print(output)
    # Output: The number of ways that 100 can be expressed as the
    # sum of the 3th powers of unique, natural numbers is 1
