"""
Brent's Method for Root Finding

Find a root of a function in a bracketing interval using Brent's method.

Brent's method combines bisection, secant, and inverse quadratic interpolation
to efficiently and robustly find a root of a continuous function. It is
guaranteed to converge as long as the root is bracketed.

See:
    https://en.wikipedia.org/wiki/Brent%27s_method

Author: Aryan Singh (2nd year LNMIIT)
"""

from collections.abc import Callable


def brent_method(
    function: Callable[[float], float],
    lower_bound: float,
    upper_bound: float,
    tolerance: float = 1e-14,
    max_iterations: int = 100,
) -> float:
    """
    Find a root of a function in a bracketing interval using Brent's method.

    Args:
        function: A continuous function for which the root is sought.
        lower_bound: One end of the bracketing interval.
        upper_bound: The other end of the bracketing interval.
        tolerance: The tolerance for convergence (default 1e-14).
        max_iterations: Maximum number of iterations (default 100).

    Returns:
        A float value approximating the root.

    Raises:
        ValueError: If the root is not bracketed in [lower_bound, upper_bound].

    Examples:
        >>> round(brent_method(lambda x: x**3 - 1, -5, 5), 6)
        1.0
        >>> round(brent_method(lambda x: x**2 - 4*x + 3, 0, 2), 6)
        1.0
        >>> round(brent_method(lambda x: x**2 - 4*x + 3, 2, 4), 6)
        3.0
        >>> brent_method(lambda x: x**2 - 4*x + 3, 4, 1000)
        Traceback (most recent call last):
            ...
        ValueError: Root is not bracketed in the interval [4, 1000].
    """
    function_lower = function(lower_bound)
    function_upper = function(upper_bound)
    if function_lower * function_upper >= 0:
        error_message = (
            f"Root is not bracketed in the interval [{lower_bound}, {upper_bound}]."
        )
        raise ValueError(error_message)

    if abs(function_lower) < abs(function_upper):
        lower_bound, upper_bound = upper_bound, lower_bound
        function_lower, function_upper = function_upper, function_lower

    previous_bound = lower_bound
    function_previous = function_lower
    previous_step = upper_bound - lower_bound
    bisect_flag = True

    for _ in range(max_iterations):
        if function_upper == 0:
            return round(upper_bound, 12)
        if function_previous not in {function_lower, function_upper}:
            # Inverse quadratic interpolation
            s = (
                lower_bound
                * function_upper
                * function_previous
                / (
                    (function_lower - function_upper)
                    * (function_lower - function_previous)
                )
                + upper_bound
                * function_lower
                * function_previous
                / (
                    (function_upper - function_lower)
                    * (function_upper - function_previous)
                )
                + previous_bound
                * function_lower
                * function_upper
                / (
                    (function_previous - function_lower)
                    * (function_previous - function_upper)
                )
            )
        else:
            # Secant method
            s = upper_bound - function_upper * (upper_bound - lower_bound) / (
                function_upper - function_lower
            )

        conditions = [
            not (
                (3 * lower_bound + upper_bound) / 4 < s < upper_bound
                if upper_bound > lower_bound
                else upper_bound < s < (3 * lower_bound + upper_bound) / 4
            ),
            bisect_flag
            and abs(s - upper_bound) >= abs(upper_bound - previous_bound) / 2,
            not bisect_flag
            and abs(s - upper_bound) >= abs(previous_bound - previous_step) / 2,
            bisect_flag and abs(upper_bound - previous_bound) < tolerance,
            not bisect_flag and abs(previous_bound - previous_step) < tolerance,
        ]
        if any(conditions):
            s = (lower_bound + upper_bound) / 2
            bisect_flag = True
        else:
            bisect_flag = False

        function_s = function(s)
        previous_step, previous_bound = previous_bound, upper_bound
        function_previous = function_upper

        if function_lower * function_s < 0:
            upper_bound = s
            function_upper = function_s
        else:
            lower_bound = s
            function_lower = function_s

        if abs(function_lower) < abs(function_upper):
            lower_bound, upper_bound = upper_bound, lower_bound
            function_lower, function_upper = function_upper, function_lower

        if abs(upper_bound - lower_bound) < tolerance or function_upper == 0:
            return round(upper_bound, 12)

    return round(upper_bound, 12)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
