"""
Some of the more common equations associated with fluids and fluid dynamics.
"""

# Acceleration Constant on Earth (unit m/s^2)
g = 9.80665

def buoyantForce(fluidDensity:float, volume:float, gravity:float=g) -> float:
    """
    Calculates buoyant force on object submerged within static fluid
    Args:
        fluidDensity: density of fluid (kg/m^3)
        volume: volume of object / liquid being displaced by object
        gravity: gravitational force on system. Default is Earth Gravity
    returns:
        buoyant force on object in Newtons
    """

    if fluidDensity<=0:
        raise ValueError("Impossible fluid density")
    if volume<0:
        raise ValueError("Impossible Object volume")
    if gravity<=0:
        raise ValueError("Impossible Gravity")

    return fluidDensity * gravity * volume



if __name__ == "__main__":
