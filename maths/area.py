"""
Çeşitli geometrik şekillerin alanını bulun
Wikipedia referansı: https://en.wikipedia.org/wiki/Area
"""

#Organised by K. Umut Araz

from math import pi, sqrt, tan


def yüzey_alani_küp(kenar_uzunluğu: float) -> float:
    """
    Bir küpün yüzey alanını hesaplayın.

    >>> yüzey_alani_küp(1)
    6
    >>> yüzey_alani_küp(1.6)
    15.360000000000003
    >>> yüzey_alani_küp(0)
    0
    >>> yüzey_alani_küp(3)
    54
    >>> yüzey_alani_küp(-1)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_küp() sadece negatif olmayan değerleri kabul eder
    """
    if kenar_uzunluğu < 0:
        raise ValueError("yüzey_alani_küp() sadece negatif olmayan değerleri kabul eder")
    return 6 * kenar_uzunluğu**2


def yüzey_alani_dikdörtgenler_prizmasi(uzunluk: float, genişlik: float, yükseklik: float) -> float:
    """
    Bir dikdörtgenler prizmasının yüzey alanını hesaplayın.

    >>> yüzey_alani_dikdörtgenler_prizmasi(1, 2, 3)
    22
    >>> yüzey_alani_dikdörtgenler_prizmasi(0, 0, 0)
    0
    >>> yüzey_alani_dikdörtgenler_prizmasi(1.6, 2.6, 3.6)
    38.56
    >>> yüzey_alani_dikdörtgenler_prizmasi(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_dikdörtgenler_prizmasi() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_dikdörtgenler_prizmasi(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_dikdörtgenler_prizmasi() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_dikdörtgenler_prizmasi(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_dikdörtgenler_prizmasi() sadece negatif olmayan değerleri kabul eder
    """
    if uzunluk < 0 or genişlik < 0 or yükseklik < 0:
        raise ValueError("yüzey_alani_dikdörtgenler_prizmasi() sadece negatif olmayan değerleri kabul eder")
    return 2 * ((uzunluk * genişlik) + (genişlik * yükseklik) + (uzunluk * yükseklik))


def yüzey_alani_küre(yarıçap: float) -> float:
    """
    Bir kürenin yüzey alanını hesaplayın.
    Wikipedia referansı: https://en.wikipedia.org/wiki/Sphere
    Formül: 4 * pi * r^2

    >>> yüzey_alani_küre(5)
    314.1592653589793
    >>> yüzey_alani_küre(1)
    12.566370614359172
    >>> yüzey_alani_küre(1.6)
    32.169908772759484
    >>> yüzey_alani_küre(0)
    0.0
    >>> yüzey_alani_küre(-1)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_küre() sadece negatif olmayan değerleri kabul eder
    """
    if yarıçap < 0:
        raise ValueError("yüzey_alani_küre() sadece negatif olmayan değerleri kabul eder")
    return 4 * pi * yarıçap**2


def yüzey_alani_yarım_küre(yarıçap: float) -> float:
    """
    Bir yarım kürenin yüzey alanını hesaplayın.
    Formül: 3 * pi * r^2

    >>> yüzey_alani_yarım_küre(5)
    235.61944901923448
    >>> yüzey_alani_yarım_küre(1)
    9.42477796076938
    >>> yüzey_alani_yarım_küre(0)
    0.0
    >>> yüzey_alani_yarım_küre(1.1)
    11.40398133253095
    >>> yüzey_alani_yarım_küre(-1)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_yarım_küre() sadece negatif olmayan değerleri kabul eder
    """
    if yarıçap < 0:
        raise ValueError("yüzey_alani_yarım_küre() sadece negatif olmayan değerleri kabul eder")
    return 3 * pi * yarıçap**2


def yüzey_alani_koni(yarıçap: float, yükseklik: float) -> float:
    """
    Bir koninin yüzey alanını hesaplayın.
    Wikipedia referansı: https://en.wikipedia.org/wiki/Cone
    Formül: pi * r * (r + (h ** 2 + r ** 2) ** 0.5)

    >>> yüzey_alani_koni(10, 24)
    1130.9733552923256
    >>> yüzey_alani_koni(6, 8)
    301.59289474462014
    >>> yüzey_alani_koni(1.6, 2.6)
    23.387862992395807
    >>> yüzey_alani_koni(0, 0)
    0.0
    >>> yüzey_alani_koni(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_koni() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_koni(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_koni() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_koni(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_koni() sadece negatif olmayan değerleri kabul eder
    """
    if yarıçap < 0 or yükseklik < 0:
        raise ValueError("yüzey_alani_koni() sadece negatif olmayan değerleri kabul eder")
    return pi * yarıçap * (yarıçap + (yükseklik**2 + yarıçap**2) ** 0.5)


def yüzey_alani_konik_kesit(
    yarıçap_1: float, yarıçap_2: float, yükseklik: float
) -> float:
    """
    Bir konik kesitin yüzey alanını hesaplayın.

    >>> yüzey_alani_konik_kesit(1, 2, 3)
    45.511728065337266
    >>> yüzey_alani_konik_kesit(4, 5, 6)
    300.7913575056268
    >>> yüzey_alani_konik_kesit(0, 0, 0)
    0.0
    >>> yüzey_alani_konik_kesit(1.6, 2.6, 3.6)
    78.57907060751548
    >>> yüzey_alani_konik_kesit(-1, 2, 3)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_konik_kesit() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_konik_kesit(1, -2, 3)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_konik_kesit() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_konik_kesit(1, 2, -3)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_konik_kesit() sadece negatif olmayan değerleri kabul eder
    """
    if yarıçap_1 < 0 or yarıçap_2 < 0 or yükseklik < 0:
        raise ValueError(
            "yüzey_alani_konik_kesit() sadece negatif olmayan değerleri kabul eder"
        )
    eğik_yükseklik = (yükseklik**2 + (yarıçap_1 - yarıçap_2) ** 2) ** 0.5
    return pi * ((eğik_yükseklik * (yarıçap_1 + yarıçap_2)) + yarıçap_1**2 + yarıçap_2**2)


def yüzey_alani_silindir(yarıçap: float, yükseklik: float) -> float:
    """
    Bir silindirin yüzey alanını hesaplayın.
    Wikipedia referansı: https://en.wikipedia.org/wiki/Cylinder
    Formül: 2 * pi * r * (h + r)

    >>> yüzey_alani_silindir(7, 10)
    747.6990515543707
    >>> yüzey_alani_silindir(1.6, 2.6)
    42.22300526424682
    >>> yüzey_alani_silindir(0, 0)
    0.0
    >>> yüzey_alani_silindir(6, 8)
    527.7875658030853
    >>> yüzey_alani_silindir(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_silindir() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_silindir(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_silindir() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_silindir(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_silindir() sadece negatif olmayan değerleri kabul eder
    """
    if yarıçap < 0 or yükseklik < 0:
        raise ValueError("yüzey_alani_silindir() sadece negatif olmayan değerleri kabul eder")
    return 2 * pi * yarıçap * (yükseklik + yarıçap)


def yüzey_alani_torus(torus_yarıçapı: float, tüp_yarıçapı: float) -> float:
    """Bir torusun yüzey alanını hesaplayın.
    Wikipedia referansı: https://en.wikipedia.org/wiki/Torus
    :return 4pi^2 * torus_yarıçapı * tüp_yarıçapı
    >>> yüzey_alani_torus(1, 1)
    39.47841760435743
    >>> yüzey_alani_torus(4, 3)
    473.7410112522892
    >>> yüzey_alani_torus(3, 4)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_torus() iğne veya kendi kendine kesişen torusları desteklemez
    >>> yüzey_alani_torus(1.6, 1.6)
    101.06474906715503
    >>> yüzey_alani_torus(0, 0)
    0.0
    >>> yüzey_alani_torus(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_torus() sadece negatif olmayan değerleri kabul eder
    >>> yüzey_alani_torus(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: yüzey_alani_torus() sadece negatif olmayan değerleri kabul eder
    """
    if torus_yarıçapı < 0 or tüp_yarıçapı < 0:
        raise ValueError("yüzey_alani_torus() sadece negatif olmayan değerleri kabul eder")
    if torus_yarıçapı < tüp_yarıçapı:
        raise ValueError(
            "yüzey_alani_torus() iğne veya kendi kendine kesişen torusları desteklemez"
        )
    return 4 * pow(pi, 2) * torus_yarıçapı * tüp_yarıçapı


def alan_dikdörtgen(uzunluk: float, genişlik: float) -> float:
    """
    Bir dikdörtgenin alanını hesaplayın.

    >>> alan_dikdörtgen(10, 20)
    200
    >>> alan_dikdörtgen(1.6, 2.6)
    4.16
    >>> alan_dikdörtgen(0, 0)
    0
    >>> alan_dikdörtgen(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: alan_dikdörtgen() sadece negatif olmayan değerleri kabul eder
    >>> alan_dikdörtgen(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: alan_dikdörtgen() sadece negatif olmayan değerleri kabul eder
    >>> alan_dikdörtgen(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: alan_dikdörtgen() sadece negatif olmayan değerleri kabul eder
    """
    if uzunluk < 0 or genişlik < 0:
        raise ValueError("alan_dikdörtgen() sadece negatif olmayan değerleri kabul eder")
    return uzunluk * genişlik


def alan_kare(kenar_uzunluğu: float) -> float:
    """
    Bir karenin alanını hesaplayın.

    >>> alan_kare(10)
    100
    >>> alan_kare(0)
    0
    >>> alan_kare(1.6)
    2.5600000000000005
    >>> alan_kare(-1)
    Traceback (most recent call last):
        ...
    ValueError: alan_kare() sadece negatif olmayan değerleri kabul eder
    """
    if kenar_uzunluğu < 0:
        raise ValueError("alan_kare() sadece negatif olmayan değerleri kabul eder")
    return kenar_uzunluğu**2


def alan_üçgen(tabani: float, yükseklik: float) -> float:
    """
    Taban ve yükseklik verilen bir üçgenin alanını hesaplayın.

    >>> alan_üçgen(10, 10)
    50.0
    >>> alan_üçgen(1.6, 2.6)
    2.08
    >>> alan_üçgen(0, 0)
    0.0
    >>> alan_üçgen(-1, -2)
    Traceback (most recent call last):
        ...
    ValueError: alan_üçgen() sadece negatif olmayan değerleri kabul eder
    >>> alan_üçgen(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: alan_üçgen() sadece negatif olmayan değerleri kabul eder
    >>> alan_üçgen(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: alan_üçgen() sadece negatif olmayan değerleri kabul eder
    """
    if tabani < 0 or yükseklik < 0:
        raise ValueError("alan_üçgen() sadece negatif olmayan değerleri kabul eder")
    return (tabani * yükseklik) / 2


def alan_üçgen_üç_kenar(kenar1: float, kenar2: float, kenar3: float) -> float:
    """
    Üç kenar uzunluğu bilinen bir üçgenin alanını hesaplayın.
    Bu fonksiyon Heron formülünü kullanır: https://en.wikipedia.org/wiki/Heron%27s_formula

    >>> alan_üçgen_üç_kenar(5, 12, 13)
    30.0
    >>> alan_üçgen_üç_kenar(10, 11, 12)
    51.521233486786784
    >>> alan_üçgen_üç_kenar(0, 0, 0)
    0.0
    >>> alan_üçgen_üç_kenar(1.6, 2.6, 3.6)
    1.8703742940919619
    >>> alan_üçgen_üç_kenar(-1, -2, -1)
    Traceback (most recent call last):
        ...
    ValueError: alan_üçgen_üç_kenar() sadece negatif olmayan değerleri kabul eder
    >>> alan_üçgen_üç_kenar(1, -2, 1)
    Traceback (most recent call last):
        ...
    ValueError: alan_üçgen_üç_kenar() sadece negatif olmayan değerleri kabul eder
    >>> alan_üçgen_üç_kenar(2, 4, 7)
    Traceback (most recent call last):
        ...
    ValueError: Verilen üç kenar bir üçgen oluşturmaz
    >>> alan_üçgen_üç_kenar(2, 7, 4)
    Traceback (most recent call last):
        ...
    ValueError: Verilen üç kenar bir üçgen oluşturmaz
    >>> alan_üçgen_üç_kenar(7, 2, 4)
    Traceback (most recent call last):
        ...
    ValueError: Verilen üç kenar bir üçgen oluşturmaz
    """
    if kenar1 < 0 or kenar2 < 0 or kenar3 < 0:
    if kenar1 < 0 veya kenar2 < 0 veya kenar3 < 0:
        raise ValueError("alan_üçgen_üç_kenar() sadece negatif olmayan değerleri kabul eder")
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
