"""
In 1682 the German mathematician Gottfried Willhelm von Leibniz formulated
the following alternating series:

1 - 1/3 + 1/5 - 1/7 + 1/9 .. = π/4

This algorithm is called the Leibniz formula (for π),
it is an inefficient approach to calculate the digits of π (pi).

IN: the amount of iterations (int); OUT: the calculated value (float)

Usage:
>>> round(leibniz_formula_for_pi(1000000000), 3)
3.142

>>> leibniz_formula_for_pi("this_is_a_string")
ValueError: The input needs to be an integer.
"""


def leibniz_formula_for_pi(rounds: int) -> float:
    sum = 0.0
    denominator = 1

    if type(rounds) != int:
        raise ValueError("The input needs to be an integer.")

    for round in range(rounds):
        if round % 2 == 0:  # check whether round is an even number
            sum = sum - 1 / denominator
        else:
            sum = sum + 1 / denominator

        denominator = denominator + 2  # 3, 5, 7, 9 etc.

    return abs(4 * sum)  # = π as an positive integer.
