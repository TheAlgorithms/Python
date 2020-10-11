"""
Problem 102: https://projecteuler.net/problem=102

Three distinct points are plotted at random on a Cartesian plane,
 for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'),
 a 27K text file containing the co-ordinates of one thousand "random"
 triangles, find the number of triangles for which the
 interior contains the origin.

NOTE: The first two examples in the file represent
 the triangles in the example given above.
"""


# Class representing a 2D point with x and y coordinates
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def minus(self, p):
        """ Returns the difference between self and another 2D point

        >>> p = Point(2, 3)
        >>> p.minus( Point(4, 5))
        p.x == 2 and p.y == 2
        """

        return Point(p.x - self.x, p.y - self.y)

    def __str__(self):
        return f"( {self.x}, {self.y})"
    def __unicode__(self):
        return f"( {self.x}, {self.y})"
    def __repr__(self):
        return f"( {self.x}, {self.y})"


def side(p1, p2):
    """ Returns the distance between p1 and p2

    >>> cross_product(Point(0, 3), Point(4, 0))
    5.0
    """
    return (abs(p2.x - p1.x) ** 2.0 + abs(p2.y - p1.y) ** 2.0) ** 0.5


def cross_product(p1, p2):
    """ Returns the cross product between two 2D points

    >>> cross_product(Point(1, 2), Point(3, 4))
    -2.0
    """
    return p1.x * p2.y - p1.y * p2.x

def area(p1, p2, p3):
    """ Returns the area of an triangle of vertices on points p1, p2, p3

    >>> area(Point(1, 2), Point(-2, 3), Point(3, 4))
    4.000000000000002
    """

    a = side(p1, p2)
    b = side(p2, p3)
    c = side(p3, p1)

    cp = cross_product(p1.minus(p2), p1.minus(p3))

    if cp == 0:
        return 0

    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def triangle_contains_origin(triangle):
    """ Returns wheter a triangle contains (0, 0) or not

    >>> triangle_contains_origin([Point(-175,41), Point(-421,-714), Point(574,-645)])
    False

    >>> triangle_contains_origin([Point(-340,495), Point(-153,-910), Point(835,-947)])
    True
    """

    p1, p2, p3 = triangle
    p0 = Point(0.0, 0.0)

    big_area = area(p1, p2, p3)
    smaller_areas = [
        area(p1, p2, p0),
        area(p2, p3, p0),
        area(p3, p1, p0),
    ]

    return round(big_area, 5) == round(sum(smaller_areas), 5)


def build_triangle(fromStr):
    """ Returns an array of 2D Points composing a triangle from a comma separated string

    >>> len(build_triangle('-340,495,-153,-910,835,-947'))
    3
    """
    splitted = fromStr.split(",")
    asInt = [float(i) for i in splitted]
    triangle = []
    for i in range(0, 6, 2):
        new_point = Point(asInt[i], asInt[i + 1])
        triangle.append(new_point)
    return triangle

def triangles_from_file(fileName):
    """ Returns an array of triangles from the file provided by Project Euler

    >>> len(triangles_from_file('triangles_euler102.txt'))
    1000
    """

    data = open(fileName, "r").read()
    tests = data.split("\n")
    triangles = [build_triangle(i) for i in tests if not i == ""]

    return triangles


def count_triangles():
    """ Returns the count of triangles that contains the origin
    
    >>> count_triangles()
    228
    """
    triangles = triangles_from_file("triangles_euler102.txt")

    return len([True for i in triangles if triangle_contains_origin(i)])


if __name__ == "__main__":
    print(f"Triangles containing the origin: {count_triangles()}")
