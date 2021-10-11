# KINEMATICS #

# Kinematics is the physics of motion

# Here is an explanation on the "big 4 equations", all of which were used to make this
# algorithm: https://www.physicsclassroom.com/class/1dkin/Lesson-6/Kinematic-Equations

# Output will always be a float, so if you need to round, set r to whatever place you
# are rounding to

# NOTE: Not all of these equations will give you an exactly same answer, but will be
# very close. Typically you would only show sig
# figs when you calculate with these equations.

# Doctests are all tested with intial_velocity=0, v=104.96, intial_position=0,
# final_position=1720, acceleration=3.2, time_elapsed=32.8, retaining_wall=2
# These were calculated by hand so the output for distance is different, but the outputs
# are more accurate than the one used for the example.

# Typing hints
from typing import Union


# Square root function just so I don't have to import math and it looks cleaner
def sqrt(num: Union[int, float]) -> Union[int, float]:
    if num < 0:
        multiplier = -1
        final_result = abs(num)
    else:
        multiplier = 1
        final_result = num

    return multiplier * (final_result ** 0.5)


# FINDING VELOCITY #


class NotEnoughInfo(Exception):
    pass


def velocity(
    intial_position: Union[int, float] = None,
    final_position: Union[int, float] = None,
    intial_velocity: Union[int, float] = None,
    acceleration: Union[int, float] = None,
    time_elapsed: Union[int, float] = None,
    retaining_wall: int = None,
) -> float:
    """
    Find velocity with given intial_velocity, intial_position, final_position,
    acceleration, or time_elapsed.

    :param intial_velocity: int, float
    :param intial_position: int, float
    :param final_position: int, float
    :param acceleration: int, float
    :param time_elapsed int, float
    :param retaining_wall: int
    :return: float

    >>> velocity(intial_velocity=0, acceleration=3.2, time_elapsed=32.8,
    ... retaining_wall=2)
    104.96
    >>> velocity(intial_velocity=0, intial_position=0, final_position=1720,
    ... time_elapsed=32.8, retaining_wall=2)
    104.88
    >>> velocity(intial_velocity=0, intial_position=0, final_position=1720,
    ... acceleration=3.2, retaining_wall=2)
    104.92

    The variable 'r' can only be an integer.
    >>> velocity(intial_velocity=0, intial_position=0, final_position=1720,
    ... acceleration=3.2, retaining_wall=[2])
    Traceback (most recent call last):
        ...
    ValueError: r cannot be type 'list'

    When not given enough information, you will get an error.
    Ex. Trying to find velocity without initial position, final position
    and time
    >>> velocity(intial_velocity=0, acceleration=3.2, retaining_wall=2)
    Traceback (most recent call last):
        ...
    NotEnoughInfo: Not enough information to complete calculation.
    """
    if not intial_position and not final_position:
        if None in (intial_velocity, acceleration, time_elapsed):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if retaining_wall is not None:
                if type(retaining_wall) != int:
                    raise ValueError(
                        f"r cannot be type '{type(retaining_wall).__name__}'"
                    )
                else:
                    return round(
                        float(intial_velocity + (acceleration * time_elapsed)),
                        retaining_wall,
                    )
            else:
                return float(intial_velocity + (acceleration * time_elapsed))
    else:
        if not acceleration and not time_elapsed:
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if not acceleration:
                if None in (intial_velocity, intial_position, final_position):
                    raise NotEnoughInfo(
                        "Not enough information to complete calculation."
                    )
                else:
                    if retaining_wall is not None:
                        if type(retaining_wall) != int:
                            raise ValueError(
                                f"r cannot be type '{type(retaining_wall).__name__}'"
                            )
                        else:
                            return round(
                                float(
                                    (
                                        (
                                            (final_position - intial_position)
                                            / time_elapsed
                                        )
                                        * 2
                                    )
                                    - intial_velocity
                                ),
                                retaining_wall,
                            )
                    else:
                        return float(
                            (((final_position - intial_position) / time_elapsed) * 2)
                            - intial_velocity
                        )
            else:
                if None in (intial_velocity, intial_position, final_position):
                    raise NotEnoughInfo(
                        "Not enough information to complete calculation."
                    )
                else:
                    solution = intial_velocity ** 2 + (
                        2 * acceleration * (final_position - intial_position)
                    )
                    final_result = sqrt(solution)
                    if retaining_wall is not None:
                        if type(retaining_wall) != int:
                            raise ValueError(
                                f"r cannot be type '{type(retaining_wall).__name__}'"
                            )
                        else:
                            return round(float(final_result), retaining_wall)
                    else:
                        return float(final_result)
