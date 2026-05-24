"""
Project Euler Problem 142: https://projecteuler.net/problem=142

Perfect Square Collection

Find the smallest x + y + z with integers x > y > z > 0  such that
x + y, x - y, x + z, x - z, y + z, y - z are all perfect squares.


Change the variables to a, b, c, so that 3 requirements are satisfied automatically:
a^2 = y - z
b^2 = x - y
c^2 = z + x

and the rest of requirements for perfect squares are:
z + y = c^2 - b^2
y + x = a^2 + c^2
x - z = a^2 + b^2

Then iterate over a^2, b^2 and c^2 to check if the combination satisfies all
3 requirements.

The total sum x + y + z = (a^2 - b^2 + 3c^2) / 2, so we break loop for c^2 if
the sum is already bigger than found sum.

"""


def solution(number_of_terms: int = 3) -> int | None:
    """

    Iterate over combinations of a, b, c and save min sum.
    In case only one term x = 1 is solution.
    In case of two terms, x = 5, y = 4 is the solution.

    >>> solution(1)
    1
    >>> solution(2)
    9
    """

    if number_of_terms == 1:
        return 1
    if number_of_terms == 2:
        return 9

    n_max = 2500
    squares: list[int] = []

    for a in range(n_max + 1):
        squares += [a * a]
    squares_set = set(squares)

    min_sum = None
    for a in range(1, len(squares)):
        a_sq = squares[a]
        for b in range(1, len(squares)):
            b_sq = squares[b]
            if a_sq + b_sq not in squares_set:
                continue
            for c in range(max(a, b) + 1, len(squares)):
                c_sq = squares[c]
                # break if x + y + z is already bigger than min_sum:
                if min_sum is not None and (a_sq - b_sq + 3 * c_sq) // 2 > min_sum:
                    break
                if (c_sq - b_sq in squares_set) and (a_sq + c_sq in squares_set):
                    x2, y2, z2 = (
                        a_sq + b_sq + c_sq,
                        a_sq - b_sq + c_sq,
                        c_sq - a_sq - b_sq,
                    )
                    if z2 > 0 and x2 % 2 == 0 and y2 % 2 == 0 and z2 % 2 == 0:
                        sum_ = (x2 + y2 + z2) // 2
                        min_sum = sum_ if min_sum is None else min(min_sum, sum_)

    return min_sum


if __name__ == "__main__":
    print(f"{solution() = }")
