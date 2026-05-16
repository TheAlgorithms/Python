from __future__ import annotations

"""
Shear stress is a component of stress that is coplanar to the material cross-section.
It arises due to a shear force, the component of the force vector parallel to the
material cross-section.

https://en.wikipedia.org/wiki/Shear_stress
"""


def shear_stress(
    stress: float,
    tangential_force: float,
    area: float,
) -> tuple[str, float]:
    """
    This function can calculate any one of the three -
    1. Shear Stress
    2. Tangential Force
    3. Cross-sectional Area
    This is calculated from the other two provided values
    Examples -
    >>> shear_stress(stress=25, tangential_force=100, area=0)
    ('area', 4.0)
    >>> shear_stress(stress=0, tangential_force=1600, area=200)
    ('stress', 8.0)
    >>> shear_stress(stress=1000, tangential_force=0, area=1200)
    ('tangential_force', 1200000)
    """
    if (stress, tangential_force, area).count(0) != 1:
        raise ValueError("You cannot supply more or less than 2 values")
    elif stress < 0:
        raise ValueError("Stress cannot be negative")
    elif tangential_force < 0:
        raise ValueError("Tangential Force cannot be negative")
    elif area < 0:
        raise ValueError("Area cannot be negative")
    elif stress == 0:
        return (
            "stress",
            tangential_force / area,
        )
    elif tangential_force == 0:
        return (
            "tangential_force",
            stress * area,
        )
    else:
        return (
            "area",
            tangential_force / stress,
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
