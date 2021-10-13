# KINEMATICS #

# Kinematics is the physics of motion

# Here is an explanation on the "big 4 equations", all of which were used to make this
# algorithm: https://www.physicsclassroom.com/class/1dkin/Lesson-6/Kinematic-Equations

# Output will always be a float, so if you need to round, set r to whatever place you
# are rounding to

# NOTE: Not all of these equations will give you an exactly same answer, but will be
# very close. Typically you would only show sig
# figs when you calculate with these equations.

# Doctests are all tested with initial_velocity=0, final_velocity=104.96,
# initial_position=0, final_position=1720, acceleration=3.2, time_elapsed=32.8,
# retaining_wall=2

# These were calculated by hand so the output for distance is different, but the outputs
# are more accurate than the one used for the example.

# In all cases distance is final_position-initial_position
# TOTAL distance is final_position+initial_position
# If you want to find distance from one point to another assume initial_position=0

# Typing hints
from typing import Union, Optional

# FINDING TIME #


class NotEnoughInfo(Exception):
    pass


# Named "ktime", as in "kinematics time", to prevent clashing and confusion
# between this and the function time()
# retaining_wall is rounding place
def ktime(
    initial_position: Optional[Union[int, float]] = None,
    final_position: Optional[Union[int, float]] = None,
    initial_velocity: Optional[Union[int, float]] = None,
    final_velocity: Optional[Union[int, float]] = None,
    acceleration: Optional[Union[int, float]] = None,
    retaining_wall: Optional[int] = None,
) -> float:
    """
    Return time for given initial_position, final_position, initial_velocity,
    final_velocity, or acceleration.

    :param initial_position: int, float
    :param final_position: int, float
    :param initial_velocity: int, float
    :param final_velocity: int, float
    :param acceleration: int, float
    :param retaining_wall: int
    :return: float

    >>> ktime(initial_velocity=0, final_velocity=104.96, acceleration=3.2,
    ... retaining_wall=2)
    32.8
    >>> ktime(initial_position=0, final_position=1720, initial_velocity=0,
    ... final_velocity=104.96, retaining_wall=2)
    32.77

    The variable 'retaining_wall' can only be an integer.
    >>> ktime(initial_position=0, final_position=1720, initial_velocity=0,
    ... final_velocity=104.96, retaining_wall=True)
    Traceback (most recent call last):
        ...
    ValueError: retaining_wall cannot be type 'bool'

    When not given enough information, you will get an error.
    Ex. Trying to find time without final velocity
    ktime(initial_velocity=0, acceleration=3.2, retaining_wall=2)
    Traceback (most recent call last):
        ...
    NotEnoughInfo: Not enough information to complete calculation.
    """
    # initialze variables so mypy won't give me an error
    acceleration = acceleration
    initial_position = initial_position
    final_position = final_position
    inital_velocity = initial_velocity
    final_velocity = final_velocity
    retaining_wall = retaining_wall
    
    if not acceleration:
        if None in (initial_position, final_position, initial_velocity, final_velocity):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if retaining_wall is not None:
                if type(retaining_wall) != int:
                    raise ValueError(
                        f"retaining_wall cannot be type '{type(retaining_wall).__name__}'"
                    )
                else:
                    return round(
                        float(
                            (2 * (final_position - initial_position))
                            / (final_velocity + initial_velocity)
                        ),
                        retaining_wall,
                    )
            else:
                return float(
                    (2 * (final_position - initial_position))
                    / (final_velocity + initial_velocity)
                )
    else:
        if None in (initial_velocity, final_velocity):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if retaining_wall is not None:
                if type(retaining_wall) != int:
                    raise ValueError(
                        f"retaining_wall cannot be type '{type(retaining_wall).__name__}'"
                    )
                else:
                    return round(
                        float((final_velocity - initial_velocity) / acceleration),
                        retaining_wall,
                    )
            else:
                return float((final_velocity - initial_velocity) / acceleration)
