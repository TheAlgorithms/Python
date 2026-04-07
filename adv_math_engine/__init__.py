"""Advanced mathematics engine for vector algebra, vector calculus, and series expansions."""

from adv_math_engine.series_expansion import (
    estimate_lagrange_remainder,
    maclaurin_series,
    taylor_series,
)
from adv_math_engine.vector_algebra import (
    angle_between,
    check_linear_independence,
    cross_product,
    dot_product,
    gram_schmidt,
    vector_projection,
)
from adv_math_engine.vector_calculus import (
    curl,
    divergence,
    gradient,
    line_integral,
    partial_derivative,
    surface_integral,
)

__all__ = [
    "angle_between",
    "check_linear_independence",
    "cross_product",
    "curl",
    "divergence",
    "dot_product",
    "estimate_lagrange_remainder",
    "gradient",
    "gram_schmidt",
    "line_integral",
    "maclaurin_series",
    "partial_derivative",
    "surface_integral",
    "taylor_series",
    "vector_projection",
]
