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

# FINDING ACCELERATION

class NotEnoughInfo(Exception):
    pass

def acceleration(v0=None, v=None, x=None, x0=None, t=None, r=None):
    """
    Find acceleration for given x0, x, v0, v, or t.
    
    :param x0: int, float
    :param x: int, float
    :param v0: int, float
    :param v: int, float
    :param t: int, float
    :param r: int
    :return: float
    
    >>> acceleration(x0=0, x=1720, v0=0, v=104.96, r=2)
    3.2
    >>> acceleration(v0=0, v=104.96, t=32.8, r=2)
    3.2
    """
    if not t:
        if None in (v0,v,x,x0):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type {type(r).__name__}")
                else:
                    return round(float((v**2-v0**2)/(2*(x-x0))), r)
            else:
                return float((v**2-v0**2)/(2*(x-x0)))
    else:
        if None in (v0,v,t):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float((v-v0)/t), r)
            else:
                return float((v-v0)/t)
