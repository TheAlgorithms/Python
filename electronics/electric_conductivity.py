from __future__ import annotations

ELECTRON_CHARGE = 1.6021e-19  # units = C


def electric_conductivity(
    conductivity: float,
    electron_conc: float,
    mobility: float,
) -> tuple[str, float]:
    """
    This function can calculate any one of the three -
    1. Conductivity
    2. Electron Concentration
    3. Electron Mobility
    This is calculated from the other two provided values
    Examples -
    >>> electric_conductivity(conductivity=25, electron_conc=100, mobility=0)
    ('mobility', 1.5604519068722301e+18)
    >>> electric_conductivity(conductivity=0, electron_conc=1600, mobility=200)
    ('conductivity', 5.12672e-14)
    >>> electric_conductivity(conductivity=1000, electron_conc=0, mobility=1200)
    ('electron_conc', 5.201506356240767e+18)
    """
    if (conductivity, electron_conc, mobility).count(0) != 1:
        raise ValueError("You cannot supply more or less than 2 values")
    elif conductivity < 0:
        raise ValueError("Conductivity cannot be negative")
    elif electron_conc < 0:
        raise ValueError("Electron concentration cannot be negative")
    elif mobility < 0:
        raise ValueError("mobility cannot be negative")
    elif conductivity == 0:
        return (
            "conductivity",
            mobility * electron_conc * ELECTRON_CHARGE,
        )
    elif electron_conc == 0:
        return (
            "electron_conc",
            conductivity / (mobility * ELECTRON_CHARGE),
        )
    else:
        return (
            "mobility",
            conductivity / (electron_conc * ELECTRON_CHARGE),
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
