"""
The Energy-Mass Equivalence Law, as formulated by Albert Einstein's theory of special relativity, states that the energy (E) of an object is directly proportional to its mass (m) and the square of the speed of light (c),
represented by the famous equation:
E=mc²

In this equation:
E represents energy in joules (J).
m represents mass in kilograms (kg).
c is the speed of light in a vacuum, approximately 299,792,458 meters per second (m/s).
This groundbreaking concept reveals that mass and energy are interchangeable, and a small amount of mass can yield an immense amount of energy, as demonstrated in nuclear reactions like those in the sun and nuclear bombs.

"""

c_const = 299792458


def energy_mass(mass: float):
    if mass <= 0:
        raise ValueError("Invalid inputs. Enter positive value for mass")

    return mass * (c_const ^ 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
