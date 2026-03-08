"""
Find the area of various geometric shapes
Wikipedia reference: https://en.wikipedia.org/wiki/Area
"""

from math import pi, sqrt, tan


def surface_area_cube(side_length: float) -> float:
    """
    Calculate the Surface Area of a Cube.

    >>> surface_area_cube(1)
    6
    >>> surface_area_cube(1.6)
    15.360000000000003
    >>> surface_area_cube(0)
    0
    >>> surface_area_cube(3)
    54
    >>> surface_area_cube(-1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cube() only accepts non-negative values
    """
    if side_length < 0:
        raise ValueError("surface_area_cube() only accepts non-negative values")
    return 6 * side_length**2


def surface_area_cuboid(length: float, breadth: float, height: float) -> float:
    """
    Calculate the Surface Area of a Cuboid.

    >>> surface_area_cuboid(1, 2, 3)
    22
    >>> surface_area_cuboid(0, 0, 0)
    0
    >>> surface_area_cuboid(1.6, 2.6, 3.6)
    38.56
    >>> surface_area_cuboid(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cuboid() only accepts non-negative values
    >>> surface_area_cuboid(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cuboid() only accepts non-negative values
    >>> surface_area_cuboid(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cuboid() only accepts non-negative values
    """
    if length < 0 or breadth < 0 or height < 0:
        raise ValueError("surface_area_cuboid() only accepts non-negative values")
    return 2 * ((length * breadth) + (breadth * height) + (length * height))


def surface_area_sphere(radius: float) -> float:
    """
    Calculate the Surface Area of a Sphere.
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    Formula: 4 * pi * r^2

    >>> surface_area_sphere(5)
    314.1592653589793
    >>> surface_area_sphere(1)
    12.566370614359172
    >>> surface_area_sphere(1.6)
    32.169908772759484
    >>> surface_area_sphere(0)
    0.0
    >>> surface_area_sphere(-1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_sphere() only accepts non-negative values
    """
    if radius < 0:
        raise ValueError("surface_area_sphere() only accepts non-negative values")
    return 4 * pi * radius**2


def surface_area_hemisphere(radius: float) -> float:
    """
    Calculate the Surface Area of a Hemisphere.
    Formula: 3 * pi * r^2

    >>> surface_area_hemisphere(5)
    235.61944901923448
    >>> surface_area_hemisphere(1)
    9.42477796076938
    >>> surface_area_hemisphere(0)
    0.0
    >>> surface_area_hemisphere(1.1)
    11.40398133253095
    >>> surface_area_hemisphere(-1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_hemisphere() only accepts non-negative values
    """
    if radius < 0:
        raise ValueError("surface_area_hemisphere() only accepts non-negative values")
    return 3 * pi * radius**2


def surface_area_cone(radius: float, height: float) -> float:
    """
    Calculate the Surface Area of a Cone.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    Formula: pi * r * (r + (h ** 2 + r ** 2) ** 0.5)

    >>> surface_area_cone(10, 24)
    1130.9733552923256
    >>> surface_area_cone(6, 8)
    301.59289474462014
    >>> surface_area_cone(1.6, 2.6)
    23.387862992395807
    >>> surface_area_cone(0, 0)
    0.0
    >>> surface_area_cone(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cone() only accepts non-negative values
    >>> surface_area_cone(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cone() only accepts non-negative values
    >>> surface_area_cone(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cone() only accepts non-negative values
    """
    if radius < 0 or height < 0:
        raise ValueError("surface_area_cone() only accepts non-negative values")
    return pi * radius * (radius + (height**2 + radius**2) ** 0.5)


def surface_area_conical_frustum(
    radius_1: float, radius_2: float, height: float
) -> float:
    """
    Calculate the Surface Area of a Conical Frustum.

    >>> surface_area_conical_frustum(1, 2, 3)
    45.511728065337266
    >>> surface_area_conical_frustum(4, 5, 6)
    300.7913575056268
    >>> surface_area_conical_frustum(0, 0, 0)
    0.0
    >>> surface_area_conical_frustum(1.6, 2.6, 3.6)
    78.57907060751548
    >>> surface_area_conical_frustum(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_conical_frustum() only accepts non-negative values
    >>> surface_area_conical_frustum(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_conical_frustum() only accepts non-negative values
    >>> surface_area_conical_frustum(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_conical_frustum() only accepts non-negative values
    """
    if radius_1 < 0 or radius_2 < 0 or height < 0:
        raise ValueError(
            "surface_area_conical_frustum() only accepts non-negative values"
        )
    slant_height = (height**2 + (radius_1 - radius_2) ** 2) ** 0.5
    return pi * ((slant_height * (radius_1 + radius_2)) + radius_1**2 + radius_2**2)


def surface_area_cylinder(radius: float, height: float) -> float:
    """
    Calculate the Surface Area of a Cylinder.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cylinder
    Formula: 2 * pi * r * (h + r)

    >>> surface_area_cylinder(7, 10)
    747.6990515543707
    >>> surface_area_cylinder(1.6, 2.6)
    42.22300526424682
    >>> surface_area_cylinder(0, 0)
    0.0
    >>> surface_area_cylinder(6, 8)
    527.7875658030853
    >>> surface_area_cylinder(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cylinder() only accepts non-negative values
    >>> surface_area_cylinder(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cylinder() only accepts non-negative values
    >>> surface_area_cylinder(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_cylinder() only accepts non-negative values
    """
    if radius < 0 or height < 0:
        raise ValueError("surface_area_cylinder() only accepts non-negative values")
    return 2 * pi * radius * (height + radius)


def surface_area_torus(torus_radius: float, tube_radius: float) -> float:
    """Calculate the Area of a Torus.
    Wikipedia reference: https://en.wikipedia.org/wiki/Torus
    :return 4pi^2 * torus_radius * tube_radius
    >>> surface_area_torus(1, 1)
    39.47841760435743
    >>> surface_area_torus(4, 3)
    473.7410112522892
    >>> surface_area_torus(3, 4)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_torus() does not support spindle or self intersecting tori
    >>> surface_area_torus(1.6, 1.6)
    101.06474906715503
    >>> surface_area_torus(0, 0)
    0.0
    >>> surface_area_torus(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_torus() only accepts non-negative values
    >>> surface_area_torus(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: surface_area_torus() only accepts non-negative values
    """
    if torus_radius < 0 or tube_radius < 0:
        raise ValueError("surface_area_torus() only accepts non-negative values")
    if torus_radius < tube_radius:
        raise ValueError(
            "surface_area_torus() does not support spindle or self intersecting tori"
        )
    return 4 * pow(pi, 2) * torus_radius * tube_radius


def area_rectangle(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    >>> area_rectangle(10, 20)
    200
    >>> area_rectangle(1.6, 2.6)
    4.16
    >>> area_rectangle(0, 0)
    0
    >>> area_rectangle(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_rectangle() only accepts non-negative values
    >>> area_rectangle(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_rectangle() only accepts non-negative values
    >>> area_rectangle(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_rectangle() only accepts non-negative values
    """
    if length < 0 or width < 0:
        raise ValueError("area_rectangle() only accepts non-negative values")
    return length * width


def area_square(side_length: float) -> float:
    """
    Calculate the area of a square.

    >>> area_square(10)
    100
    >>> area_square(0)
    0
    >>> area_square(1.6)
    2.5600000000000005
    >>> area_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: area_square() only accepts non-negative values
    """
    if side_length < 0:
        raise ValueError("area_square() only accepts non-negative values")
    return side_length**2


def area_triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle given the base and height.

    >>> area_triangle(10, 10)
    50.0
    >>> area_triangle(1.6, 2.6)
    2.08
    >>> area_triangle(0, 0)
    0.0
    >>> area_triangle(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle() only accepts non-negative values
    >>> area_triangle(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle() only accepts non-negative values
    >>> area_triangle(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle() only accepts non-negative values
    """
    if base < 0 or height < 0:
        raise ValueError("area_triangle() only accepts non-negative values")
    return (base * height) / 2


def area_triangle_three_sides(side1: float, side2: float, side3: float) -> float:
    """
    Calculate area of triangle when the length of 3 sides are known.
    This function uses Heron's formula: https://en.wikipedia.org/wiki/Heron%27s_formula

    >>> area_triangle_three_sides(5, 12, 13)
    30.0
    >>> area_triangle_three_sides(10, 11, 12)
    51.521233486786784
    >>> area_triangle_three_sides(0, 0, 0)
    0.0
    >>> area_triangle_three_sides(1.6, 2.6, 3.6)
    1.8703742940919619
    >>> area_triangle_three_sides(-1, -2, -1)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle_three_sides() only accepts non-negative values
    >>> area_triangle_three_sides(1, -2, 1)
    Traceback (most recent call last):
        ...
    ValueError: area_triangle_three_sides() only accepts non-negative values
    >>> area_triangle_three_sides(2, 4, 7)
    Traceback (most recent call last):
        ...
    ValueError: Given three sides do not form a triangle
    >>> area_triangle_three_sides(2, 7, 4)
    Traceback (most recent call last):
        ...
    ValueError: Given three sides do not form a triangle
    >>> area_triangle_three_sides(7, 2, 4)
    Traceback (most recent call last):
        ...
    ValueError: Given three sides do not form a triangle
    """
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("area_triangle_three_sides() only accepts non-negative values")
    elif side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        raise ValueError("Given three sides do not form a triangle")
    semi_perimeter = (side1 + side2 + side3) / 2
    area = sqrt(
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    )
    return area


def area_parallelogram(base: float, height: float) -> float:
    """
    Calculate the area of a parallelogram.

    >>> area_parallelogram(10, 20)
    200
    >>> area_parallelogram(1.6, 2.6)
    4.16
    >>> area_parallelogram(0, 0)
    0
    >>> area_parallelogram(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_parallelogram() only accepts non-negative values
    >>> area_parallelogram(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_parallelogram() only accepts non-negative values
    >>> area_parallelogram(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_parallelogram() only accepts non-negative values
    """
    if base < 0 or height < 0:
        raise ValueError("area_parallelogram() only accepts non-negative values")
    return base * height


def area_trapezium(base1: float, base2: float, height: float) -> float:
    """
    Calculate the area of a trapezium.

    >>> area_trapezium(10, 20, 30)
    450.0
    >>> area_trapezium(1.6, 2.6, 3.6)
    7.5600000000000005
    >>> area_trapezium(0, 0, 0)
    0.0
    >>> area_trapezium(-1, -2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(-1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(1, -2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    >>> area_trapezium(-1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: area_trapezium() only accepts non-negative values
    """
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("area_trapezium() only accepts non-negative values")
    return 1 / 2 * (base1 + base2) * height


def area_circle(radius: float) -> float:
    """
    Calculate the area of a circle.

    >>> area_circle(20)
    1256.6370614359173
    >>> area_circle(1.6)
    8.042477193189871
    >>> area_circle(0)
    0.0
    >>> area_circle(-1)
    Traceback (most recent call last):
        ...
    ValueError: area_circle() only accepts non-negative values
    """
    if radius < 0:
        raise ValueError("area_circle() only accepts non-negative values")
    return pi * radius**2


def area_ellipse(radius_x: float, radius_y: float) -> float:
    """
    Calculate the area of a ellipse.

    >>> area_ellipse(10, 10)
    314.1592653589793
    >>> area_ellipse(10, 20)
    628.3185307179587
    >>> area_ellipse(0, 0)
    0.0
    >>> area_ellipse(1.6, 2.6)
    13.06902543893354
    >>> area_ellipse(-10, 20)
    Traceback (most recent call last):
        ...
    ValueError: area_ellipse() only accepts non-negative values
    >>> area_ellipse(10, -20)
    Traceback (most recent call last):
        ...
    ValueError: area_ellipse() only accepts non-negative values
    >>> area_ellipse(-10, -20)
    Traceback (most recent call last):
        ...
    ValueError: area_ellipse() only accepts non-negative values
    """
    if radius_x < 0 or radius_y < 0:
        raise ValueError("area_ellipse() only accepts non-negative values")
    return pi * radius_x * radius_y


def area_rhombus(diagonal_1: float, diagonal_2: float) -> float:
    """
    Calculate the area of a rhombus.

    >>> area_rhombus(10, 20)
    100.0
    >>> area_rhombus(1.6, 2.6)
    2.08
    >>> area_rhombus(0, 0)
    0.0
    >>> area_rhombus(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_rhombus() only accepts non-negative values
    >>> area_rhombus(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_rhombus() only accepts non-negative values
    >>> area_rhombus(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_rhombus() only accepts non-negative values
    """
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError("area_rhombus() only accepts non-negative values")
    return 1 / 2 * diagonal_1 * diagonal_2


def area_reg_polygon(sides: int, length: float) -> float:
    """
    Calculate the area of a regular polygon.
    Wikipedia reference: https://en.wikipedia.org/wiki/Polygon#Regular_polygons
    Formula: (n*s^2*cot(pi/n))/4

    >>> area_reg_polygon(3, 10)
    43.301270189221945
    >>> area_reg_polygon(4, 10)
    100.00000000000001
    >>> area_reg_polygon(0, 0)
    Traceback (most recent call last):
        ...
    ValueError: area_reg_polygon() only accepts integers greater than or equal to \
three as number of sides
    >>> area_reg_polygon(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_reg_polygon() only accepts integers greater than or equal to \
three as number of sides
    >>> area_reg_polygon(5, -2)
    Traceback (most recent call last):
        ...
    ValueError: area_reg_polygon() only accepts non-negative values as \
length of a side
    >>> area_reg_polygon(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: area_reg_polygon() only accepts integers greater than or equal to \
three as number of sides
    """
    if not isinstance(sides, int) or sides < 3:
        raise ValueError(
            "area_reg_polygon() only accepts integers greater than or \
equal to three as number of sides"
        )
    elif length < 0:
        raise ValueError(
            "area_reg_polygon() only accepts non-negative values as \
length of a side"
        )
    return (sides * length**2) / (4 * tan(pi / sides))
    return (sides * length**2) / (4 * tan(pi / sides))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # verbose so we can see methods missing tests

    print("[DEMO] Areas of various geometric shapes: \n")
    print(f"Rectangle: {area_rectangle(10, 20) = }")
    print(f"Square: {area_square(10) = }")
    print(f"Triangle: {area_triangle(10, 10) = }")
    print(f"Triangle: {area_triangle_three_sides(5, 12, 13) = }")
    print(f"Parallelogram: {area_parallelogram(10, 20) = }")
    print(f"Rhombus: {area_rhombus(10, 20) = }")
    print(f"Trapezium: {area_trapezium(10, 20, 30) = }")
    print(f"Circle: {area_circle(20) = }")
    print(f"Ellipse: {area_ellipse(10, 20) = }")
    print("\nSurface Areas of various geometric shapes: \n")
    print(f"Cube: {surface_area_cube(20) = }")
    print(f"Cuboid: {surface_area_cuboid(10, 20, 30) = }")
    print(f"Sphere: {surface_area_sphere(20) = }")
    print(f"Hemisphere: {surface_area_hemisphere(20) = }")
    print(f"Cone: {surface_area_cone(10, 20) = }")
    print(f"Conical Frustum: {surface_area_conical_frustum(10, 20, 30) = }")
    print(f"Cylinder: {surface_area_cylinder(10, 20) = }")
    print(f"Torus: {surface_area_torus(20, 10) = }")
    print(f"Equilateral Triangle: {area_reg_polygon(3, 10) = }")
    print(f"Square: {area_reg_polygon(4, 10) = }")
    print(f"Reqular Pentagon: {area_reg_polygon(5, 10) = }")
