"""
Check if three points are collinear in 3D.

In short, the idea is that we are able to create a triangle using three points,
and the area of that triangle can determine if the three points are collinear or not.


First, we create two vectors with the same initial point from the three points,
then we will calculate the cross-product of them.

The length of the cross vector is numerically equal to the area of a parallelogram.

Finally, the area of the triangle is equal to half of the area of the parallelogram.

Since we are only differentiating between zero and anything else,
we can get rid of the square root when calculating the length of the vector,
and also the division by two at the end.

From a second perspective, if the two vectors are parallel and overlapping,
we can't get a nonzero perpendicular vector,
since there will be an infinite number of orthogonal vectors.

To simplify the solution we will not calculate the length,
but we will decide directly from the vector whether it is equal to (0, 0, 0) or not.


Read More:
    https://math.stackexchange.com/a/1951650
"""

Vector3d = tuple[float, float, float]
Point3d = tuple[float, float, float]


def create_vector(end_point1: Point3d, end_point2: Point3d) -> Vector3d:
    """
    Pass two points to get the vector from them in the form (x, y, z).

    >>> create_vector((0, 0, 0), (1, 1, 1))
    (1, 1, 1)
    >>> create_vector((45, 70, 24), (47, 32, 1))
    (2, -38, -23)
    >>> create_vector((-14, -1, -8), (-7, 6, 4))
    (7, 7, 12)
    """
    x = end_point2[0] - end_point1[0]
    y = end_point2[1] - end_point1[1]
    z = end_point2[2] - end_point1[2]
    return (x, y, z)


def get_3d_vectors_cross(ab: Vector3d, ac: Vector3d) -> Vector3d:
    """
    Get the cross of the two vectors AB and AC.

    I used determinant of 2x2 to get the determinant of the 3x3 matrix in the process.

    Read More:
        https://en.wikipedia.org/wiki/Cross_product
        https://en.wikipedia.org/wiki/Determinant

    >>> get_3d_vectors_cross((3, 4, 7), (4, 9, 2))
    (-55, 22, 11)
    >>> get_3d_vectors_cross((1, 1, 1), (1, 1, 1))
    (0, 0, 0)
    >>> get_3d_vectors_cross((-4, 3, 0), (3, -9, -12))
    (-36, -48, 27)
    >>> get_3d_vectors_cross((17.67, 4.7, 6.78), (-9.5, 4.78, -19.33))
    (-123.2594, 277.15110000000004, 129.11260000000001)
    """
    x = ab[1] * ac[2] - ab[2] * ac[1]  # *i
    y = (ab[0] * ac[2] - ab[2] * ac[0]) * -1  # *j
    z = ab[0] * ac[1] - ab[1] * ac[0]  # *k
    return (x, y, z)


def is_zero_vector(vector: Vector3d, accuracy: int) -> bool:
    """
    Check if vector is equal to (0, 0, 0) or not.

    Since the algorithm is very accurate, we will never get a zero vector,
    so we need to round the vector axis,
    because we want a result that is either True or False.
    In other applications, we can return a float that represents the collinearity ratio.

    >>> is_zero_vector((0, 0, 0), accuracy=10)
    True
    >>> is_zero_vector((15, 74, 32), accuracy=10)
    False
    >>> is_zero_vector((-15, -74, -32), accuracy=10)
    False
    """
    return tuple(round(x, accuracy) for x in vector) == (0, 0, 0)


def are_collinear(a: Point3d, b: Point3d, c: Point3d, accuracy: int = 10) -> bool:
    """
    Check if three points are collinear or not.

    1- Create two vectors AB and AC.
    2- Get the cross vector of the two vectors.
    3- Calculate the length of the cross vector.
    4- If the length is zero then the points are collinear, else they are not.

    The use of the accuracy parameter is explained in is_zero_vector docstring.

    >>> are_collinear((4.802293498137402, 3.536233125455244, 0),
    ...               (-2.186788107953106, -9.24561398001649, 7.141509524846482),
    ...               (1.530169574640268, -2.447927606600034, 3.343487096469054))
    True
    >>> are_collinear((-6, -2, 6),
    ...               (6.200213806439997, -4.930157614926678, -4.482371908289856),
    ...               (-4.085171149525941, -2.459889509029438, 4.354787180795383))
    True
    >>> are_collinear((2.399001826862445, -2.452009976680793, 4.464656666157666),
    ...               (-3.682816335934376, 5.753788986533145, 9.490993909044244),
    ...               (1.962903518985307, 3.741415730125627, 7))
    False
    >>> are_collinear((1.875375340689544, -7.268426006071538, 7.358196269835993),
    ...               (-3.546599383667157, -4.630005261513976, 3.208784032924246),
    ...               (-2.564606140206386, 3.937845170672183, 7))
    False
    """
    ab = create_vector(a, b)
    ac = create_vector(a, c)
    return is_zero_vector(get_3d_vectors_cross(ab, ac), accuracy)
