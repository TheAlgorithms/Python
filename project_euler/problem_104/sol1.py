"""
Project Euler Problem 104 : https://projecteuler.net/problem=104

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number
for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9,
but not necessarily in order). And F2749, which contains 575 digits, is the first
Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND
the last nine digits are 1-9 pandigital, find k.
"""

import sys

sys.set_int_max_str_digits(0)


def is_pandigital_both(number: int) -> bool:
    """
    Checks if the first 9 and last 9 digits of a number are `1-9 pandigital`.

    Returns:
        bool - True if the first 9 and last 9 digits contain all the digits 1 to 9,
              False otherwise

    >>> is_pandigital_both(123456789987654321)
    True

    >>> is_pandigital_both(120000987654321)
    False

    >>> is_pandigital_both(1234567895765677987654321)
    True
    """

    return is_pandigital_end(number) and is_pandigital_start(number)


def is_pandigital_end(number: int) -> bool:
    """
    Checks if the last 9 digits of a number are `1-9 pandigital`.

    Returns:
        bool - True if the last 9 digits contain all the digits 1 to 9, False otherwise

    >>> is_pandigital_end(123456789987654321)
    True

    >>> is_pandigital_end(120000987654321)
    True

    >>> is_pandigital_end(12345678957656779870004321)
    False
    """
    digit_count = [True] + [False] * 9

    # Count the occurrences of each digit[0-9]
    for _ in range(9):
        number, mod = divmod(number, 10)
        if digit_count[mod]:
            return False
        digit_count[mod] = True

    # Return False if any digit is missing
    return all(digit_count[1:])


def is_pandigital_start(number: int) -> bool:
    """
    Checks if the first 9 digits of a number are `1-9 pandigital`.

    Returns:
        bool - True if the first 9 digits contain all the digits 1 to 9, False otherwise

    >>> is_pandigital_start(123456789987654321)
    True

    >>> is_pandigital_start(120000987654321)
    False

    >>> is_pandigital_start(1234567895765677987654321)
    True
    """

    number = int(str(number)[:9])
    return is_pandigital_end(number)


def slow_solution(a: int = 1, b: int = 1, ck: int = 3, max_k: int = 10_00_000) -> int:
    """
    Returns index `k` of the least Fibonacci number `F(k)` that is `1-9 pandigital`
    from both sides. Here `ck <= k < max_k`.

    Parameters:
        a: int - First fibonacci number `F(k)-2`
        b: int - Second fibonacci number `F(k)-1`
        ck: int - Initial index `k` of the Fibonacci number `F(k)`
        max_k: int - Maximum index `k` of the Fibonacci number `F(k)`

    Returns:
        int - index `k` of the least `1-9 pandigital` Fibonacci number `F(k)`

    >>> slow_solution()
    329468
    """

    # Equivalent to 10**9, for getting no higher then 9 digit numbers
    billion = 1_000_000_000

    # Fibonacci numbers
    fk_2 = a  # fk - 2
    fk_1 = b  # fk - 1
    # fk      # fk_1 + fk_2

    # Fibonacci numbers mod billion
    mk_2 = a % billion  # (fk - 2) % billion
    mk_1 = b % billion  # (fk - 1) % billion
    # mk                # (fk    ) % billion

    end_pandigital = [0] * max_k

    # Check fibonacci numbers % 10**9
    for k in range(ck, max_k):
        mk = (mk_2 + mk_1) % billion
        mk_2 = mk_1
        mk_1 = mk

        if is_pandigital_end(mk):
            end_pandigital[k] = 1

    # Check fibonacci numbers
    for k in range(ck, max_k):
        fk = fk_2 + fk_1
        fk_2 = fk_1
        fk_1 = fk

        # perform check only if k is in end_pandigital
        if end_pandigital[k] and is_pandigital_both(fk):
            return k

    # Not found
    return -1


def solution(a: int = 1, b: int = 1, ck: int = 3, max_k: int = 10_00_000) -> int:
    """
    Returns index `k` of the least Fibonacci number `F(k)` that is `1-9 pandigital`
    from both sides. Here `ck <= k < max_k`.

    Parameters:
        a: int - First fibonacci number `F(k)-2`
        b: int - Second fibonacci number `F(k)-1`
        ck: int - Initial index `k` of the Fibonacci number `F(k)`
        max_k: int - Maximum index `k` of the Fibonacci number `F(k)`

    Returns:
        int - index `k` of the least `1-9 pandigital` Fibonacci number `F(k)`

    >>> solution()
    329468
    """

    # Equivalent to 10**9, for getting no higher then 9 digit numbers
    billion = 1_000_000_000

    # For reserving 9 digits (and a few more digits for carry) from the start
    billion_plus = billion * 1_000_000

    # Fibonacci numbers
    fk_2 = a  # fk - 2
    fk_1 = b  # fk - 1
    # fk      # fk_1 + fk_2

    # Fibonacci numbers mod billion
    mk_2 = a % billion  # (fk - 2) % billion
    mk_1 = b % billion  # (fk - 1) % billion
    # mk                # (fk    ) % billion

    end_pandigital = [0] * max_k

    # Check fibonacci numbers % 10**9
    for k in range(ck, max_k):
        mk = (mk_2 + mk_1) % billion
        mk_2 = mk_1
        mk_1 = mk

        if is_pandigital_end(mk):
            end_pandigital[k] = 1

    # Check fibonacci numbers
    for k in range(ck, max_k):
        fk = fk_2 + fk_1
        fk_2 = fk_1
        fk_1 = fk

        # We don't care about the digits after the 9'th one
        # But still we need to keep some digits after after the 9'th
        # Because of carry
        if fk_2 > billion_plus:
            fk_1 //= 10
            fk_2 //= 10

        # perform check only if k is in end_pandigital
        if end_pandigital[k] and is_pandigital_start(fk):
            return k

    # Not found
    return -1


def benchmark() -> None:
    """
    Benchmark
    """
    # Running performance benchmarks...
    # Solution : 8.59146850000252   to  9.774559199999203
    # Slow Sol : 57.75938980000137  to  61.15365279999969

    from timeit import timeit

    print("Running performance benchmarks...")

    print(f"Solution : {timeit('solution()', globals=globals(), number=10)}")
    print(f"Slow Sol : {timeit('slow_solution()', globals=globals(), number=10)}")


if __name__ == "__main__":
    print(f"{solution() = }")
    benchmark()
