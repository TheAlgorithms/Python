"""
Functions useful for doing molecular chemistry:
* molarity_to_normality
* moles_to_pressure
* moles_to_volume
* pressure_and_volume_to_temperature
* mass_to_moles
* moles_to_molecules
"""


def molarity_to_normality(nfactor: int, moles: float, volume: float) -> float:
    """
    Convert molarity to normality.
      Volume is taken in litres.

      Wikipedia reference: https://en.wikipedia.org/wiki/Equivalent_concentration
      Wikipedia reference: https://en.wikipedia.org/wiki/Molar_concentration

      >>> molarity_to_normality(2, 3.1, 0.31)
      20
      >>> molarity_to_normality(4, 11.4, 5.7)
      8
    """
    return round(float(moles / volume) * nfactor)


def moles_to_pressure(volume: float, moles: float, temperature: float) -> float:
    """
    Convert moles to pressure.
      Ideal gas laws are used.
      Temperature is taken in kelvin.
      Volume is taken in litres.
      Pressure has atm as SI unit.

      Wikipedia reference: https://en.wikipedia.org/wiki/Gas_laws
      Wikipedia reference: https://en.wikipedia.org/wiki/Pressure
      Wikipedia reference: https://en.wikipedia.org/wiki/Temperature

      >>> moles_to_pressure(0.82, 3, 300)
      90
      >>> moles_to_pressure(8.2, 5, 200)
      10
    """
    return round(float((moles * 0.0821 * temperature) / (volume)))


def moles_to_volume(pressure: float, moles: float, temperature: float) -> float:
    """
    Convert moles to volume.
      Ideal gas laws are used.
      Temperature is taken in kelvin.
      Volume is taken in litres.
      Pressure has atm as SI unit.

      Wikipedia reference: https://en.wikipedia.org/wiki/Gas_laws
      Wikipedia reference: https://en.wikipedia.org/wiki/Pressure
      Wikipedia reference: https://en.wikipedia.org/wiki/Temperature

      >>> moles_to_volume(0.82, 3, 300)
      90
      >>> moles_to_volume(8.2, 5, 200)
      10
    """
    return round(float((moles * 0.0821 * temperature) / (pressure)))


def pressure_and_volume_to_temperature(
    pressure: float, moles: float, volume: float
) -> float:
    """
    Convert pressure and volume to temperature.
      Ideal gas laws are used.
      Temperature is taken in kelvin.
      Volume is taken in litres.
      Pressure has atm as SI unit.

      Wikipedia reference: https://en.wikipedia.org/wiki/Gas_laws
      Wikipedia reference: https://en.wikipedia.org/wiki/Pressure
      Wikipedia reference: https://en.wikipedia.org/wiki/Temperature

      >>> pressure_and_volume_to_temperature(0.82, 1, 2)
      20
      >>> pressure_and_volume_to_temperature(8.2, 5, 3)
      60
    """
    return round(float((pressure * volume) / (0.0821 * moles)))


def mass_to_moles(mass: float, molar_mass: float) -> float:
    """
    Convert mass of a substance to moles.
      Mass is taken in grams.
      Molar mass is taken in grams per mole (g/mol).

      Wikipedia reference: https://en.wikipedia.org/wiki/Mole_(unit)

      >>> mass_to_moles(36.03, 18.015)
      2.0
      >>> mass_to_moles(11.0, 44.01)
      0.25
    """
    if molar_mass <= 0:
        raise ValueError("Molar mass must be greater than zero.")
    if mass < 0:
        raise ValueError("Mass cannot be negative.")

    return round(float(mass / molar_mass), 2)


def moles_to_molecules(moles: float) -> float:
    """
    Convert moles of a substance to total molecules using Avogadro's constant.

      Wikipedia reference: https://en.wikipedia.org/wiki/Avogadro_constant

      >>> moles_to_molecules(2)
      1.2044e+24
      >>> moles_to_molecules(0.5)
      3.011e+23
    """
    if moles < 0:
        raise ValueError("Moles cannot be negative.")

    return float(f"{moles * 6.022e23:.4e}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
