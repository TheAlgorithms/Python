from __future__ import annotations

import numpy as np

from adv_math_engine.series_expansion import _numerical_nth_derivative
from adv_math_engine.utils import timed_call

try:
    import sympy as sp
except Exception:  # pragma: no cover
    sp = None


def numerical_benchmark(iterations: int = 2000) -> float:
    func = lambda x: np.sin(x) * np.exp(x)

    def run() -> float:
        total = 0.0
        for value in np.linspace(-1.0, 1.0, iterations):
            total += _numerical_nth_derivative(func, n=1, at=float(value))
        return total

    _, elapsed = timed_call(run)
    return elapsed


def symbolic_benchmark(iterations: int = 2000) -> float | None:
    if sp is None:
        return None
    x = sp.symbols("x")
    derivative_expr = sp.diff(sp.sin(x) * sp.exp(x), x)
    evaluator = sp.lambdify(x, derivative_expr, "numpy")

    def run() -> float:
        total = 0.0
        for value in np.linspace(-1.0, 1.0, iterations):
            total += float(evaluator(value))
        return total

    _, elapsed = timed_call(run)
    return elapsed


if __name__ == "__main__":
    num_time = numerical_benchmark()
    sym_time = symbolic_benchmark()
    print(f"numerical_time_seconds={num_time:.6f}")
    if sym_time is None:
        print("symbolic_time_seconds=unavailable")
    else:
        print(f"symbolic_time_seconds={sym_time:.6f}")
