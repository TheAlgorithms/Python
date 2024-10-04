"""
Find the Bragg angle of a crystal given the wavelength of radiation, distane between the planes of crystal and the order of diffraction.

In many areas of science, Bragg's law, Wulff–Bragg's condition, or Laue–Bragg interference are a special case of Laue diffraction, 
giving the angles for coherent scattering of waves from a large crystal lattice. 
It describes how the superposition of wave fronts scattered by lattice planes leads to a strict relation between the wavelength and scattering angle. 
This law was initially formulated for X-rays, but it also applies to all types of matter waves including neutron and electron waves if there are a large number of atoms, 
as well as visible light with artificial periodic microscale lattices.  
    
Reference: https://en.wikipedia.org/wiki/Bragg%27s_law

"""



import math

def bragg_angle(distance: float, n: int, wavelength: float) -> float:
    """
    Calculate the Bragg diffraction angle in degrees.

    The Bragg diffraction angle is given by
    sin(θ) = (n * λ) / (2 * d)
    
    Parameters:
    distance (float): Distance between crystal planes (in meters).
    n (int): Order of reflection.
    wavelength (float): Wavelength of the radiation (in meters).
    
    Returns:
    float: The Bragg diffraction angle θ in degrees.
    
    Example:
    >>> bragg_angle(2.2e-10, 1, 2.2e-10)
    30.0

    >>> bragg_angle(5.0e-10, 2, 1.0e-10)
    11.5

    >>> bragg_angle(4.0e-10, 1, 8.0e-10)
    90.0

    # Test case for an invalid sine value that is out of range
    >>> bragg_angle(1e-10, 2, 3e-10)
    Traceback (most recent call last):
        ...
    ValueError: The calculated sine value is out of the valid range.
    """
    
    sine_theta = (n * wavelength) / (2 * distance)
    
    if sine_theta > 1 or sine_theta < -1:
        raise ValueError("The calculated sine value is out of the valid range.")
    
    theta_radians = math.asin(sine_theta)
    
    theta_degrees = math.degrees(theta_radians)
    
    return round(theta_degrees, 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
