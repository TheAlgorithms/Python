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

# FINDING DISTANCE #

class NotEnoughInfo(Exception):
    pass

def distance(v0=None, v=None, x0=None, a=None, t=None, r=None):
    """
    Find distance for given x0, v0, v, a, or t.
    
    :param v0: int, float
    :param x0: int, float
    :param v: int, float
    :param a: int, float
    :param t: int, float
    :param r: int
    :return: float
    
    >>> distance(v0=0, x0=0, a=3.2, t=32.8, r=2)
    1721.34
    >>> distance(v0=0, v=104.96, x0=0, t=32.8, r=2)
    1721.34
    """
    if not a:
        if None in (x0,v0,v,t):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float(x0+((v+v0)/2)*t), r)
            else:
                return float(x0+((v+v0)/2)*t)
    else:
        if None in (v0,x0,a,t):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float(x0+(v0*t)+((a*(t**2))*0.5)), r)
            else:
                return float(x0+(v0*t)+((a*(t**2))*0.5))
