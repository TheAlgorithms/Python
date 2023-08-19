"""
Title : Calculate the path length of a sequence of points (x,y)

Description :
        Calculates the path length of a sequence of points (x,y)
        where the next point in the sequence follows an increasing order of x

        https://math.libretexts.org/Bookshelves/Calculus/Map%3A_Calculus__Early_Transcendentals_(Stewart)/08%3A_Further_Applications_of_Integration/8.01%3A_Arc_Length

"""


def discrete_path_length(seq: list) -> float:
    """
    Generates a sequence of coordinates for a semicircle of radius and calculates
    path length in this case. i.e length of the semicircle
    >>> radius = 5
    >>> xRange = np.arange(-radius,radius,0.001)
    >>> seq = [(x,(5**2 - x**2)**.5) for x in xRange]
    >>> print(discrete_path_length(seq))
    15.60795911036593
    """
    res_slopes = []
    for i in range(1, len(seq)):
        res_slopes.append(
            ((seq[i][0] - seq[i - 1][0]) ** 2 + (seq[i][1] - seq[i - 1][1]) ** 2) ** 0.5
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
    xrange = np.arange(-radius, radius, 0.001)
    # Make points for sequence for a semicircle of radius 5
    seq = [(x, (5**2 - x**2) ** 0.5) for x in xrange]
    print(
        f"Test Radius {radius},\
          Test Arc {discrete_path_length(seq)},\
          Expected Arc {3.14159 * radius}"
    )
