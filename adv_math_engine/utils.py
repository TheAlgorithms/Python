"""Utility helpers for numerical computations."""

from __future__ import annotations

from collections.abc import Callable
from time import perf_counter

import numpy as np

ArrayLike = float | list[float] | np.ndarray


def as_float_array(value: ArrayLike) -> np.ndarray:
    """Convert any scalar/vector-like input to a NumPy float64 array."""
    return np.asarray(value, dtype=float)


def validate_tolerance(numerical: float | np.ndarray, actual: float | np.ndarray, epsilon: float = 1e-6) -> bool:
    """Return True if |numerical - actual| < epsilon for all entries."""
    return bool(np.all(np.abs(as_float_array(numerical) - as_float_array(actual)) < epsilon))


def timed_call(fn: Callable[..., object], *args: object, **kwargs: object) -> tuple[object, float]:
    """Run a callable and return (result, elapsed_seconds)."""
    start = perf_counter()
    result = fn(*args, **kwargs)
    return result, perf_counter() - start
