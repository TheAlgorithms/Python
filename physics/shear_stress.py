from __future__ import annotations

"""
In foundational mechanics, shear stress is defined as a stress component that acts
parallel to the material's cross-section. It arises from a shear force, which is the
component of the force vector acting coplanar with the cross-section.

The relationship is governed by the core formula: tau = F / A
where:
    tau (τ) is the shear stress
    F is the tangential force (shear force)
    A is the cross-sectional area

Reference: https://en.wikipedia.org/wiki/Shear_stress
"""


def calculate_shear_stress(
    shear_stress: float | None = None,
    tangential_force: float | None = None,
    area: float | None = None,
) -> float:
    """
    Calculates the missing variable in the shear stress formula (tau = F / A).
    Exactly two of the parameters must be provided.

    Args:
        shear_stress: The stress parallel to the cross-section (Pascal).
        tangential_force: The force acting parallel to the cross-section (Newton).
        area: The cross-sectional area (Square meters).

    Returns:
        The calculated missing value (shear_stress, tangential_force, or area).

    Raises:
        ValueError: If fewer or more than two parameters are provided,
                    if a parameter is negative, or if a division by zero occurs.

    Examples:
        >>> calculate_shear_stress(tangential_force=100.0, area=4.0)
        25.0
        >>> calculate_shear_stress(shear_stress=8.0, area=200.0)
        1600.0
        >>> calculate_shear_stress(shear_stress=1000.0, tangential_force=1200000.0)
        1200.0
    """
    params = (shear_stress, tangential_force, area)
    none_count = params.count(None)

    if none_count != 1:
        raise ValueError("Exactly two values must be provided to calculate the third.")

    # Validation: Physically, these values should not be negative in this context
    if any(p is not None and p < 0 for p in params):
        raise ValueError("Parameters cannot be negative.")

    if shear_stress is None:
        if area == 0:
            raise ValueError("Area cannot be zero when calculating stress.")
        return tangential_force / area

    if tangential_force is None:
        return shear_stress * area

    if area is None:
        if shear_stress == 0:
            raise ValueError("Shear stress cannot be zero when calculating area.")
        return tangential_force / shear_stress

    return 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
