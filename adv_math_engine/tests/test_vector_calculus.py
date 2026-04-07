from __future__ import annotations

import numpy as np

from adv_math_engine.vector_calculus import (
    curl,
    divergence,
    gradient,
    line_integral,
    partial_derivative,
    surface_integral,
)


def test_partial_derivative_central() -> None:
    f = lambda x, y: x**2 + y**3
    value = partial_derivative(f, [2.0, 3.0], 0, method="central")
    assert np.isclose(value, 4.0, atol=1e-4)


def test_gradient_matches_analytic() -> None:
    f = lambda x, y, z: x**2 + y**2 + z**2
    grad = gradient(f, [1.0, -2.0, 0.5])
    assert np.allclose(grad, np.array([2.0, -4.0, 1.0]), atol=1e-4)


def test_divergence() -> None:
    field = [lambda x, y, z: x**2, lambda x, y, z: y**2, lambda x, y, z: z**2]
    div = divergence(field, [1.0, 2.0, 3.0])
    assert np.isclose(div, 12.0, atol=1e-3)


def test_curl() -> None:
    field = [lambda x, y, z: -y, lambda x, y, z: x, lambda x, y, z: 0.0]
    result = curl(field, [0.2, -0.3, 1.5])
    assert np.allclose(result, np.array([0.0, 0.0, 2.0]), atol=1e-3)


def test_line_integral_circle() -> None:
    field = lambda r: np.column_stack((-r[:, 1], r[:, 0]))
    curve = lambda t: np.column_stack((np.cos(t), np.sin(t)))
    value = line_integral(field, curve, 0.0, 2.0 * np.pi, num_steps=2000)
    assert np.isclose(value, 2.0 * np.pi, atol=2e-2)


def test_surface_integral_unit_sphere_area_like() -> None:
    scalar_field = lambda points: np.ones(points.shape[:2])

    def sphere(u: np.ndarray, v: np.ndarray) -> np.ndarray:
        x = np.sin(u) * np.cos(v)
        y = np.sin(u) * np.sin(v)
        z = np.cos(u)
        return np.stack((x, y, z), axis=2)

    value = surface_integral(scalar_field, sphere, (0.0, np.pi), (0.0, 2.0 * np.pi), num_u=150, num_v=150)
    assert np.isclose(value, 4.0 * np.pi, atol=0.1)
