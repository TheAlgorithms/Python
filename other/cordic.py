# CORDIC algorithm info: https://en.wikipedia.org/wiki/CORDIC

from enum import Enum

SHIFT = 16
SHIFT_BASE = 65536

# (1/scale_factor) which scale factor is Π(cos(arctan(2^-i)))
SCALE_CONSTANT = 1.64676

#  The elementary angles for the lookup table. They correspond to
#  arctan(2^-i) and then shifted left by 8 bits in an integer format
ELEM_ANGLE = [
    2949120,
    1740967,
    919789,
    466945,
    234379,
    117304,
    58666,
    29335,
    14668,
    7334,
    3667,
    1833,
    917,
    458,
    229,
    115,
    57,
    29,
    14,
    7,
    4,
    2,
    1,
]


class CordicMode(Enum):
    ROTATION = 0
    VECTOR = 1


class Cordic:
    @staticmethod
    def cos_cordic(theta: int) -> float:
        """
        Calculate cosine for theta in degrees.
        >>> round(Cordic.cos_cordic(60), 4)
        0.5
        >>> round(Cordic.cos_cordic(45), 4)
        0.7071
        >>> round(Cordic.cos_cordic(20), 4)
        0.9397
        """
        return (
            Cordic.fixed_to_float(Cordic.cordic(1, 0, theta, CordicMode.ROTATION)["x"])
            / SCALE_CONSTANT
        )

    @staticmethod
    def sin_cordic(theta: int) -> float:
        """
        Calculate sine for theta in degrees.
        >>> round(Cordic.sin_cordic(65), 4)
        0.9063
        >>> round(Cordic.sin_cordic(45), 4)
        0.7071
        >>> round(Cordic.sin_cordic(30), 4)
        0.5
        """
        return (
            Cordic.fixed_to_float(Cordic.cordic(1, 0, theta, CordicMode.ROTATION)["y"])
            / SCALE_CONSTANT
        )

    @staticmethod
    def arctan_div_cordic(x: int, y: int) -> float:
        """
        Calculate inverse tangent and returns theta in degrees.
        >>> round(Cordic.arctan_div_cordic(4, 5), 4)    # Arctan(5/4)
        51.3416
        """
        return Cordic.fixed_to_float(Cordic.cordic(x, y, 0, CordicMode.VECTOR)["z"])

    @staticmethod
    def arctan_cordic(y: int) -> float:
        """
        Calculate inverse tangent and returns theta in degrees.
        >>> round(Cordic.arctan_cordic(2), 4)    # Arctan(2)
        63.4361
        """
        return Cordic.fixed_to_float(Cordic.cordic(1, y, 0, CordicMode.VECTOR)["z"])

    @staticmethod
    def rot_decision(mode: CordicMode, value: int) -> bool:
        """
        The function will return the flag if we are in rotation mode,
        and the opposite if we are in vector mode. This is because rotation
        mode runs if (z < 0) whereas vector mode runs if (y >= 0)
        """
        if value < 0:
            flag = True
        else:
            flag = False

        if mode == CordicMode.ROTATION:
            return flag
        else:
            return not flag

    @staticmethod
    def cordic(x: int, y: int, z: int, mode: CordicMode) -> dict:
        """
        Cordic in rotation mode. The only difference between this and cordic
        vector mode is the if condition in the for loop. x and y are shifted
        to the left by 8 to give it better precision, but proper fixed point
        arithmetic hasn't been implemented.
        x: The x coordinate in the vector.
        y: The y coordinate in the vector.
        z: The angle accumulator. Reaches 0 after n iterations

        Cordic in vector mode. The only difference
        is the condiition in the middle of the for loop. Need
        to make everything in fixed point arithmetic.
        x: The x coordinate of the vector.
        y: The y coordinate of the vector. Reaches 0 after n iterations.
        z: The angle accumulator. Reaches z[0] + arctan(y[0]/x[0]) after n iterations.
        """
        x = x << SHIFT
        y = y << SHIFT
        z = z << SHIFT

        for i in range(len(ELEM_ANGLE)):
            x_temp = x
            # If the mode is rotation, our check for rotation direction
            # is on the z value, but if it is in vector, it is on the y value.
            if mode == CordicMode.ROTATION:
                flag = Cordic.rot_decision(mode, z)
            else:
                flag = Cordic.rot_decision(mode, y)

            if flag:
                x = x + (y >> i)
                y = y - (x_temp >> i)
                z = z + ELEM_ANGLE[i]
            else:
                x = x - (y >> i)
                y = y + (x_temp >> i)
                z = z - ELEM_ANGLE[i]

        result = {"x": x, "y": y, "z": z}
        return result

    @staticmethod
    def fixed_to_float(fixed: int) -> float:
        return fixed / SHIFT_BASE

    @staticmethod
    def float_to_fixed(flt: float) -> int:
        return int(flt * SHIFT_BASE)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
