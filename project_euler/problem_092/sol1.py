"""
Project Euler Problem 092: https://projecteuler.net/problem=92
Square digit chains
A number chain is created by continuously adding the square of the digits in
a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?

References:
    - https://en.wikipedia.org/wiki/Digital_root
    - https://en.wikipedia.org/wiki/Digit_DP
"""


def solution(number: int = 10_000_000) -> int:
    """
    Returns how many starting numbers below `number` will arrive at 89
    in the digit-square chain.

    Uses digit DP so the count is computed in O(k * d_max * 10) time —
    roughly 40 000 operations for number = 10^7 — instead of iterating
    all `number` values explicitly.

    Key observations:
    1. For any n < number, digit_square_sum(n) ≤ num_digits * 81,
       so chain endpoints can be precomputed for that small range only.
    2. A digit DP over the decimal digits of (number - 1) counts how many
       integers in [0, number-1] have each possible digit-square sum,
       grouping by whether the prefix is still bounded ("tight") or free.
       Integers whose digit-square sum equals 0 are exactly 0 itself.

    >>> solution(100)
    80

    >>> solution(10_000_000)
    8581146
    """
    num_digits = len(str(number - 1)) if number > 1 else 1
    limit = num_digits * 81 + 1  # max possible digit-square sum + 1

    def digit_square_sum(n: int) -> int:
        total = 0
        while n:
            total += (n % 10) ** 2
            n //= 10
        return total

    # Precompute whether each value 1..limit-1 eventually reaches 89.
    # All intermediate chain values stay below limit because the digit-square
    # sum of any k-digit number is at most k * 81 = limit - 1.
    ends_at_89 = bytearray(limit)
    for i in range(1, limit):
        n = i
        while n not in (1, 89):
            n = digit_square_sum(n)
        ends_at_89[i] = n == 89

    # Digit DP over the decimal digits of (number - 1).
    # Treating shorter numbers as zero-padded strings (e.g. 7 → "0000007")
    # is safe because 0^2 = 0 contributes nothing to the digit-square sum.
    # dp_tight[s] / dp_free[s] = count of digit sequences whose running
    # digit-square sum is s and whose prefix is still ≤ / already < the
    # corresponding prefix of (number - 1).
    digits = [int(d) for d in str(number - 1)] if number > 1 else [0]

    dp_tight: dict[int, int] = {0: 1}
    dp_free: dict[int, int] = {}

    for lim in digits:
        new_tight: dict[int, int] = {}
        new_free: dict[int, int] = {}

        for dss, cnt in dp_tight.items():
            for d in range(lim + 1):
                new_val = dss + d * d
                if new_val < limit:
                    if d == lim:
                        new_tight[new_val] = new_tight.get(new_val, 0) + cnt
                    else:
                        new_free[new_val] = new_free.get(new_val, 0) + cnt

        for dss, cnt in dp_free.items():
            for d in range(10):
                new_val = dss + d * d
                if new_val < limit:
                    new_free[new_val] = new_free.get(new_val, 0) + cnt

        dp_tight, dp_free = new_tight, new_free

    # Sum counts for all digit-square sums that end at 89.
    # dss == 0 corresponds to the number 0, which is excluded.
    return sum(
        cnt
        for dss, cnt in (*dp_tight.items(), *dp_free.items())
        if 0 < dss < limit and ends_at_89[dss]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution() = }")
