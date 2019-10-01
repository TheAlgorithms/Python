"""Uses Pythagoras theorem to calculate the distance between two points in space."""

import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


def distance(a, b):
    return math.sqrt(abs(((b.x - a.x)**2 + (b.y - a.y)**2 + (b.z - a.z)**2)))
