"""
Project Euler problem 145: https://projecteuler.net/problem=145
Author: Vineet Rao, Maxim Smolskiy
Problem statement:

Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313.
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""


def solution(max_power: int = 9) -> int:
    """
    This solution counts reversible numbers below 10^max_power
    using mathematical patterns instead of brute force.

    A reversible number is a number where:
        n + reverse(n)

    contains only odd digits.

    Example:
        36 + 63 = 99
        409 + 904 = 1313

    Instead of checking every number one by one, we observe
    some repeating patterns based on the number of digits.

    --------------------------------------------------------
    Main Observations
    --------------------------------------------------------

    1. Numbers with length = 1 (mod 4)
    ----------------------------------
    These lengths never work because the carry pattern becomes
    inconsistent while adding the number and its reverse.

    Examples:
        1 digit, 5 digits, 9 digits ...

    Count = 0


    2. Even length numbers
    -----------------------
    For numbers with even digits (2, 4, 6, 8 ...):

    - Each pair of digits must produce an odd sum.
    - One digit in the pair must be even and the other odd.
    - The carry pattern stays consistent.

    Counting possibilities:
        - First pair has 20 valid combinations
          (leading digit cannot be zero)

        - Every inner pair has 30 valid combinations

    Formula:
        20 * 30^(k-1)

    where:
        length = 2k

    Examples:
        2 digits  -> 20
        4 digits  -> 600
        6 digits  -> 18000
        8 digits  -> 540000


    3. Length = 3 (mod 4)
    ----------------------
    These are lengths like:
        3, 7, 11 ...

    Here the middle digit creates a special carry cycle,
    which only works for lengths of the form:

        4j + 3

    Formula:
        100 * 500^j

    Examples:
        3 digits -> 100
        7 digits -> 50000


    --------------------------------------------------------
    Complexity
    --------------------------------------------------------

    Time Complexity:
        O(max_power)

    Space Complexity:
        O(1)

    The algorithm is extremely fast because it only loops
    through digit lengths instead of checking every number.
    """
    result = 0
    for length in range(1, max_power + 1):
        if length % 2 == 0:
            # Even length 2k -> 20 x 30^(k-1)
            k = length // 2
            result += 20 * (30 ** (k - 1))
        elif length % 4 == 3:
            # Odd length 4j+3 -> 100 x 500^j
            j = (length - 3) // 4
            result += 100 * (500**j)
        # Lengths == 1 (mod 4) contribute 0 and are intentionally skipped.

    return result


def benchmark() -> None:
    """
    Benchmarks
    """
    from timeit import timeit

    print("Running performance benchmarks...")
    print(f"solution : {timeit('solution()', globals=globals(), number=10_000)}")


if __name__ == "__main__":
    print(f"Solution : {solution()}")
    benchmark()
