from math import pi


def arc(angle: int, radius: int) -> float:
    """
    >>> arc(45, 5)
    3.9269908169872414
    >>> arc(120, 15)
    31.415926535897928
    """
    return 2 * pi * radius * (angle / 360)


if __name__ == "__main__":
    print(arc(90, 10))
