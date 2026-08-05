"""
In electrical engineering, the Y-Δ transform, also written wye-delta and also known by
many other names, is a mathematical technique to simplify the analysis of an electrical
network.
The name derives from the shapes of the circuit diagrams, which look respectively like
the letter Y and the Greek capital letter Δ. This circuit transformation theory was
published by Arthur Edwin Kennelly in 1899. It is widely used in analysis of three-phase
electric power circuits.

The Y-Δ transform can be considered a special case of the star-mesh transform for three
resistors. In mathematics, the Y-Δ transform plays an important role in theory of
circular planar graphs.

Source: https://en.wikipedia.org/wiki/Y-%CE%94_transform
"""

from sys import exit
from unittest import mock


def delta_to_wye(resistors: list) -> dict:
    """
    >>> delta_to_wye([2.0, 3.0, 4.0])
    {'r1': 1.3333333333333333, 'r2': 0.8888888888888888, 'r3': 0.6666666666666666}
    """
    r_wye: dict = {}
    ra, rb, rc = resistors[0], resistors[1], resistors[2]
    r_wye.update({"r1": rb * rc / (ra + rb + rc)})
    r_wye.update({"r2": ra * rc / (ra + rb + rc)})
    r_wye.update({"r3": ra * rb / (ra + rb + rc)})
    return r_wye


def wye_to_delta(resistors: list) -> dict:
    """
    >>> wye_to_delta([2.0, 3.0, 4.0])
    {'ra': 13.0, 'rb': 8.666666666666666, 'rc': 6.5}
    """
    r1, r2, r3 = resistors[0], resistors[1], resistors[2]
    r_delta: dict = {}
    r_delta.update({"ra": (r1 * r2 + r2 * r3 + r3 * r1) / r1})
    r_delta.update({"rb": (r1 * r2 + r2 * r3 + r3 * r1) / r2})
    r_delta.update({"rc": (r1 * r2 + r2 * r3 + r3 * r1) / r3})
    return r_delta


def transform(mode: int, resistors: list) -> dict:
    """
    >>> transform(1, [4.0, 5.0, 6.0])
    {'r1': 2.0, 'r2': 1.6, 'r3': 1.3333333333333333}

    >>> transform(2, [4.0, 5.0, 6.0])
    {'ra': 18.5, 'rb': 14.8, 'rc': 12.333333333333334}
    """
    r_transformed = {}
    if mode == 1:
        r_transformed = delta_to_wye(resistors)
    elif mode == 2:
        r_transformed = wye_to_delta(resistors)
    return r_transformed


def get_type_transform() -> int:
    mode: int = 0
    try:
        print("""
        1. From delta to wye
        2. From wye to delta
        """)
        mode = int(input("? --> "))
    except ValueError:
        print("Invalid Value. Only int inputs are accepted")
        exit()
    return mode


def get_resistors_values(mode: int) -> list:
    r: list = []
    print("Select conversion (type 1 or 2)")
    try:
        if mode == 1:
            r = list(
                map(
                    float, input("Resistant values (format ra rb rc): ").strip().split()
                )
            )[:3]
        elif mode == 2:
            r = list(
                map(
                    float, input("Resistant values (format r1 r2 r3): ").strip().split()
                )
            )[:3]
        else:
            print("Incorrect selected option. Valid option 1 or 2")
    except ValueError:
        print("Invalid Value. Only int inputs are accepted")
        exit()
    return r


def test_get_type_transformation() -> None:
    with mock.patch("builtins.input", return_value="1"):
        m = get_type_transform()
        assert m == 1


def test_get_resistors_values() -> None:
    with mock.patch("builtins.input", return_value="2 4 8"):
        r = get_resistors_values(2)
        assert r == [2.0, 4.0, 8.0]


def main() -> None:
    print("star - delta transform")
    mode = get_type_transform()
    r = get_resistors_values(mode)
    r_transformed = transform(mode, r)
    print(f"Result: '{r_transformed}'")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    main()
