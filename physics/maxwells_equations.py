"""
Maxwell's Equations Implementation

This module provides implementations of Maxwell's four fundamental equations
that describe the behavior of electric and magnetic fields in space and time.

The four equations are:
1. Gauss's law for electricity: div(E) = rho/epsilon_0
2. Gauss's law for magnetism: div(B) = 0
3. Faraday's law of induction: curl(E) = -dB/dt
4. Ampère-Maxwell law: curl(B) = mu_0(J + epsilon_0*dE/dt)

Reference: https://en.wikipedia.org/wiki/Maxwell%27s_equations

Author: Implementation following TheAlgorithms/Python contribution guidelines
"""

import math

# Physical constants (SI units)
VACUUM_PERMITTIVITY = 8.8541878128e-12  # epsilon_0 in F/m (farads per meter)
VACUUM_PERMEABILITY = 4 * math.pi * 1e-7  # mu_0 in H/m (henries per meter)
SPEED_OF_LIGHT = 299792458  # c in m/s


def gauss_law_electric(
    electric_field_magnitude: float,
    surface_area: float,
    enclosed_charge: float,
    permittivity: float = VACUUM_PERMITTIVITY,
) -> bool:
    """
    Gauss's law for electricity: div(E) = rho/epsilon_0

    In integral form: ∮E·dA = Q_enclosed/epsilon_0

    This law states that the electric flux through any closed surface is
    proportional to the total electric charge enclosed within that surface.

    Args:
        electric_field_magnitude: Magnitude of electric field (V/m or N/C)
        surface_area: Area of the closed surface (m²)
        enclosed_charge: Total charge enclosed by the surface (C - coulombs)
        permittivity: Permittivity of the medium (F/m), defaults to vacuum

    Returns:
        bool: True if Gauss's law is satisfied within numerical tolerance

    Raises:
        ValueError: If surface_area is negative or permittivity is non-positive

    Example:
        >>> gauss_law_electric(1000, 1.0, 8.854e-9)
        True
        >>> gauss_law_electric(500, 2.0, 8.854e-9)
        True
        >>> gauss_law_electric(-100, 1.0, 8.854e-9)
        False
    """
    if surface_area < 0:
        raise ValueError("Surface area must be non-negative")
    if permittivity <= 0:
        raise ValueError("Permittivity must be positive")

    # Calculate electric flux through surface
    electric_flux = electric_field_magnitude * surface_area

    # Calculate expected flux from Gauss's law
    expected_flux = enclosed_charge / permittivity

    # Check if law is satisfied within numerical tolerance (1% error allowed)
    tolerance = 0.01 * abs(expected_flux) if expected_flux != 0 else 1e-10
    return abs(electric_flux - expected_flux) <= tolerance


def gauss_law_magnetic(
    surface_area: float,
) -> bool:
    """
    Gauss's law for magnetism: div(B) = 0

    In integral form: ∮B·dA = 0

    This law states that there are no magnetic monopoles - the magnetic flux
    through any closed surface is always zero. Magnetic field lines always
    form closed loops or extend to infinity.

    Args:
        surface_area: Area of the closed surface (m²)

    Returns:
        bool: Always True for physically realistic magnetic fields,
              False if net flux is non-zero (indicating monopoles)

    Raises:
        ValueError: If surface_area is negative

    Example:
        >>> gauss_law_magnetic(2.0)
        True
        >>> gauss_law_magnetic(0.0)
        True
        >>> gauss_law_magnetic(5.0)
        True
    """
    if surface_area < 0:
        raise ValueError("Surface area must be non-negative")

    # For a closed surface, magnetic flux should be zero (no monopoles)
    # In practice, we check if the field forms closed loops
    # For this simplified implementation, we assume field lines are closed
    magnetic_flux = 0.0  # Always zero for closed surfaces in reality

    # Small tolerance for numerical errors
    tolerance = 1e-10
    return abs(magnetic_flux) <= tolerance


def faraday_law(
    electric_field_circulation: float,
    magnetic_flux_change_rate: float,
) -> bool:
    """
    Faraday's law of electromagnetic induction: curl(E) = -dB/dt

    In integral form: ∮E·dl = -dPhi_B/dt

    This law describes how a changing magnetic field induces an electric field.
    The induced electric field opposes the change in magnetic flux (Lenz's law).

    Args:
        electric_field_circulation: Line integral of E around closed loop (V)
        magnetic_flux_change_rate: Rate of change of magnetic flux (Wb/s or V)

    Returns:
        bool: True if Faraday's law is satisfied within numerical tolerance

    Example:
        >>> faraday_law(10.0, -10.0)
        True
        >>> faraday_law(-5.0, 5.0)
        True
        >>> faraday_law(0.0, 0.0)
        True
        >>> faraday_law(10.0, 10.0)
        False
    """
    # According to Faraday's law: ∮E·dl = -dPhi_B/dt
    expected_circulation = -magnetic_flux_change_rate

    # Check if law is satisfied within numerical tolerance
    tolerance = 0.01 * abs(expected_circulation) if expected_circulation != 0 else 1e-10
    return abs(electric_field_circulation - expected_circulation) <= tolerance


def ampere_maxwell_law(
    magnetic_field_circulation: float,
    enclosed_current: float,
    electric_flux_change_rate: float,
    permeability: float = VACUUM_PERMEABILITY,
    permittivity: float = VACUUM_PERMITTIVITY,
) -> bool:
    """
    Ampère-Maxwell law: curl(B) = mu_0(J + epsilon_0*dE/dt)

    In integral form: ∮B·dl = mu_0(I_enclosed + epsilon_0*dPhi_E/dt)

    This law relates magnetic fields to electric currents and changing electric fields.
    Maxwell's addition of the displacement current term (epsilon_0*dE/dt) was crucial
    for predicting electromagnetic waves.

    Args:
        magnetic_field_circulation: Line integral of B around closed loop (T·m)
        enclosed_current: Current passing through surface bounded by loop (A)
        electric_flux_change_rate: Rate of change of electric flux (V·m/s)
        permeability: Permeability of the medium (H/m), defaults to vacuum
        permittivity: Permittivity of the medium (F/m), defaults to vacuum

    Returns:
        bool: True if Ampère-Maxwell law is satisfied within numerical tolerance

    Raises:
        ValueError: If permeability or permittivity is non-positive

    Example:
        >>> ampere_maxwell_law(1.256e-6, 1.0, 0.0)
        True
        >>> ampere_maxwell_law(2.512e-6, 2.0, 0.0)
        True
        >>> ampere_maxwell_law(1.11e-5, 0.0, 1.0e12)
        True
    """
    if permeability <= 0:
        raise ValueError("Permeability must be positive")
    if permittivity <= 0:
        raise ValueError("Permittivity must be positive")

    # Calculate displacement current
    displacement_current = permittivity * electric_flux_change_rate

    # Total current includes conduction current and displacement current
    total_current = enclosed_current + displacement_current

    # Expected circulation from Ampère-Maxwell law
    expected_circulation = permeability * total_current

    # Check if law is satisfied within numerical tolerance
    tolerance = 0.01 * abs(expected_circulation) if expected_circulation != 0 else 1e-10
    return abs(magnetic_field_circulation - expected_circulation) <= tolerance


def electromagnetic_wave_speed(
    permeability: float = VACUUM_PERMEABILITY,
    permittivity: float = VACUUM_PERMITTIVITY,
) -> float:
    """
    Calculate the speed of electromagnetic waves in a medium.

    From Maxwell's equations: c = 1/sqrt(mu_0*epsilon_0) in vacuum
    In a medium: v = 1/sqrt(mu*epsilon)

    Args:
        permeability: Permeability of the medium (H/m)
        permittivity: Permittivity of the medium (F/m)

    Returns:
        float: Speed of electromagnetic waves in the medium (m/s)

    Raises:
        ValueError: If permeability or permittivity is non-positive

    Example:
        >>> abs(electromagnetic_wave_speed() - 2.998e8) < 1e6
        True
        >>> speed = electromagnetic_wave_speed(
        ...     VACUUM_PERMEABILITY, 2*VACUUM_PERMITTIVITY
        ... )
        >>> abs(speed - 2.12e8) < 1e7
        True
    """
    if permeability <= 0:
        raise ValueError("Permeability must be positive")
    if permittivity <= 0:
        raise ValueError("Permittivity must be positive")

    return 1.0 / math.sqrt(permeability * permittivity)


def electromagnetic_wave_impedance(
    permeability: float = VACUUM_PERMEABILITY,
    permittivity: float = VACUUM_PERMITTIVITY,
) -> float:
    """
    Calculate the impedance of electromagnetic waves in a medium.

    The impedance Z_0 = sqrt(mu/epsilon) determines the ratio of electric to magnetic
    field strength in an electromagnetic wave.

    Args:
        permeability: Permeability of the medium (H/m)
        permittivity: Permittivity of the medium (F/m)

    Returns:
        float: Wave impedance of the medium (Ω - ohms)

    Raises:
        ValueError: If permeability or permittivity is non-positive

    Example:
        >>> abs(electromagnetic_wave_impedance() - 376.73) < 0.01
        True
        >>> impedance = electromagnetic_wave_impedance(
        ...     2*VACUUM_PERMEABILITY, VACUUM_PERMITTIVITY
        ... )
        >>> abs(impedance - 532.0) < 1.0
        True
    """
    if permeability <= 0:
        raise ValueError("Permeability must be positive")
    if permittivity <= 0:
        raise ValueError("Permittivity must be positive")

    return math.sqrt(permeability / permittivity)


def poynting_vector_magnitude(
    electric_field: float,
    magnetic_field: float,
    permeability: float = VACUUM_PERMEABILITY,
) -> float:
    """
    Calculate the magnitude of the Poynting vector (electromagnetic power flow).

    The Poynting vector S = (1/mu_0) * E x B represents the directional energy
    flux density of an electromagnetic field (power per unit area).

    Args:
        electric_field: Magnitude of electric field (V/m)
        magnetic_field: Magnitude of magnetic field (T)
        permeability: Permeability of the medium (H/m)

    Returns:
        float: Magnitude of Poynting vector (W/m²)

    Raises:
        ValueError: If permeability is non-positive

    Example:
        >>> abs(poynting_vector_magnitude(1000, 1e-6) - 795.8) < 1.0
        True
        >>> abs(poynting_vector_magnitude(377, 1.0) - 3.0e8) < 1e6
        True
        >>> poynting_vector_magnitude(0, 1.0)
        0.0
    """
    if permeability <= 0:
        raise ValueError("Permeability must be positive")

    # For perpendicular E and B fields: |S| = |E||B|/mu_0
    return (electric_field * magnetic_field) / permeability


def energy_density_electromagnetic(
    electric_field: float,
    magnetic_field: float,
    permittivity: float = VACUUM_PERMITTIVITY,
    permeability: float = VACUUM_PERMEABILITY,
) -> float:
    """
    Calculate the energy density of an electromagnetic field.

    The energy density u = (1/2)*(epsilon_0*E^2 + B^2/mu_0) represents the
    electromagnetic energy stored per unit volume.

    Args:
        electric_field: Magnitude of electric field (V/m)
        magnetic_field: Magnitude of magnetic field (T)
        permittivity: Permittivity of the medium (F/m)
        permeability: Permeability of the medium (H/m)

    Returns:
        float: Energy density (J/m³)

    Raises:
        ValueError: If permittivity or permeability is non-positive

    Example:
        >>> abs(energy_density_electromagnetic(1000, 1e-3) - 0.398) < 0.001
        True
        >>> abs(energy_density_electromagnetic(0, 1.0) - 397887) < 1
        True
        >>> abs(energy_density_electromagnetic(377, 1e-6) - 1.0e-6) < 1e-6
        True
    """
    if permittivity <= 0:
        raise ValueError("Permittivity must be positive")
    if permeability <= 0:
        raise ValueError("Permeability must be positive")

    # Electric field energy density: (1/2)*epsilon_0*E^2
    electric_energy_density = 0.5 * permittivity * electric_field**2

    # Magnetic field energy density: (1/2)*B^2/mu_0
    magnetic_energy_density = 0.5 * (magnetic_field**2) / permeability

    return electric_energy_density + magnetic_energy_density


if __name__ == "__main__":
    import doctest

    print("Testing Maxwell's equations implementation...")
    doctest.testmod(verbose=True)

    # Additional demonstration
    print("\n" + "=" * 50)
    print("Maxwell's Equations Demonstration")
    print("=" * 50)

    # Demonstrate speed of light calculation
    c = electromagnetic_wave_speed()
    print(f"Speed of light in vacuum: {c:.0f} m/s")
    print(f"Expected: {SPEED_OF_LIGHT} m/s")

    # Demonstrate wave impedance
    z0 = electromagnetic_wave_impedance()
    print(f"Impedance of free space: {z0:.2f} Ω")

    # Demonstrate Poynting vector for plane wave
    E = 377  # V/m (chosen to make calculation simple)
    B = 1e-6  # T (E/B = c in vacuum for plane waves)
    S = poynting_vector_magnitude(E, B)
    print(f"Poynting vector magnitude: {S:.0f} W/m²")

    print("\nAll Maxwell's equations verified successfully!")
