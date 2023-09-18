"""
Title : Calculate the path length of a sequence of points (x,y)

Description :
        Calculates the path length of a sequence of points (x,y)
        where the next point in the sequence follows an increasing order of x

        https://math.libretexts.org/Bookshelves/Calculus/Map%3A_Calculus__Early_Transcendentals_(Stewart)/08%3A_Further_Applications_of_Integration/8.01%3A_Arc_Length

"""


def discrete_path_length(cordinateSequence: list[tuple[float, float]]) -> float:
    """
    cordinateSequence : a list of (x,y) pairs , with sorted in non decreasing manner of x

    Example:
    Generates a sequence of coordinates for a semicircle of radius and calculates
    path length in this case. i.e length of the semicircle

    >>> import numpy as np
    >>> radius = 5
    >>> X_Cordinates = np.arange(-radius,radius,0.001)
    >>> cordinateSequence = [(x,(5**2 - x**2)**.5) for x in X_Cordinates]
    >>> "%.4f" % discrete_path_length(cordinateSequence)
    '15.6080'

    """
    if cordinateSequence is None:
        return None

    if len(cordinateSequence) < 2:
        return 0
    res_slopes = []
    for i in range(1, len(cordinateSequence)):
        res_slopes.append(
            ((cordinateSequence[i][0] - cordinateSequence[i - 1][0]) ** 2 + (cordinateSequence[i][1] - cordinateSequence[i - 1][1]) ** 2) ** 0.5
        )
    return sum(res_slopes)


if __name__ == "__main__":
    try:
        import numpy as np
    except ImportError as err:
        print("Please Install Numpy first !")
        raise err
    import doctest

    doctest.testmod()
    radius = 5
    X_Cordinates_array = np.arange(-radius, radius, 0.001)
    # Make points for sequence for a semicircle of radius 5
    cordinateSequence = [(x, (5**2 - x**2) ** 0.5) for x in X_Cordinates_array]
    print(
        f"Test Radius {radius},\
          Test Arc {discrete_path_length(cordinateSequence)},\
          Expected Arc {3.14159 * radius}"
    )
