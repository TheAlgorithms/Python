"""
Collision types and final velocities are central to physics.
This module computes final velocities for inelastic and elastic collisions.
It also classifies the collision type from initial and final velocities.

Description: Collisions happen when two masses interact head-on.
There are two types: inelastic and elastic. In inelastic collisions, the
masses stick together and share one final velocity. In elastic collisions,
momentum and kinetic energy are conserved, and masses rebound.
Momentum is mass times velocity; kinetic energy is 1/2 mv^2.
The collision type comes from comparing initial and final momentum and
kinetic energy of the system.

Reference: https://en.wikipedia.org/wiki/Collision
"""


def inelastic_collisions(
    mass1: float, mass2: float, velocity1: float, velocity2: float
) -> float:
    """Calculate final velocity after a perfectly inelastic collision.

    The two objects stick together and share a common final velocity.

    Parameters:
        mass1: Mass of the first object.
        mass2: Mass of the second object.
        velocity1: Initial velocity of the first object.
        velocity2: Initial velocity of the second object.

    Returns:
        The final combined velocity of the two objects.

    Examples:
        >>> inelastic_collisions(2.0, 3.0, 5.0, 6.0)
        5.6
        >>> inelastic_collisions(9.0, 8.1, -3.2, 3.1)
        -0.22
    """
    initial_momentum = (mass1 * velocity1) + (mass2 * velocity2)
    total_mass = mass2 + mass1
    final_velocity = round((initial_momentum / total_mass), 2)

    return final_velocity


def elastic_collisions(
    mass1: float, mass2: float, velocity1: float, velocity2: float
) -> str:
    """Calculate final velocities after a perfectly elastic collision.

    The collision is head-on and conserves both momentum and kinetic energy.

    Parameters:
        mass1: Mass of the first object.
        mass2: Mass of the second object.
        velocity1: Initial velocity of the first object.
        velocity2: Initial velocity of the second object.

    Returns:
        A formatted string containing the final velocities of both objects.

    Examples:
        >>> elastic_collisions(1.0, 2.0, -3.0, -1.0)
        '-0.34 ; -2.34'
        >>> elastic_collisions(9.0, 8.1, -3.2, 3.1)
        '2.76 ; -3.54'
    """
    com_velocity = inelastic_collisions(mass1, mass2, velocity1, velocity2)
    initial_velocities = [velocity1, velocity2]
    final_velocities = []

    for vel in initial_velocities:
        new_vel = -1 * (vel - com_velocity)
        final_vel = com_velocity + new_vel
        final_velocities.append(round(final_vel, 2))

    return f"{final_velocities[0]} ; {final_velocities[1]}"


def type_collision(
    mass1: float,
    mass2: float,
    velocity_initial1: float,
    velocity_initial2: float,
    velocity_final1: float,
    velocity_final2: float,
) -> str:
    """Determine the collision type from initial and final velocities.

    Compares initial and final momentum and kinetic energy to classify the collision.

    Parameters:
        mass1: Mass of the first object.
        mass2: Mass of the second object.
        velocity_initial1: Initial velocity of the first object.
        velocity_initial2: Initial velocity of the second object.
        velocity_final1: Final velocity of the first object.
        velocity_final2: Final velocity of the second object.

    Returns:
        A string describing the collision type.

    Examples:
        >>> type_collision(1.0, 1.0, 2.0, 3.0, 2.0, 3.0)
        'Perfectly Elastic Collision'
        >>> type_collision(1.0, 1.0, 2.0, 3.0, 2.5, 2.5)
        'Perfectly Inelastic Collision'
        >>> type_collision(1.0, 1.0, 2.0, 3.0, 0.0, 0.0)
        'Inelastic Collision'
    """
    momentum_initial = (mass1 * velocity_initial1) + (mass2 * velocity_initial2)
    momentum_final = (mass1 * velocity_final1) + (mass2 * velocity_final2)
    kinetic_initial = 0.5 * (
        (mass1 * velocity_initial1**2) + (mass2 * velocity_initial2**2)
    )
    kinetic_final = 0.5 * ((mass1 * velocity_final1**2) + (mass2 * velocity_final2**2))

    if kinetic_final == kinetic_initial and momentum_initial == momentum_final:
        return f"Perfectly Elastic Collision"
    elif not (kinetic_final == kinetic_initial) and momentum_initial == momentum_final:
        return f"Perfectly Inelastic Collision"
    else:
        return "Inelastic Collision"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
