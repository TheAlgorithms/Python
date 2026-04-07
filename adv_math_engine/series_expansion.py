"""Taylor/Maclaurin series expansion utilities."""

from __future__ import annotations

import math
from collections.abc import Callable
from typing import Literal

import numpy as np

HAS_SYMPY = True
try:
    import sympy as sp
except Exception:  # pragma: no cover - optional dependency guard
    HAS_SYMPY = False


SupportedFunction = Literal["exp", "sin", "cos", "log1p"]


def _builtin_derivative_value(name: SupportedFunction, n: int, at: float) -> float:
    if name == "exp":
        return float(math.exp(at))
    if name == "sin":
        return float(math.sin(at + n * math.pi / 2.0))
    if name == "cos":
        return float(math.cos(at + n * math.pi / 2.0))
    if name == "log1p":
        if n == 0:
            return float(math.log1p(at))
        return float(((-1) ** (n - 1)) * math.factorial(n - 1) / (1.0 + at) ** n)
    msg = f"Unsupported function: {name}"
    raise ValueError(msg)


def _numerical_nth_derivative(func: Callable[[float], float], n: int, at: float, h: float = 1e-4) -> float:
    if n == 0:
        return float(func(at))
    if n == 1:
        return float((func(at + h) - func(at - h)) / (2.0 * h))
    return float(
        (_numerical_nth_derivative(func, n - 1, at + h, h) - _numerical_nth_derivative(func, n - 1, at - h, h)) / (2.0 * h)
    )


def taylor_series(
    x: float | np.ndarray,
    order: int,
    center: float = 0.0,
    *,
    function_name: SupportedFunction | None = None,
    function: Callable[[float], float] | None = None,
) -> np.ndarray:
    """Evaluate Taylor polynomial of given order around center.

    f(x) ≈ Σ[n=0..order] f^(n)(a) / n! * (x-a)^n
    """
    if function_name is None and function is None:
        msg = "Provide either function_name or function."
        raise ValueError(msg)

    x_arr = np.asarray(x, dtype=float)
    approximation = np.zeros_like(x_arr, dtype=float)

    for n in range(order + 1):
        if function_name is not None:
            derivative_at_center = _builtin_derivative_value(function_name, n, center)
        else:
            assert function is not None
            derivative_at_center = _numerical_nth_derivative(function, n, center)

        approximation = approximation + derivative_at_center / math.factorial(n) * (x_arr - center) ** n

    return approximation


def maclaurin_series(
    x: float | np.ndarray,
    order: int,
    *,
    function_name: SupportedFunction | None = None,
    function: Callable[[float], float] | None = None,
) -> np.ndarray:
    """Evaluate Maclaurin polynomial (Taylor around 0)."""
    return taylor_series(x, order=order, center=0.0, function_name=function_name, function=function)


def estimate_lagrange_remainder(max_derivative: float, x: float | np.ndarray, order: int, center: float = 0.0) -> np.ndarray:
    """Estimate Lagrange remainder bound: M|x-a|^(n+1)/(n+1)!"""
    x_arr = np.asarray(x, dtype=float)
    return np.abs(max_derivative) * np.abs(x_arr - center) ** (order + 1) / math.factorial(order + 1)


def symbolic_taylor_expression(expr_str: str, symbol: str = "x", center: float = 0.0, order: int = 6) -> str:
    """Return symbolic Taylor expression as a string when SymPy is available."""
    if not HAS_SYMPY:
        msg = "SymPy is not available."
        raise RuntimeError(msg)
    x = sp.symbols(symbol)
    expr = sp.sympify(expr_str)
    series = sp.series(expr, x, center, order + 1).removeO()
    return str(sp.expand(series))
