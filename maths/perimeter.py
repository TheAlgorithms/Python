"""
Done and sourced by https://github.com/gobmj
Find the perimeter of various geometric shapes
"""
from math import pi, sqrt


def perimeter_cube(side_length: float) -> float:
    if side_length < 0:
        raise ValueError("perimeter_cube() only accepts non-negative values")
    return 12 * side_length


def perimeter_cuboid(length: float, breadth: float, height: float) -> float:
    if length < 0 or breadth < 0 or height < 0:
        raise ValueError("perimeter_cuboid() only accepts non-negative values")
    return 4 * (length + breadth + height)


def circumference_sphere(radius: float) -> float:
    if radius < 0:
        raise ValueError("circumference_sphere() only accepts non-negative values")
    return pi * 2 * radius


def perimeter_hemisphere(radius: float) -> float:
    if radius < 0:
        raise ValueError("perimeter_hemisphere() only accepts non-negative values")
    return pi * radius


def perimeter_cone(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("perimeter_cone() only accepts non-negative values")
    return 2 * pi * radius


def perimeter_cylinder(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("perimeter_cylinder() only accepts non-negative values")
    return pi * 2 * radius


def perimeter_rectangle(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("perimeter_rectangle() only accepts non-negative values")
    return 2 * (length + width)


def perimeter_square(side_length: float) -> float:
    if side_length < 0:
        raise ValueError("perimeter_square() only accepts non-negative values")
    return 4 * side_length


def perimeter_triangle(side1: float, side2: float, side3: float) -> float:
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError(
            "perimeter_triangle_three_sides() only accepts non-negative values"
        )
    elif side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        raise ValueError("Given three sides do not form a triangle")
    return side1 + side2 + side3


def perimeter_parallelogram(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("perimeter_parallelogram() only accepts non-negative values")
    return base * height


def perimeter_trapezium(base1: float, base2: float, height: float) -> float:
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("perimeter_trapezium() only accepts non-negative values")
    return 2 * (base1 + base2)


def perimeter_circle(radius: float) -> float:
    if radius < 0:
        raise ValueError("perimeter_circle() only accepts non-negative values")
    return 2 * pi * radius


def perimeter_rhombus(diagonal_1: float, diagonal_2: float) -> float:
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError("perimeter_rhombus() only accepts non-negative values")
    return 2 * sqrt(pow(diagonal_1, 2) + pow(diagonal_2, 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # verbose so we can see methods missing tests

    print("[DEMO] Perimiter of various geometric shapes: \n")
    print(f"Rectangle: {perimeter_rectangle(10, 20) = }")
    print(f"Square: {perimeter_square(10) = }")
    print(f"Triangle: {perimeter_triangle(5, 12, 13) = }")
    print(f"Parallelogram: {perimeter_parallelogram(10, 20) = }")
    print(f"Rhombus: {perimeter_rhombus(10, 20) = }")
    print(f"Trapezium: {perimeter_trapezium(10, 20, 30) = }")
    print(f"Circle: {perimeter_circle(20) = }")
    print(f"Cube: {perimeter_cube(20) = }")
    print(f"Cuboid: {perimeter_cuboid(10, 20, 30) = }")
    print(f"Sphere: {circumference_sphere(20) = }")
    print(f"Hemisphere: {perimeter_hemisphere(20) = }")
    print(f"Cone: {perimeter_cone(10, 20) = }")
    print(f"Cylinder: {perimeter_cylinder(10, 20) = }")
