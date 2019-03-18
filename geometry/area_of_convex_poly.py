from __future__ import print_function
import sys

"""
General algortihm to find area of any convex polygon given its verticies
using a cross product. Implemented in Python.

For doctests, run the commands:
python -m doctest -v AreaOfConvexPoly.py
or
python3 -m doctest -v AreaOfConvexPoly.py

For manual testing:
python AreaOfConvexPoly.py
"""

def AreaOfPoints(points):
    """
    General algorithm to find area of any convex polygon given its verticies
    using a cross product. Implemented in Python.

    :param points: A collection containing the points describing the verticies
    of any convex polygon. A point is stored as a tuple: [(x1, y1), (x2, y2)...]

    :return: float area of the convex polygon

    Examples:
    >>> AreaOfPoints([(1, 0), (0, 0), (1, 1), (0, 1)])
    1.0
    >>> AreaOfPoints([(0, 0), (10, 0), (10, 10)])
    50.0
    >>> AreaOfPoints([(-100, -50), (100, -50), (1090, 1090), (-1090, 1090)])
    1356600.0

    """
    #find left the bottom most point
    start = min(points, key=lambda p: (p[0], p[1]))
    points.pop(points.index(start))

    #sort points in counterclockwise order by sorting
    # the slope of the vector between start and each point
    points.sort(key=lambda p: (Slope(start, p), -p[1], p[0]))
    points.insert(0, start)

    return CrossProduct(points)

def Slope(p1, p2):
    if p2[0] - p1[0] == 0:
        return float(sys.maxsize)
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


#Finds the area of polygon by extracting the
# determinant of the 2 x n matrix of points.
def CrossProduct(points):
    points.append(points[0])
    suml = 0
    sumr = 0
    for i in range(len(points) - 1):
        suml += points[i][1] * points[i+1][0]
        sumr += points[i][0] * points[i+1][1]
    return (sumr - suml) * 0.5


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input("Input points in the following format: x1 y1 x2 y2... ").strip()
    ints = list(map(int, user_input.split(" ")))
    points = [(ints[2 * i], ints[2*i+1]) for i in range(len(ints)//2)]

    print("Area of Convex Polygon = " + str(AreaOfPoints(points)))
