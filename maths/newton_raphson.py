"""
Author: P Shreyas Shetty
Implementation of Newton-Raphson method for solving equations of kind
f(x) = 0. It is an iterative method where solution is found by the expression
    x[n+1] = x[n] + f(x[n])/f'(x[n])
If no solution exists, then either the solution will not be found when iteration
limit is reached or the gradient f'(x[n]) approaches zero. In both cases, exception
is raised. If iteration limit is reached, try increasing maxiter.
"""

import math as m
from collections.abc import Callable

DerivativeFunc = Callable[[float], float]


def calc_derivative(f: DerivativeFunc, a: float, h: float = 0.001) -> float:
    """
    Calculates derivative at point a for function f using finite difference
    method
    """
    return (f(a + h) - f(a - h)) / (2 * h)


def newton_raphson(
    f: DerivativeFunc,
    x0: float = 0,
    maxiter: int = 100,
    step: float = 0.0001,
    maxerror: float = 1e-6,
    logsteps: bool = False,
) -> tuple[float, float, list[float]]:
    a = x0  # set the initial guess
    steps = [a]
    error = abs(f(a))
    f1 = lambda x: calc_derivative(f, x, h=step)  # noqa: E731  Derivative of f(x)
    for _ in range(maxiter):
        if f1(a) == 0:
            raise ValueError("No converging solution found")
        a = a - f(a) / f1(a)  # Calculate the next estimate
        if logsteps:
            steps.append(a)
        if error < maxerror:
            break
    else:
        raise ValueError("Iteration limit reached, no converging solution found")
    if logsteps:
        # If logstep is true, then log intermediate steps
        return a, error, steps
    return a, error, []


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    f = lambda x: m.tanh(x) ** 2 - m.exp(3 * x)  # noqa: E731
    solution, error, steps = newton_raphson(
        f, x0=10, maxiter=1000, step=1e-6, logsteps=True
    )
    plt.plot([abs(f(x)) for x in steps])
    plt.xlabel("step")
    plt.ylabel("error")
    plt.show()
    print(f"solution = {{{solution:f}}}, error = {{{error:f}}}")
