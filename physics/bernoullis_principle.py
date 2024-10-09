"""
Title: Bernoulli's Principle Implementation

Description:
This Python script implements Bernoulli's Principle, which describes the behavior of
a fluid under varying conditions of pressure, velocity, and height. Bernoulli's equation
is applied to an incompressible, frictionless fluid to calculate the unknown variable
(pressure, velocity, or height) when the others are known.

Bernoulli's Equation:
P1 + 0.5 * ρ * v1^2 + ρ * g * h1 = P2 + 0.5 * ρ * v2^2 + ρ * g * h2

Where:
- P1, P2 are pressures at points 1 and 2 (in Pascals),
- v1, v2 are velocities at points 1 and 2 (in m/s),
- h1, h2 are heights at points 1 and 2 (in meters),
- ρ is the fluid density (in kg/m³, default is 1000 for water),
- g is the acceleration due to gravity (default is 9.81 m/s²).

The function `bernoullis_principle` calculates one unknown variable based on inputs and returns the result.
"""


def bernoullis_principle(P1, v1, h1, P2=None, v2=None, h2=None, density=1000, g=9.81):
    """
    Apply Bernoulli's Principle to calculate unknown variables.

    Parameters:
    P1 : float -> Pressure at point 1 (in Pascals)
    v1 : float -> Velocity at point 1 (in m/s)
    h1 : float -> Height at point 1 (in meters)
    P2 : float -> Pressure at point 2 (in Pascals) (optional)
    v2 : float -> Velocity at point 2 (in m/s) (optional)
    h2 : float -> Height at point 2 (in meters) (optional)
    density : float -> Fluid density (in kg/m^3) (default is 1000 for water)
    g : float -> Acceleration due to gravity (default is 9.81 m/s²)

    Returns:
    - If one unknown is provided (P2, v2, or h2), the function calculates the missing value.
    """

    if P2 is None:
        # Calculate Pressure at point 2 (P2)
        P2 = P1 + 0.5 * density * (v1**2 - v2**2) + density * g * (h1 - h2)
        return P2
    elif v2 is None:
        # Calculate Velocity at point 2 (v2)
        v2 = ((2 * (P1 - P2 + density * g * (h1 - h2))) / density + v1**2) ** 0.5
        return v2
    elif h2 is None:
        # Calculate Height at point 2 (h2)
        h2 = h1 + (P1 - P2 + 0.5 * density * (v1**2 - v2**2)) / (density * g)
        return h2
    else:
        return "Please provide at least one unknown (P2, v2, or h2)."


# Example Usage
# Given: P1 = 101325 Pa, v1 = 5 m/s, h1 = 10 m, v2 = 10 m/s, h2 = 5 m
P1 = 101325  # Pressure at point 1 in Pascals
v1 = 5  # Velocity at point 1 in m/s
h1 = 10  # Height at point 1 in meters
v2 = 10  # Velocity at point 2 in m/s
h2 = 5  # Height at point 2 in meters

# Calculate pressure at point 2 (P2)
P2 = bernoullis_principle(P1, v1, h1, v2=v2, h2=h2)
print(f"Pressure at point 2: {P2} Pascals")
