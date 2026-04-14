"""
Calculates the First Fundamental Form of a parametric surface.

The first fundamental form allows the measurement of lengths, angles,
and areas on a surface defined by parametric equations r(u, v).

Reference:
- https://en.wikipedia.org/wiki/First_fundamental_form

Author: Chahat Sandhu
GitHub: https://github.com/singhc7
"""

import sympy as sp


def first_fundamental_form(
    x_expr: str, y_expr: str, z_expr: str
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """
    Calculate the First Fundamental Form coefficients (E, F, G) for a surface
    defined by parametric equations x(u,v), y(u,v), z(u,v).

    Args:
        x_expr: A string representing the x component in terms of u and v.
        y_expr: A string representing the y component in terms of u and v.
        z_expr: A string representing the z component in terms of u and v.

    Returns:
        A tuple containing the sympy expressions for E, F, and G.

    Examples:
        >>> # Example 1: A simple plane r(u, v) = <u, v, 0>
        >>> E, F, G = first_fundamental_form("u", "v", "0")
        >>> print(f"E: {E}, F: {F}, G: {G}")
        E: 1, F: 0, G: 1

        >>> # Example 2: A paraboloid r(u, v) = <u, v, u**2 + v**2>
        >>> E, F, G = first_fundamental_form("u", "v", "u**2 + v**2")
        >>> print(f"E: {E}, F: {F}, G: {G}")
        E: 4*u**2 + 1, F: 4*u*v, G: 4*v**2 + 1

        >>> # Example 3: A cylinder r(u, v) = <cos(u), sin(u), v>
        >>> E, F, G = first_fundamental_form("cos(u)", "sin(u)", "v")
        >>> print(f"E: {sp.simplify(E)}, F: {F}, G: {G}")
        E: 1, F: 0, G: 1
    """
    # Define the mathematical symbols
    u, v = sp.symbols("u v")

    # Parse the string expressions into sympy objects
    x = sp.sympify(x_expr)
    y = sp.sympify(y_expr)
    z = sp.sympify(z_expr)

    # Define the position vector r
    r = sp.Matrix([x, y, z])

    # Calculate partial derivatives (tangent vectors)
    r_u = sp.diff(r, u)
    r_v = sp.diff(r, v)

    # Compute the coefficients E, F, G using the dot product
    # We use simplify to combine trigonometric terms where possible
    e = sp.simplify(r_u.dot(r_u))
    f = sp.simplify(r_u.dot(r_v))
    g = sp.simplify(r_v.dot(r_v))

    return e, f, g


if __name__ == "__main__":
    import doctest

    doctest.testmod()
