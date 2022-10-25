 

import math
def arc(angle: int, rad: int) -> float:
    """
    >>> arc(45, 5)
    3.9269908169872414
    >>> arc(120, 15)
    31.415926535897928
    """
    pi = math.pi

    return 2 * pi * rad * (angle / 360)


if __name__ == "__main__":
    angle = 90
    rad = 10
    print(f"The length of the arc with radius {rad} and a central angle of {angle} degrees is {arc(angle, rad)}")
