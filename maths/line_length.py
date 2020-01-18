from typing import Callable, Union
import math as m

def line_length(fnc: Callable[[Union[int, float]], Union[int, float]],
                x_start: Union[int, float],
                x_end: Union[int, float],
                steps: int = 100) -> float:

    """
    Approximates the arc length of a line segment by treating the curve as a
    sequence of linear lines and summing their lengths
    :param fnc: a function which defines a curve
    :param x_start: left end point to indicate the start of line segment
    :param x_end: right end point to indicate end of line segment
    :param steps: an accuracy gauge; more steps increases accuracy
    :return: a float representing the length of the curve

    >>> def f(x):
    ...    return x
    >>> f"{line_length(f, 0, 1, 10):.6f}"
    '1.414214'

    >>> def f(x):
    ...    return 1
    >>> f"{line_length(f, -5.5, 4.5):.6f}"
    '10.000000'

    >>> def f(x):
    ...    return m.sin(5 * x) + m.cos(10 * x) + x * x/10
    >>> f"{line_length(f, 0.0, 10.0, 10000):.6f}"
    '69.534930'
    """

    x1 = x_start
    fx1 = fnc(x_start)
    length = 0.0

    for i in range(steps):

        # Approximates curve as a sequence of linear lines and sums their length
        x2 = (x_end - x_start) / steps + x1
        fx2 = fnc(x2)
        length += m.hypot(x2 - x1, fx2 - fx1)

        # Increment step
        x1 = x2
        fx1 = fx2

    return length

if __name__ == "__main__":

    def f(x):
        return m.sin(10*x)

    print("f(x) = sin(10 * x)")
    print("The length of the curve from x = -10 to x = 10 is:")
    i = 10
    while i <= 100000:
        print(f"With {i} steps: {line_length(f, -10, 10, i)}")
        i *= 10
