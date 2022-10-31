# dodecahedron.py

"""
A regular dodecahedron is a three-dimensional figure made up of
12 pentagon faces having the same equal size.
"""


def dodecahedron_surface_area(edge: float) -> float:
    """
    Calculates the surface area of a regular dodecahedron
    a = 3 * ((25 + 10 * (5** (1 / 2))) ** (1 / 2 )) * (e**2)
    where:
    a --> is the area of the dodecahedron
    e --> is the length of the edge
    reference-->"Dodecahedron" Study.com
    <https://study.com/academy/lesson/dodecahedron-volume-surface-area-formulas.html>

    :param edge: length of the edge of the dodecahedron
    :type edge: float
    :return: the surface area of the dodecahedron as a float


    Tests:
    >>> dodecahedron_surface_area(5)
    516.1432201766901
    >>> dodecahedron_surface_area(10)
    2064.5728807067603
    >>> dodecahedron_surface_area(-1)
    Traceback (most recent call last):
      ...
    ValueError: Length must be a positive.
    """

    if edge <= 0 or not isinstance(edge, int):
        raise ValueError("Length must be a positive.")
    return 3 * ((25 + 10 * (5 ** (1 / 2))) ** (1 / 2)) * (edge**2)


def dodecahedron_volume(edge: float) -> float:
    """
    Calculates the volume of a regular dodecahedron
    v = ((15 + (7 * (5** (1 / 2)))) / 4) * (e**3)
    where:
    v --> is the volume of the dodecahedron
    e --> is the length of the edge
    reference-->"Dodecahedron" Study.com
    <https://study.com/academy/lesson/dodecahedron-volume-surface-area-formulas.html>

    :param edge: length of the edge of the dodecahedron
    :type edge: float
    :return: the volume of the dodecahedron as a float

    Tests:
    >>> dodecahedron_volume(5)
    957.8898700780791
    >>> dodecahedron_volume(10)
    7663.118960624633
    >>> dodecahedron_volume(-1)
    Traceback (most recent call last):
      ...
    ValueError: Length must be a positive.
    """

    if edge <= 0 or not isinstance(edge, int):
        raise ValueError("Length must be a positive.")
    return ((15 + (7 * (5 ** (1 / 2)))) / 4) * (edge**3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
