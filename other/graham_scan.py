"""
This is a pure Python implementation of the merge-insertion sort algorithm
Source: https://en.wikipedia.org/wiki/Graham_scan

For doctests run following command:
python3 -m doctest -v graham_scan.py
"""

from __future__ import annotations

from collections import deque
from enum import Enum
from math import atan2, degrees
from sys import maxsize


def graham_scan(points: list[list[int, int]]) -> list[list[int, int]]:
    """Pure implementation of graham scan algorithm in Python

    :param points: The unique points on coordinates.
    :return: The points on convex hell.

    Examples:
    >>> graham_scan([(9, 6), (3, 1), (0, 0), (5, 5), (5, 2), (7, 0), (3, 3), (1, 4)])
    [(0, 0), (7, 0), (9, 6), (5, 5), (1, 4)]

    >>> graham_scan([(0, 0), (1, 0), (1, 1), (0, 1)])
    [(0, 0), (1, 0), (1, 1), (0, 1)]

    >>> graham_scan([(0, 0), (1, 1), (2, 2), (3, 3), (-1, 2)])
    [(0, 0), (1, 1), (2, 2), (3, 3), (-1, 2)]

    >>> graham_scan([(-100, 20), (99, 3), (1, 10000001), (5133186, -25), (-66, -4)])
    [(5133186, -25), (1, 10000001), (-100, 20), (-66, -4)]
    """

    if len(points) <= 2:
        # There is no convex hull
        raise ValueError("graham_scan: argument must contain more than 3 points.")
    if len(points) == 3:
        return points
    # find the lowest and the most left point
    minidx = 0
    miny, minx = maxsize, maxsize
    for i, point in enumerate(points):
        x = point[0]
        y = point[1]
        if y < miny:
            miny = y
            minx = x
            minidx = i
        if y == miny:
            if x < minx:
                minx = x
                minidx = i

    # remove the lowest and the most left point from points for preparing for sort
    points.pop(minidx)

    def angle_comparer(point: list[int, int], minx: int, miny: int) -> float:
        """Return the angle toward to point from (minx, miny)

        :param point: The target point
               minx: The starting point's x
               miny: The starting point's y
        :return: the angle

        Examples:
        >>> angle_comparer([1,1], 0, 0)
        45.0

        >>> angle_comparer([100,1], 10, 10)
        -5.710593137499642

        >>> angle_comparer([5,5], 2, 3)
        33.690067525979785
        """
        # sort the points accorgind to the angle from the lowest and the most left point
        x = point[0]
        y = point[1]
        angle = degrees(atan2(y - miny, x - minx))
        return angle

    sorted_points = sorted(points, key=lambda point: angle_comparer(point, minx, miny))
    # This insert actually costs complexity,
    # and you should insteadly add (minx, miny) into stack later.
    # I'm using insert just for easy understanding.
    sorted_points.insert(0, (minx, miny))

    # traversal from the lowest and the most left point in anti-clockwise direction
    # if direction gets right, the previous point is not the convex hull.
    class Direction(Enum):
        left = 1
        straight = 2
        right = 3

    def check_direction(
        starting: list[int, int], via: list[int, int], target: list[int, int]
    ) -> Direction:
        """Return the direction toward to the line from via to target from starting

        :param starting: The starting point
               via: The via point
               target: The target point
        :return: the Direction

        Examples:
        >>> check_direction([1,1], [2,2], [3,3])
        Direction.straight

        >>> check_direction([60,1], [-50,199], [30,2])
        Direction.left

        >>> check_direction([0,0], [5,5], [10,0])
        Direction.right
        """
        x0, y0 = starting
        x1, y1 = via
        x2, y2 = target
        via_angle = degrees(atan2(y1 - y0, x1 - x0))
        if via_angle < 0:
            via_angle += 360
        target_angle = degrees(atan2(y2 - y0, x2 - x0))
        if target_angle < 0:
            target_angle += 360
        # t-
        #  \ \
        #   \ v
        #    \|
        #     s
        # via_angle is always lower than target_angle, if direction is left.
        # If they are same, it means they are on a same line of convex hull.
        if target_angle > via_angle:
            return Direction.left
        if target_angle == via_angle:
            return Direction.straight
        if target_angle < via_angle:
            return Direction.right

    stack = deque()
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])
    stack.append(sorted_points[2])
    # In any ways, the first 3 points line are towards left.
    # Because we sort them the angle from minx, miny.
    current_direction = Direction.left

    for i in range(3, len(sorted_points)):
        while True:
            starting = stack[-2]
            via = stack[-1]
            target = sorted_points[i]
            next_direction = check_direction(starting, via, target)

            if next_direction == Direction.left:
                current_direction = Direction.left
                break
            if next_direction == Direction.straight:
                if current_direction == Direction.left:
                    # We keep current_direction as left.
                    # Because if the straight line keeps as straight,
                    # we want to know if this straight line is towards left.
                    break
                elif current_direction == Direction.right:
                    # If the straight line is towards right,
                    # every previous points on those straigh line is not convex hull.
                    stack.pop()
            if next_direction == Direction.right:
                stack.pop()
        stack.append(sorted_points[i])
    return list(stack)
