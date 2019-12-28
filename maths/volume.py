"""
Find Volumes of Various Shapes.

Wikipedia reference: https://en.wikipedia.org/wiki/Volume
"""

from math import pi


def vol_cube(side_length):
    """Calculate the Volume of a Cube."""
    # Cube side_length.
    return float(side_length ** 3)


def vol_cuboid(width, height, length):
    """Calculate the Volume of a Cuboid."""
    # Multiply lengths together.
    return float(width * height * length)


def vol_cone(area_of_base, height):
    """
    Calculate the Volume of a Cone.

    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    volume = (1/3) * area_of_base * height
    """
    return (float(1) / 3) * area_of_base * height


def vol_right_circ_cone(radius, height):
    """
    Calculate the Volume of a Right Circular Cone.

    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    volume = (1/3) * pi * radius^2 * height
    """

    return (float(1) / 3) * pi * (radius ** 2) * height


def vol_prism(area_of_base, height):
    """
    Calculate the Volume of a Prism.

    V = Bh
    Wikipedia reference: https://en.wikipedia.org/wiki/Prism_(geometry)
    """
    return float(area_of_base * height)


def vol_pyramid(area_of_base, height):
    """
    Calculate the Volume of a Prism.

    V = (1/3) * Bh
    Wikipedia reference: https://en.wikipedia.org/wiki/Pyramid_(geometry)
    """
    return (float(1) / 3) * area_of_base * height


def vol_sphere(radius):
    """
    Calculate the Volume of a Sphere.

    V = (4/3) * pi * r^3
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    """
    return (float(4) / 3) * pi * radius ** 3


def vol_circular_cylinder(radius, height):
    """Calculate the Volume of a Circular Cylinder.

    Wikipedia reference: https://en.wikipedia.org/wiki/Cylinder
    volume = pi * radius^2 * height
    """
    return pi * radius ** 2 * height


def main():
    """Print the Results of Various Volume Calculations."""
    print("Volumes:")
    print("Cube: " + str(vol_cube(2)))  # = 8
    print("Cuboid: " + str(vol_cuboid(2, 2, 2)))  # = 8
    print("Cone: " + str(vol_cone(2, 2)))  # ~= 1.33
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2)))  # ~= 8.38
    print("Prism: " + str(vol_prism(2, 2)))  # = 4
    print("Pyramid: " + str(vol_pyramid(2, 2)))  # ~= 1.33
    print("Sphere: " + str(vol_sphere(2)))  # ~= 33.5
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2)))  # ~= 25.1


if __name__ == "__main__":
    main()
