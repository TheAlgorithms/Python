from math import pi


def arc_length(angle: int, diameter: int) -> float:
    """
    >>> arc_length(45, 5)
    1.9634954084936207
    >>> arc_length(120, 15)
    15.707963267948964
    >>> arc_length(90, 10)
    7.853981633974483
    """
    return pi * diameter * (angle / 360)


if __name__ == "__main__":
    print(arc_length(90, 10))
