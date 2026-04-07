from __future__ import annotations

import math

import numpy as np

from adv_math_engine.series_expansion import (
    estimate_lagrange_remainder,
    maclaurin_series,
    taylor_series,
)
from adv_math_engine.utils import validate_tolerance


def test_maclaurin_exp_convergence() -> None:
    x = np.linspace(-1.0, 1.0, 50)
    approx = maclaurin_series(x, order=12, function_name="exp")
    actual = np.exp(x)
    assert validate_tolerance(approx, actual, epsilon=1e-4)


def test_taylor_sin_about_nonzero_center() -> None:
    x = np.array([0.2, 0.3, 0.5])
    approx = taylor_series(x, order=9, center=0.3, function_name="sin")
    assert np.allclose(approx, np.sin(x), atol=1e-6)


def test_log1p_remainder_bound() -> None:
    x = 0.2
    order = 6
    approx = maclaurin_series(x, order=order, function_name="log1p")
    actual = np.log1p(x)
    remainder = estimate_lagrange_remainder(max_derivative=math.factorial(order), x=x, order=order)
    assert abs(actual - approx) <= remainder + 1e-6


def test_arbitrary_function_numeric_derivative() -> None:
    f = lambda val: np.cos(val) * np.exp(val)
    x = np.array([0.0, 0.1, 0.2])
    approx = taylor_series(x, order=8, center=0.0, function=f)
    assert np.allclose(approx, f(x), atol=5e-3)
