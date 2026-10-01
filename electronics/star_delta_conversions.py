# https://www.electrical4u.com/delta-star-transformation-star-delta-transformation/#:~:text=The%20relation%20of%20delta%20%E2%80%93%20star,of%20the%20delta%20connected%20resistances.
# https://en.wikipedia.org/wiki/Y-%CE%94_transform


def star_to_delta(
    impedance_a: complex,
    impedance_b: complex,
    impedance_c: complex,
) -> list[complex]:
    """

    Convert's star impedance arrangement to delta

    Examples:
    1.) Impedance with resistances and zero reactance
    >>> star_to_delta(complex(2,0),complex(1,0),complex(1,0))
    [(2.5+0j), (5+0j), (5+0j)]

    2.) Impedance with resistance and reactance
    >>> star_to_delta(complex(2,0),complex(1,2),complex(1,6))
    [(-3.5+12j), (8.2+7.6j), (3.702702702702702+1.7837837837837838j)]

    3.) Zero impedance
    >>> star_to_delta(complex(0,0),complex(1,2),complex(1,6))
    Traceback (most recent call last):
       ...
    ValueError: entered impedance value is zero

    4.) Negative resistance
    >>> star_to_delta(complex(12,0),complex(-1,2),complex(1,6))
    Traceback (most recent call last):
       ...
    ValueError: entered resistance value is negative
    """

    if abs(impedance_a) == 0 or abs(impedance_b) == 0 or abs(impedance_c) == 0:
        raise ValueError("entered impedance value is zero")

    if impedance_a.real < 0 or impedance_b.real < 0 or impedance_c.real < 0:
        raise ValueError("entered resistance value is negative")

    delta_arrangement = []
    impedance_chain = (
        impedance_a * impedance_b
        + impedance_b * impedance_c
        + impedance_c * impedance_a
    )
    delta_arrangement.append(impedance_chain / impedance_a)
    delta_arrangement.append(impedance_chain / impedance_b)
    delta_arrangement.append(impedance_chain / impedance_c)

    return delta_arrangement


def delta_to_star(
    impedance_a: complex,
    impedance_b: complex,
    impedance_c: complex,
) -> list[complex]:
    """

    Convert's delta impedance arrangement to star

    Examples:
    1.) Impedance with resistances and zero reactance
    >>> delta_to_star(complex(3,0),complex(5,0),complex(7,0))
    [(2.3333333333333335+0j), (1.4+0j), (1+0j)]

    2.) Impedance with resistance and reactance
    >>> delta_to_star(complex(1,3),complex(2,0),complex(0,-3))
    [-2j, (3-1j), (0.6666666666666666+2j)]

    3.) Zero impedance
    >>> delta_to_star(complex(0,0),complex(1,2),complex(1,6))
    Traceback (most recent call last):
      ...
    ValueError: entered impedance value is zero

    4.) Negative resistance
    >>> delta_to_star(complex(12,0),complex(-1,2),complex(1,6))
    Traceback (most recent call last):
      ...
    ValueError: entered resistance value is negative
    """
    if abs(impedance_a) == 0 or abs(impedance_b) == 0 or abs(impedance_c) == 0:
        raise ValueError("entered impedance value is zero")

    if impedance_a.real < 0 or impedance_b.real < 0 or impedance_c.real < 0:
        raise ValueError("entered resistance value is negative")

    star_arrangement = []
    impedance_sum = impedance_a + impedance_b + impedance_c
    star_arrangement.append((impedance_b * impedance_c) / impedance_sum)
    star_arrangement.append((impedance_c * impedance_a) / impedance_sum)
    star_arrangement.append((impedance_a * impedance_b) / impedance_sum)

    return star_arrangement


if __name__ == "__main__":
    import doctest

    doctest.testmod()
