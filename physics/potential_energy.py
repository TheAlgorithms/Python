from scipy.constants import g

"""
Finding the gravitational potential energy of an object with reference
to the earth,by taking its mass and height above the ground as input.

Description : Potential energy is stored energy that depends on the
position or configuration of objects within a force field. It can be
released as kinetic energy when the objects move under that force.

Gravitational potential energy is the energy an object has because of
its position in a gravitational field. It is the potential energy a
massive object has in relation to another massive object due to gravity.
This energy is associated with the gravitational field and is released
when the objects fall toward each other. Near the Earth's surface this
potential energy is approximately proportional to mass, gravity, and
height, so it is often written as U = mgh for a body close to Earth.

Spring potential energy is the stored energy in an elastic spring when
it is compressed or stretched from its rest length. For small deformations,
it is proportional to the square of the displacement from equilibrium.

For two point particles interacting pairwise, the gravitational potential
energy U is given by
U=-GMm/R
where M and m are the masses of the two particles, R is the distance
between them, and G is the gravitational constant.

Reference : "https://en.m.wikipedia.org/wiki/Gravitational_energy"
"""


def gravitational_potential_energy(mass: float, height: float) -> float:
    """
    Function calculates the gravitational potential energy of an object.

    Parameters:
        mass: Mass of the object
        height: Height the object is at

    Returns:
        The value of energy in Joules
    
    Complexity:
        Time Complexity: O(1) - Constant execution time for evaluation logic.
        Space Complexity: O(1) - Constant memory allocation.   

    Examples:
        >>> gravitational_potential_energy(10,10)
        980.665
        >>> gravitational_potential_energy(0,5)
        0.0
        >>> gravitational_potential_energy(8,0)
        0.0
        >>> gravitational_potential_energy(10,5)
        490.3325
        >>> gravitational_potential_energy(0,0)
        0.0
        >>> gravitational_potential_energy(2,8)
        156.9064
        >>> gravitational_potential_energy(20,100)
        19613.3
    """
    if mass < 0:
        # handling of negative values of mass
        raise ValueError("The mass of a body cannot be negative")
    if height < 0:
        # handling of negative values of height
        raise ValueError("The height above the ground cannot be negative")

    return mass * g * height

def spring_potential_energy(spr_con: float, dspl: float) -> float:
    """
    Function calculates the spring potential energy of an object.

    Parameters:
        spr_con: The spring constant of a spring
        dspl: The length of the displacement of the spring

    Returns:
        The value of energy in Joules
    
    Complexity:
        Time Complexity: O(1) - Constant execution time for evaluation logic.
        Space Complexity: O(1) - Constant memory allocation.   

    Examples:
        >>> spring_potential_energy(100,2)
        200.0
        >>> spring_potential_energy(10,0.5)
        1.25
        >>> spring_potential_energy(8,0)
        0.0
        >>> spring_potential_energy(14.6,8)
        467.2
        >>> spring_potential_energy(17,4.5)
        172.125
    """
    if spr_con < 0  :
        raise ValueError("The values for spring_constant cannot be negative")
    
    return 0.5 * spr_con * (dspl ** 2)



if __name__ == "__main__":
    from doctest import testmod
    print(spring_potential_energy(17,4.5))
    testmod(name="gravitational_potential_energy")
