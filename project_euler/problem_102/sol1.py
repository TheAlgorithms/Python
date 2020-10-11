"""
Problem 102: https://projecteuler.net/problem=102

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""

# Class to represent a point with x and y coordinates
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Calculates the difference between two points
    def minus(self, p):
        return Point(p.x - self.x, p.y - self.y)

    def __str__(self):
        return f"( {self.x}, {self.y})"


# Calculates the distance between p1 and p2, or one side of a triangle
def side(p1, p2):
    return (abs(p2.x - p1.x) ** 2.0 + abs(p2.y - p1.y) ** 2.0) ** 0.5


# Calculates the cross product between two points
def cross_product(p1, p2):
    return p1.x * p2.y - p1.y * p2.x


# Calculates the area of an triangle with vertices on points p1, p2, p3
def area(p1, p2, p3):
    a = side(p1, p2)
    b = side(p2, p3)
    c = side(p3, p1)

    cp = cross_product(p1.minus(p2), p1.minus(p3))

    if cp == 0:
        return 0

    s = (a + b + c) / 2.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


# Returns wheter a triangle contains (0, 0) or not
def triangle_contains_origin(triangle):

    p1, p2, p3 = triangle
    p0 = Point(0.0, 0.0)

    bigArea = area(p1, p2, p3)
    smallerAreas = [
        area(p1, p2, p0),
        area(p2, p3, p0),
        area(p3, p1, p0),
    ]

    return round(bigArea, 5) == round(sum(smallerAreas), 5)


# Loads the triangles from the file provided by Project Euler
def triangles_from_file(fileName):
    # Builds 3 vertices from a line
    def build_triangle(fromStr):
        splitted = fromStr.split(",")
        asInt = [float(i) for i in splitted]
        triangle = []
        for i in range(0, 6, 2):
            newPoint = Point(asInt[i], asInt[i + 1])
            triangle.append(newPoint)
        return triangle

    data = open(fileName, "r").read()
    tests = data.split("\n")
    triangles = [build_triangle(i) for i in tests if not i == ""]

    return triangles


def count_triangles():
    triangles = triangles_from_file("triangles_euler102.txt")

    return len([True for i in triangles if triangle_contains_origin(i)])


if __name__ == "__main__":
    print(f"Triangles containing the origin: {count_triangles()}")
