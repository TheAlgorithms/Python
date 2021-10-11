# KINEMATICS #

# Kinematics is the physics of motion

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

class NotEnoughInfo(Exception):
    pass

def acceleration(v0=None, v=None, x=None, x0=None, t=None, r=None):
    if not t:
        if not v0 or not v or not x0 or not x:
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type {type(r)}")
                else:
                    return round(float((v**2-v0**2)/(2*(x-x0))), r)
            else:
                return float((v**2-v0**2)/(2*(x-x0)))
    else:
        if not v0 or not v or not t:
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type {type(r)}")
                else:
                    return round(float((v-v0)/t), r)
            else:
                return float((v-v0)/t)
