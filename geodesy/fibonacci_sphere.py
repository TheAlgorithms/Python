from math import sin, cos, sqrt

def generate_fibonacci_sphere(n_points: int, radius: float = 1) -> list:
    """
    Generate a Fibonacci Sphere with a given number of points and radius.

    This algorithm creates a spherical lattice of evenly distrubuted
    (approximately equidistant) points by mapping the Fibonacci spiral onto 
    a sphere. It can be applied to computer graphics (to get the verticies
    of a spherical mesh), or to get approximate solutions to specific cases
    of the Thomson problem.

    Args:
        n_points: number of points with which to build the lattice
        radius: the radius of the resulting sphere lattice
    Returns:
        list of points (of format [x, y, z]) in the sphere lattice
    """
    points = []
    phi = (1 + sqrt(5))/2 # exact form of the golden ratio
    for i in range(n_points):
        # angle displacement from positive x-direction in radians
        theta = phi * i 
        # displacement from x-y plane (spiral starts at (0, 0, radius))
        z = radius - i/n_points
        # length of the projection of the vector from the center of the sphere
        # to the current point (height z, angle theta) onto the x-y plane
        r_proj = sqrt(radius**2 - z**2)
        # translate the polar coordinates of the projection vector (r_proj, theta) 
        # to cartesian coordinates, which will be the same as the coordinates of the 
        # current point on the sphere.
        x = r_proj * cos(theta)
        y = r_proj * sin(theta)
        points.append([x, y, z])
    return points

if __name__ == "__main__":
    import doctest

    doctest.testmod()

