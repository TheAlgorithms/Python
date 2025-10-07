"""
Brent's Method for Root Finding
-------------------------------

Brent's method is a robust and efficient algorithm for finding a zero of a
function in a given interval [left, right]. It combines bisection,
secant, and inverse quadratic interpolation methods.

References:
- https://en.wikipedia.org/wiki/Brent%27s_method
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html

Example usage:
>>> def cubic(x):
...     return x**3 - x - 2
>>> round(brent_root(cubic, 1, 2), 5)
1.52138
"""

from typing import Callable

def brent_root(
    function: Callable[[float], float],
    left: float,
    right: float,
    tolerance: float = 1e-5,
    max_iterations: int = 100,
) -> float:
    value_left, value_right = function(left), function(right)
    if value_left * value_right >= 0:
        raise ValueError("Function must have opposite signs at endpoints left and right.")

    previous_point = current_point = left
    value_previous = value_current = value_left
    distance = interval_length = right - left

    for iteration in range(max_iterations):
        if value_current * value_previous > 0:
            previous_point, value_previous = left, value_left
            distance = interval_length = right - left

        if abs(value_previous) < abs(value_current):
            left, current_point, previous_point = current_point, previous_point, current_point
            value_left, value_current, value_previous = value_current, value_previous, value_current

        tolerance1 = 2.0 * 1e-16 * abs(current_point) + 0.5 * tolerance
        midpoint = 0.5 * (previous_point - current_point)

        if abs(midpoint) <= tolerance1 or value_current == 0.0:
            return current_point

        if abs(interval_length) >= tolerance1 and abs(value_left) > abs(value_current):
            ratio = value_current / value_left
            if left == previous_point:
                numerator = 2 * midpoint * ratio
                denominator = 1 - ratio
            else:
                q = value_left / value_previous
                r = value_current / value_previous
                numerator = ratio * (2 * midpoint * q * (q - r) - (current_point - left) * (r - 1))
                denominator = (q - 1) * (r - 1) * (ratio - 1)

            if numerator > 0:
                denominator = -denominator
            numerator = abs(numerator)

            if 2 * numerator < min(3 * midpoint * denominator - abs(tolerance1 * denominator), abs(interval_length * denominator)):
                interval_length = distance
                distance = numerator / denominator
            else:
                distance = midpoint
                interval_length = midpoint
        else:
            distance = midpoint
            interval_length = midpoint

        left, value_left = current_point, value_current
        if abs(distance) > tolerance1:
            current_point += distance
        else:
            current_point += tolerance1 if midpoint > 0 else -tolerance1
        value_current = function(current_point)

    raise RuntimeError("Maximum iterations exceeded in Brent's method.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
