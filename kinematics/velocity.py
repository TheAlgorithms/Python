# KINEMATICS #

# Kinematics is the physics of motion

# Here is an explanation on the "big 4 equations", all of which were used to make this
# algorithm: https://www.physicsclassroom.com/class/1dkin/Lesson-6/Kinematic-Equations

# These are how we represent specific values when calculating using kinematic equations
# x0 = Initial Position
# x = Final Postion
# v0 = Intial Velocity
# v = Final Velocity
# a = acceleration
# t = time

# r = rounding place

# Output will always be a float, so if you need to round, set r to whatever place you 
# are rounding to

# NOTE: Not all of these equations will give you an exactly same answer, but will be 
# very close. Typically you would only show sig 
# figs when you calculate with these equations.

# Doctests are all tested with v0=0, v=104.96, x0=0, x=1720, a=3.2, t=32.8, r=2
# These were calculated by hand so the output for distance is different, but the outputs 
# are more accurate than the one used for the example.

# Typing hints
from typing import Union

# Square root function just so I don't have to import math and it looks cleaner
def sqrt(num):
    if num < 0:
        multiplier = -1
        final_result = abs(num)
    else:
        multiplier = 1
        final_result = num
        
    return multiplier*(final_result**0.5)

# FINDING VELOCITY #

class NotEnoughInfo(Exception):
    pass
  
def velocity(x0: Union[int,float] = None, x: Union[int,float] = None, 
v0: Union[int,float] = None, a: Union[int,float] = None, 
t: Union[int,float] = None, r: int = None) -> float:
    """
    Find velocity with given v0, x0, x, a, or t.
    
    :param v0: int, float
    :param x0: int, float
    :param x: int, float
    :param a: int, float
    :param t: int, float
    :param r: int
    :return: float
    
    >>> velocity(v0=0, a=3.2, t=32.8, r=2)
    104.96
    >>> velocity(v0=0, x0=0, x=1720, t=32.8, r=2)
    104.88
    >>> velocity(v0=0, x0=0, x=1720, a=3.2, r=2)
    104.92
    
    The variable 'r' can only be an integer.
    >>> velocity(v0=0, x0=0, x=1720, a=3.2, r=[2])
    Traceback (most recent call last):
        ...
    ValueError: r cannot be type 'list'
    
    When not given enough information, you will get an error.
    Ex. Trying to find velocity without initial position, final position
    and time
    >>> velocity(v0=0, a=3.2, r=2)
    Traceback (most recent call last):
        ...
    NotEnoughInfo: Not enough information to complete calculation.
    """
    if not x0 and not x:
        if None in (v0,a,t):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float(v0+(a*t)), r)
            else:
                return float(v0+(a*t))
    else:
        if not a and not t:
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if not a:
                if None in (v0,x0,x):
                    raise NotEnoughInfo("Not enough information to complete calculation.")
                else:
                    if r is not None:
                        if type(r) != int:
                            raise ValueError(f"r cannot be type '{type(r).__name__}'")
                        else:
                            return round(float((((x-x0)/t)*2)-v0), r)
                    else:
                        return float((((x-x0)/t)*2)-v0)
            else:
                if None in (v0,x0,x):
                    raise NotEnoughInfo("Not enough information to complete calculation.")
                else:
                    solution = v0**2+(2*a*(x-x0))
                    final_result = sqrt(solution)
                    if r is not None:
                        if type(r) != int:
                            raise ValueError(f"r cannot be type '{type(r).__name__}'")
                        else:
                            return round(float(final_result), r)
                    else:
                        return float(final_result)
