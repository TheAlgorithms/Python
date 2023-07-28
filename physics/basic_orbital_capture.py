from math import pow, sqrt

from scipy.constants import G, c, pi

"""
These two functions will return the radii of impact for a target object
of mass M and radius R as well as it's effective cross sectional area σ(sigma).
That is to say any projectile with velocity v passing within σ, will impact the
target object with mass M. The derivation of which is given at the bottom
of this file.

The derivation shows that a projectile does not need to aim directly at the target
body in order to hit it, as  R_capture>R_target. Astronomers refer to the effective
cross section for capture as σ=π*R_capture**2.

This algorithm does not account for an N-body problem.

"""


def capture_radii(
    target_body_radius: float, target_body_mass: float, projectile_velocity: float
) -> float:
    """
    Input Params:
    -------------
    target_body_radius: Radius of the central body SI units: meters | m
    target_body_mass: Mass of the central body SI units: kilograms | kg
    projectile_velocity: Velocity of object moving toward central body
        SI units: meters/second | m/s
    Returns:
    --------
    >>> capture_radii(6.957e8, 1.99e30, 25000.0)
    17209590691.0
    >>> capture_radii(-6.957e8, 1.99e30, 25000.0)
    Traceback (most recent call last):
        ...
    ValueError: Radius cannot be less than 0
    >>> capture_radii(6.957e8, -1.99e30, 25000.0)
    Traceback (most recent call last):
        ...
    ValueError: Mass cannot be less than 0
    >>> capture_radii(6.957e8, 1.99e30, c+1)
    Traceback (most recent call last):
        ...
    ValueError: Cannot go beyond speed of light

    Returned SI units:
    ------------------
    meters | m
    """

    if target_body_mass < 0:
        raise ValueError("Mass cannot be less than 0")
    if target_body_radius < 0:
        raise ValueError("Radius cannot be less than 0")
    if projectile_velocity > c:
        raise ValueError("Cannot go beyond speed of light")

    escape_velocity_squared = (2 * G * target_body_mass) / target_body_radius
    capture_radius = target_body_radius * sqrt(
        1 + escape_velocity_squared / pow(projectile_velocity, 2)
    )
    return round(capture_radius, 0)


def capture_area(capture_radius: float) -> float:
    """
    Input Param:
    ------------
    capture_radius: The radius of orbital capture and impact for a central body of
    mass M and a projectile moving towards it with velocity v
        SI units: meters | m
    Returns:
    --------
    >>> capture_area(17209590691)
    9.304455331329126e+20
    >>> capture_area(-1)
    Traceback (most recent call last):
        ...
    ValueError: Cannot have a capture radius less than 0

    Returned SI units:
    ------------------
    meters*meters | m**2
    """

    if capture_radius < 0:
        raise ValueError("Cannot have a capture radius less than 0")
    sigma = pi * pow(capture_radius, 2)
    return round(sigma, 0)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

"""
Derivation:

Let: Mt=target mass, Rt=target radius, v=projectile_velocity,
     r_0=radius of projectile at instant 0 to CM of target
     v_p=v at closest approach,
     r_p=radius from projectile to target CM at closest approach,
     R_capture= radius of impact for projectile with velocity v

(1)At time=0  the projectile's energy falling from infinity| E=K+U=0.5*m*(v**2)+0

    E_initial=0.5*m*(v**2)

(2)at time=0 the angular momentum of the projectile relative to CM target|
    L_initial=m*r_0*v*sin(Θ)->m*r_0*v*(R_capture/r_0)->m*v*R_capture

    L_i=m*v*R_capture

(3)The energy of the projectile at closest approach will be its kinetic energy
   at closest approach plus gravitational potential energy(-(GMm)/R)|
    E_p=K_p+U_p->E_p=0.5*m*(v_p**2)-(G*Mt*m)/r_p

    E_p=0.0.5*m*(v_p**2)-(G*Mt*m)/r_p

(4)The angular momentum of the projectile relative to the target at closest
   approach will be L_p=m*r_p*v_p*sin(Θ), however relative to the target Θ=90°
   sin(90°)=1|

    L_p=m*r_p*v_p
(5)Using conservation of angular momentum and energy, we can write a quadratic
   equation that solves for r_p|

   (a)
    Ei=Ep-> 0.5*m*(v**2)=0.5*m*(v_p**2)-(G*Mt*m)/r_p-> v**2=v_p**2-(2*G*Mt)/r_p

   (b)
    Li=Lp-> m*v*R_capture=m*r_p*v_p-> v*R_capture=r_p*v_p-> v_p=(v*R_capture)/r_p

   (c) b plugs int a|
    v**2=((v*R_capture)/r_p)**2-(2*G*Mt)/r_p->

    v**2-(v**2)*(R_c**2)/(r_p**2)+(2*G*Mt)/r_p=0->

    (v**2)*(r_p**2)+2*G*Mt*r_p-(v**2)*(R_c**2)=0

   (d) Using the quadratic formula, we'll solve for r_p then rearrange to solve to
       R_capture

    r_p=(-2*G*Mt ± sqrt(4*G^2*Mt^2+ 4(v^4*R_c^2)))/(2*v^2)->

    r_p=(-G*Mt ± sqrt(G^2*Mt+v^4*R_c^2))/v^2->

    r_p<0 is something we can ignore, as it has no physical meaning for our purposes.->

    r_p=(-G*Mt)/v^2 + sqrt(G^2*Mt^2/v^4 + R_c^2)

   (e)We are trying to solve for R_c. We are looking for impact, so we want r_p=Rt

    Rt + G*Mt/v^2 = sqrt(G^2*Mt^2/v^4 + R_c^2)->

    (Rt + G*Mt/v^2)^2 = G^2*Mt^2/v^4 + R_c^2->

    Rt^2 + 2*G*Mt*Rt/v^2 + G^2*Mt^2/v^4 = G^2*Mt^2/v^4 + R_c^2->

    Rt**2 + 2*G*Mt*Rt/v**2 = R_c**2->

    Rt**2 * (1 + 2*G*Mt/Rt *1/v**2) = R_c**2->

    escape velocity = sqrt(2GM/R)= v_escape**2=2GM/R->

    Rt**2 * (1 + v_esc**2/v**2) = R_c**2->

(6)
    R_capture = Rt * sqrt(1 + v_esc**2/v**2)

Source: Problem Set 3 #8 c.Fall_2017|Honors Astronomy|Professor Rachel Bezanson

Source #2: http://www.nssc.ac.cn/wxzygx/weixin/201607/P020160718380095698873.pdf
           8.8 Planetary Rendezvous: Pg.368
"""
