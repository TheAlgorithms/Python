"""
Numerically approximates the derivative of a given function.
"""

from typing import Callable, Union


def forward_differencing(
    fnc: Callable[[Union[int, float]], Union[int, float]],
    x: Union[int, float],
    h: float = 0.001,
) -> float:
    """
    Numerically approximates the derivative of a differentiable function in
    a given point using the forward differencing rule:
    f'(x) ~ (f(x + h) - f(x))/h.
    :param fnc: a function to differentiate
    :param x: point of differentiation
    :param h: step size

    >>> def f(x):
    ...    return x
    >>> '%.3f' % forward_differencing(f, 5, 1e-6)
    '1.000'

    >>> def f(x):
    ...    return x**2
    >>> '%.3f' % forward_differencing(f, 5, 1e-6)
    '10.000'
    """
    return 1.0 * (fnc(x + h) - fnc(x)) / h


def backward_differencing(
    fnc: Callable[[Union[int, float]], Union[int, float]],
    x: Union[int, float],
    h: float = 0.001,
) -> float:
    """
    Numerically approximates the derivative of a differentiable function in
    a given point using the backward differencing rule:
    f'(x) ~ (f(x) - f(x - h))/h.
    :param fnc: a function to differentiate
    :param x: point of differentiation
    :param h: step size

    >>> def f(x):
    ...    return x
    >>> '%.3f' % forward_differencing(f, 5, 1e-6)
    '1.000'

    >>> def f(x):
    ...    return x**2
    >>> '%.3f' % forward_differencing(f, 5, 1e-6)
    '10.000'
    """
    return 1.0 * (fnc(x) - fnc(x - h)) / h


def centered_differencing(
    fnc: Callable[[Union[int, float]], Union[int, float]],
    x: Union[int, float],
    h: float = 0.001,
) -> float:
    """
    Numerically approximates the derivative of a differentiable function in
    a given point using the centered differencing rule:
    f'(x) ~ (f(x + h) - f(x - h))/2*h.
    :param fnc: a function to differentiate
    :param x: point of differentiation
    :param h: step size

    >>> def f(x):
    ...    return x
    >>> '%.3f' % forward_differencing(f, 5, 1e-6)
    '1.000'

    >>> def f(x):
    ...    return x**2
    >>> '%.3f' % forward_differencing(f, 5, 1e-6)
    '10.000'
    """
    return 1.0 * (fnc(x + h) - fnc(x - h)) / (2 * h)


if __name__ == "__main__":

    def f(x):
        return x

    def g(x):
        return x ** 2

    print("f(x) = x")  # derivative of f(x) = x is always 1
    print("The derivative of f in x = 5 is:")
    print(f"\t Using forward differencing: {forward_differencing(f, 5, 1e-6)}")
    print(f"\t Using backward differencing: {backward_differencing(f, 5, 1e-6)}")
    print(f"\t Using centered differencing: {centered_differencing(f, 5, 1e-6)}")

    print("g(x) = x^2")  # derivative of g(x) = x^2 is always 2*x
    print("The derivative of g in x = 5 is:")
    print(f"\t Using forward differencing: {forward_differencing(g, 5, 1e-6)}")
    print(f"\t Using backward differencing: {backward_differencing(g, 5, 1e-6)}")
    print(f"\t Using centered differencing: {centered_differencing(g, 5, 1e-6)}")
