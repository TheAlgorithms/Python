"""Vector calculus operators and numerical integration routines."""

from __future__ import annotations

from collections.abc import Callable

import numpy as np

from adv_math_engine.utils import as_float_array


DerivativeMethod = str


def partial_derivative(
    f: Callable[..., float],
    point: np.ndarray | list[float],
    var_index: int,
    h: float = 1e-5,
    method: DerivativeMethod = "central",
) -> float:
    """Estimate partial derivative using finite differences."""
    x0 = as_float_array(point).astype(float)
    direction = np.zeros_like(x0)
    direction[var_index] = 1.0

    if method == "forward":
        return float((f(*(x0 + h * direction)) - f(*x0)) / h)
    if method == "backward":
        return float((f(*x0) - f(*(x0 - h * direction))) / h)
    if method == "central":
        return float((f(*(x0 + h * direction)) - f(*(x0 - h * direction))) / (2.0 * h))
    msg = "method must be one of {'forward', 'backward', 'central'}"
    raise ValueError(msg)


def gradient(
    f: Callable[..., float], point: np.ndarray | list[float], h: float = 1e-5, method: DerivativeMethod = "central"
) -> np.ndarray:
    """Compute gradient ∇f at a point."""
    x0 = as_float_array(point)
    return np.array([partial_derivative(f, x0, i, h=h, method=method) for i in range(x0.size)])


def divergence(
    field: list[Callable[..., float]], point: np.ndarray | list[float], h: float = 1e-5, method: DerivativeMethod = "central"
) -> float:
    """Compute divergence ∇·F for an n-dimensional vector field."""
    x0 = as_float_array(point)
    if len(field) != x0.size:
        msg = "Field dimension must match point dimension."
        raise ValueError(msg)
    return float(sum(partial_derivative(component, x0, i, h=h, method=method) for i, component in enumerate(field)))


def curl(field: list[Callable[..., float]], point: np.ndarray | list[float], h: float = 1e-5) -> np.ndarray:
    """Compute curl ∇×F for a 3D vector field F = (P, Q, R)."""
    x0 = as_float_array(point)
    if len(field) != 3 or x0.size != 3:
        msg = "Curl is defined for 3D vector fields only."
        raise ValueError(msg)
    p, q, r = field
    d_r_dy = partial_derivative(r, x0, 1, h=h)
    d_q_dz = partial_derivative(q, x0, 2, h=h)
    d_p_dz = partial_derivative(p, x0, 2, h=h)
    d_r_dx = partial_derivative(r, x0, 0, h=h)
    d_q_dx = partial_derivative(q, x0, 0, h=h)
    d_p_dy = partial_derivative(p, x0, 1, h=h)
    return np.array([d_r_dy - d_q_dz, d_p_dz - d_r_dx, d_q_dx - d_p_dy])


def line_integral(
    field: Callable[[np.ndarray], np.ndarray],
    curve: Callable[[np.ndarray], np.ndarray],
    t_start: float,
    t_end: float,
    num_steps: int = 500,
) -> float:
    """Numerically approximate ∫_C F·dr using trapezoidal rule."""
    t = np.linspace(t_start, t_end, num_steps)
    r = curve(t)
    dr_dt = np.gradient(r, t, axis=0)
    f_values = field(r)
    integrand = np.sum(f_values * dr_dt, axis=1)
    return float(np.trapezoid(integrand, t))


def surface_integral(
    scalar_field: Callable[[np.ndarray], np.ndarray],
    parametrization: Callable[[np.ndarray, np.ndarray], np.ndarray],
    u_bounds: tuple[float, float],
    v_bounds: tuple[float, float],
    num_u: int = 120,
    num_v: int = 120,
) -> float:
    """Approximate ∬_S f dS using parameterization r(u,v)."""
    u = np.linspace(u_bounds[0], u_bounds[1], num_u)
    v = np.linspace(v_bounds[0], v_bounds[1], num_v)
    uu, vv = np.meshgrid(u, v, indexing="ij")
    surface_points = parametrization(uu, vv)

    r_u = np.gradient(surface_points, u, axis=0)
    r_v = np.gradient(surface_points, v, axis=1)
    normal_mag = np.linalg.norm(np.cross(r_u, r_v), axis=2)
    field_vals = scalar_field(surface_points)
    integrand = field_vals * normal_mag
    return float(np.trapezoid(np.trapezoid(integrand, v, axis=1), u, axis=0))
