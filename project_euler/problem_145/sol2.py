"""
Project Euler Problem 145: https://projecteuler.net/problem=145

=== Problem statement ===

Some positive integers `n` have the property that the sum `n + reverse(n)`
consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313.
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either `n` or `reverse(n)`.

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?

=== Solution explanation ===

When summing `n` and `reverse(n)`, let's picture how the calculation goes digit
by digit and examine what happens at every position.
We focus on two attributes:
    - Do the digits sum to an odd value, if so, we assign this position a `1`,
    otherwise we assign it a `0`.
    - Do the digits sum to a value greater or equal to 10, thus inducing a
    carry, if so we assign this position a `+`, otherwise we assign it a `-`.

We can construct this way some sort of layout which will prove to be useful.
For instance, we would come up with the following layout for 409:
    4  0  9
    9  0  4
    --------
    1+ 0- 1+

If we miss some information, we will use `x` to indicate it:
    `1x` -> odd sum but could be greater than 10 or not...

We can now make some observations.

If the layout is `1x` at some position (the digits at this position sum to an
odd value) then the digits at the following position (on the right of it) cannot
induce a carry on it.
Therefore we know that the following position should be `x-`.
So we went from a layout like this:
    .. 1x xx .. xx 1x ..
To a layout like this:
    .. 1x x- .. -x 1x ..
(Keep in mind that the layouts are symmetrical)

We can make similar observations by reasoning on the consequences of other
attributes.
Here is a list of a few of such observations:
    .. 1x xx .. xx 1x ..    ===>    .. 1x x- .. x- 1x ..    (a)
    .. x- xx .. xx x- ..    ===>    .. x- 1x .. 1x x- ..    (b)
    .. xx 0x .. 0x xx ..    ===>    .. +x 0x .. 0x +x ..    (c)
    .. xx x+ .. x+ xx ..    ===>    .. 0x x+ .. x+ 0x ..    (d)

Since the rightmost digits necessarily sum to an odd value `1x`, we deduce from
(a) and (b) that all the layouts should be of the form:
    1x x- 1x x- .. x- 1x x- 1x    (F1)

If the layout has an even length, it needs to satisfy the two forms:
    1x x- 1x x- .. 1x x- 1x x-    using (a) and (b) from left to right
    x- 1x x- 1x .. x- 1x x- 1x    using (a) and (b) from right to left
Therefore, it is simply:
    1- 1- 1- 1- .. 1- 1- 1- 1-

Let's examine odd-length layouts.
Since the central digit is summed with itself, the result is an even value `0x`.
Using (c) and (d), we can progressively expand this information to neighboring
positions, and the layout should look like:
    .. x+ 0x x+ 0x x+ 0x x+ ..
                ^
                | central position

If the layout is of length `4k + 1`, it should look like:
    0x x+ .. 0x .. x+ 0x
Which is not compatible with the form (F1):
    1x x- .. 1x .. x- 1x
Therefore, there is no layout of length `4k + 1`.

If the layout is of length `4k + 3`, it should look like:
    x+ 0x .. x+ 0x x+ .. 0x x+
Of course, it also needs to satisfy the form (F1):
    1x x- .. 1x x- 1x .. x- 1x
By merging the two, we get the full picture:
    1+ 0- .. 1+ 0- 1+ .. 1+ 0-

To wrap it up:
- An even-length reversible number has the layout:
    1- 1- 1- 1- .. 1- 1- 1- 1-
- A reversible number of length `4k + 3` has the layout:
    1+ 0- .. 1+ 0- 1+ .. 1+ 0-
- There is no reversible number of length `4k + 1`.

These conditions are necessary but also sufficient.
All that remains for us is to apply basic combinatorics.
"""

from itertools import product

DIGIT_COUPLES = list(product(range(10), repeat=2))

# Constants counting the digit couples (a, b) satisfying certain conditions.
#     `1-`
ODD__LOWER_THAN_10 = len(
    [(a, b) for (a, b) in DIGIT_COUPLES if (a + b) % 2 == 1 and a + b < 10]
)
#     `1-` that starts / ends a layout
ODD__LOWER_THAN_10__NON_ZERO = len(
    [
        (a, b)
        for (a, b) in DIGIT_COUPLES
        if (a + b) % 2 == 1 and a + b < 10 and a != 0 and b != 0
    ]
)
#     `1+`
ODD__GREATER_THAN_10 = len(
    [(a, b) for (a, b) in DIGIT_COUPLES if (a + b) % 2 == 1 and a + b >= 10]
)
#     `0-`
EVEN__SMALLER_THAN_10 = len(
    [(a, b) for (a, b) in DIGIT_COUPLES if (a + b) % 2 == 0 and a + b < 10]
)
#     `0-` that starts / ends a layout
CENTRAL__SMALLER_THAN_10 = len(
    [(a, b) for (a, b) in DIGIT_COUPLES if a == b and a + b < 10]
)


def fixed_length_reversible_numbers_count(length: int) -> int:
    """
    Returns the number of reversible numbers of a given length.
    """
    if length <= 0 or length % 4 == 1:
        return 0
    elif length % 2 == 0:
        return ODD__LOWER_THAN_10__NON_ZERO * ODD__LOWER_THAN_10 ** (length // 2 - 1)
    elif length % 4 == 3:
        k = length // 4
        return (
            ODD__GREATER_THAN_10 ** (k + 1)
            * EVEN__SMALLER_THAN_10**k
            * CENTRAL__SMALLER_THAN_10
        )
    else:
        raise ValueError


def solution(max_length: int = 9) -> int:
    """
    Returns the number of reversible numbers of length not exceeding the given
    one.

    >>> solution(3)
    120
    >>> solution(4)
    720
    >>> solution(5)
    720
    >>> solution(6)
    18720
    >>> solution(7)
    68720
    """
    return sum(
        fixed_length_reversible_numbers_count(length)
        for length in range(max_length + 1)
    )


if __name__ == "__main__":
    print(f"{solution() = }")
