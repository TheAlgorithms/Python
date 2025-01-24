def manhattan_distance(point_a: list, point_b: list) -> float:
    """
    Expectts two list of numbers representing two points in the same
    n-dimensional space

    https://en.wikipedia.org/wiki/Taxicab_geometry

    >>> manhattan_distance([1,1], [2,2])
    2.0
    >>> manhattan_distance([1.5,1.5], [2,2])
    1.0
    >>> manhattan_distance([1.5,1.5], [2.5,2])
    1.5
    >>> manhattan_distance([-3, -3, -3], [0, 0, 0])
    9.0
    >>> manhattan_distance([1,1], None)
    Traceback (most recent call last):
        ...
    ValueError: Missing an input
    >>> manhattan_distance([1,1], [2, 2, 2])
    Traceback (most recent call last):
        ...
    ValueError: Both points must be in the same n-dimensional space
    >>> manhattan_distance([1,"one"], [2, 2, 2])
    Traceback (most recent call last):
        ...
    TypeError: Expected a list of numbers as input, found str
    >>> manhattan_distance(1, [2, 2, 2])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found int
    >>> manhattan_distance([1,1], "not_a_list")
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    """

    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")

    return float(sum(abs(a - b) for a, b in zip(point_a, point_b)))


def _validate_point(point: list[float]) -> None:
    """
    >>> _validate_point(None)
    Traceback (most recent call last):
         ...
    ValueError: Missing an input
    >>> _validate_point([1,"one"])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    >>> _validate_point(1)
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found int
    >>> _validate_point("not_a_list")
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    """
    if point:
        if isinstance(point, list):
            for item in point:
                if not isinstance(item, (int, float)):
                    msg = (
                        "Expected a list of numbers as input, found "
                        f"{type(item).__name__}"
                    )
                    raise TypeError(msg)
        else:
            msg = f"Expected a list of numbers as input, found {type(point).__name__}"
            raise TypeError(msg)
    else:
        raise ValueError("Missing an input")


def manhattan_distance_one_liner(point_a: list, point_b: list) -> float:
    """
    Version with one liner

    >>> manhattan_distance_one_liner([1,1], [2,2])
    2.0
    >>> manhattan_distance_one_liner([1.5,1.5], [2,2])
    1.0
    >>> manhattan_distance_one_liner([1.5,1.5], [2.5,2])
    1.5
    >>> manhattan_distance_one_liner([-3, -3, -3], [0, 0, 0])
    9.0
    >>> manhattan_distance_one_liner([1,1], None)
    Traceback (most recent call last):
         ...
    ValueError: Missing an input
    >>> manhattan_distance_one_liner([1,1], [2, 2, 2])
    Traceback (most recent call last):
         ...
    ValueError: Both points must be in the same n-dimensional space
    >>> manhattan_distance_one_liner([1,"one"], [2, 2, 2])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    >>> manhattan_distance_one_liner(1, [2, 2, 2])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found int
    >>> manhattan_distance_one_liner([1,1], "not_a_list")
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    """

    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")

    return float(sum(abs(x - y) for x, y in zip(point_a, point_b)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
