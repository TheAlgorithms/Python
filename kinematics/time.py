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

# FINDING TIME #

class NotEnoughInfo(Exception):
    pass

# Named "ktime", as in "kinematics time", to prevent clashing and confusion between this and the function time()
def ktime(x0=None, x=None, v0=None, v=None, a=None, r=None):
    """
    Return time for given x0, x, v0, v, or a.
    
    :param x0: int, float
    :param x: int, float
    :param v0: int, float
    :param v: int, float
    :param a: int, float
    :param r: int
    :return: float
    
    >>> ktime(v0=0, v=104.96, a=3.2, r=2)
    32.8
    >>> ktime(x0=0, x=1720, v0=0, v=104.96, r=2)
    32.77
    """
    if not a:
        if None in (x0,x,v0,v):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float((2*(x-x0))/(v+v0)), r)
            else:
                return float((2*(x-x0))/(v+v0))
    else:
        if None in (v0,v,a):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float((v-v0)/a), r)
            else:
                return float((v-v0)/a)
