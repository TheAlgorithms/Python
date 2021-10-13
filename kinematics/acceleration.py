# KINEMATICS #

# Kinematics is the physics of motion

# Here is an explanation on the "big 4 equations", all of which were used to make this
# algorithm: https://www.physicsclassroom.com/class/1dkin/Lesson-6/Kinematic-Equations

# Output will always be a float, so if you need to round, set retaining_wall to
# whatever place you are rounding to

# NOTE: Not all of these equations will give you an exactly same answer, but will be
# very close. Typically you would only show sig
# figs when you calculate with these equations.

# Doctests are all tested with initial_velocity=0, final_velocity=104.96,
# initial_position=0, final_position=1720, acceleration=3.2,
# time_elapsed=32.8, retaining_wall=2

# These were calculated by hand so the output for distance is different, but the outputs
# are more accurate than the one used for the example.

# In all cases distance is final_position-initial_position
# TOTAL distance is final_position+initial_position
# If you want to find distance from one point to another assume initial_position=0

# Typing hints
from typing import Union, Optional

# FINDING ACCELERATION


class NotEnoughInfo(Exception):
    pass


# retaining_wall is the rounding place
def acceleration(
    initial_velocity: Optional[Union[int, float]] = None,
    final_velocity: Optional[Union[int, float]] = None,
    final_position: Optional[Union[int, float]] = None,
    initial_position: Optional[Union[int, float]] = None,
    time_elapsed: Optional[Union[int, float]] = None,
    retaining_wall: Optional[int] = None,
) -> float:
    """
    Find acceleration for given initial_position, final_position, initial_velocity,
    final_velocity, or time_elapsed.

    :param initial_position: int, float
    :param final_position: int, float
    :param initial_velocity: int, float
    :param final_velocity: int, float
    :param time_elapsed: int, float
    :param retaining_wall: int
    :return: float

    >>> acceleration(initial_position=0, final_position=1720, initial_velocity=0,
    ... final_velocity=104.96, retaining_wall=2)
    3.2
    >>> acceleration(initial_velocity=0, final_velocity=104.96, time_elapsed=32.8,
    ... retaining_wall=2)
    3.2

    The variable 'retaining_wall' can only be an integer.
    >>> acceleration(initial_velocity=0, final_velocity=104.96, time_elapsed=32.8,
    ... retaining_wall=2.1)
    Traceback (most recent call last):
        ...
    ValueError: retaining_wall cannot be type 'float'

    When not given enough information, you will get an error.
    Ex. Trying to find acceleration with final velocity and time only
    >>> acceleration(final_velocity=104.96, time_elapsed=32.8, retaining_wall=2)
    Traceback (most recent call last):
        ...
    NotEnoughInfo: Not enough information to complete calculation.
    """
    # intializing variables so mypy won't give me an error
    initial_velocity = initial_velocity
    final_velocity = final_velocity
    final_position = final_position
    initial_position = initial_position
    time_elapsed = time_elapsed
    retaining_wall = retaining_wall
    
    if not time_elapsed:
        if None in (initial_velocity, final_velocity, final_position, initial_position):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if retaining_wall is not None:
                if type(retaining_wall) != int:
                    raise ValueError(
                        f"retaining_wall cannot be type {type(retaining_wall).__name__}"
                    )
                else:
                    return round(
                        float(
                            (final_velocity**2 - initial_velocity**2)
                            / (2 * (final_position - initial_position))
                        ),
                        retaining_wall
                    )
            else:
                return float(
                    (final_velocity**2 - initial_velocity**2)
                    / (2 * (final_position - initial_position))
                )
    else:
        if None in (initial_velocity, final_velocity, time_elapsed):
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
                            (final_velocity - initial_velocity)
                            / time_elapsed
                        ),
                        retaining_wall
                    )
            else:
                return float(
                    (final_velocity - initial_velocity)
                    / time_elapsed
                )
