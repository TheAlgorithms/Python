"""
Collision detection algorithms for 2D geometric shapes.

Collision detection is a fundamental concept in computational geometry, physics
simulations, and game development. It determines whether two or more geometric
objects intersect or overlap in space.

This module implements several common 2D collision detection algorithms:
- Axis-Aligned Bounding Box (AABB) collision detection
- Circle-circle collision detection
- Circle-AABB collision detection
- Point-in-rectangle detection
- Point-in-circle detection

Reference: https://en.wikipedia.org/wiki/Collision_detection
Reference: https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
"""

from __future__ import annotations

from math import sqrt


def is_aabb_collision(
    x1: float,
    y1: float,
    w1: float,
    h1: float,
    x2: float,
    y2: float,
    w2: float,
    h2: float,
) -> bool:
    """
    Check if two Axis-Aligned Bounding Boxes (AABBs) are colliding.

    Each rectangle is defined by its top-left corner (x, y), width (w),
    and height (h).

    >>> is_aabb_collision(0, 0, 10, 10, 5, 5, 10, 10)
    True
    >>> is_aabb_collision(0, 0, 10, 10, 20, 20, 10, 10)
    False
    >>> is_aabb_collision(0, 0, 10, 10, 10, 0, 10, 10)
    False
    >>> is_aabb_collision(0, 0, 5, 5, 3, 3, 5, 5)
    True
    >>> is_aabb_collision(-5, -5, 10, 10, 0, 0, 10, 10)
    True
    >>> is_aabb_collision(0, 0, -1, 10, 5, 5, 10, 10)
    Traceback (most recent call last):
        ...
    ValueError: Width and height must be non-negative
    >>> is_aabb_collision(0, 0, 10, 10, 5, 5, -1, 10)
    Traceback (most recent call last):
        ...
    ValueError: Width and height must be non-negative
    """
    if w1 < 0 or h1 < 0 or w2 < 0 or h2 < 0:
        raise ValueError("Width and height must be non-negative")

    return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2


def is_circle_collision(
    cx1: float,
    cy1: float,
    r1: float,
    cx2: float,
    cy2: float,
    r2: float,
) -> bool:
    """
    Check if two circles are colliding.

    Each circle is defined by its center (cx, cy) and radius (r).

    >>> is_circle_collision(0, 0, 5, 8, 0, 5)
    True
    >>> is_circle_collision(0, 0, 5, 20, 20, 5)
    False
    >>> is_circle_collision(0, 0, 10, 5, 5, 10)
    True
    >>> is_circle_collision(0, 0, 1, 3, 0, 1)
    False
    >>> is_circle_collision(0, 0, 0, 0, 0, 0)
    False
    >>> is_circle_collision(0, 0, -1, 5, 5, 3)
    Traceback (most recent call last):
        ...
    ValueError: Radius must be non-negative
    """
    if r1 < 0 or r2 < 0:
        raise ValueError("Radius must be non-negative")

    distance_squared = (cx2 - cx1) ** 2 + (cy2 - cy1) ** 2
    radius_sum = r1 + r2
    return distance_squared < radius_sum**2


def is_circle_aabb_collision(
    cx: float,
    cy: float,
    r: float,
    rx: float,
    ry: float,
    rw: float,
    rh: float,
) -> bool:
    """
    Check if a circle and an Axis-Aligned Bounding Box (AABB) are colliding.

    The circle is defined by its center (cx, cy) and radius (r).
    The rectangle is defined by its top-left corner (rx, ry), width (rw),
    and height (rh).

    >>> is_circle_aabb_collision(5, 5, 3, 0, 0, 10, 10)
    True
    >>> is_circle_aabb_collision(20, 20, 3, 0, 0, 10, 10)
    False
    >>> is_circle_aabb_collision(12, 5, 3, 0, 0, 10, 10)
    True
    >>> is_circle_aabb_collision(0, 0, 1, 5, 5, 10, 10)
    False
    >>> is_circle_aabb_collision(5, 5, -1, 0, 0, 10, 10)
    Traceback (most recent call last):
        ...
    ValueError: Radius must be non-negative
    >>> is_circle_aabb_collision(5, 5, 3, 0, 0, -1, 10)
    Traceback (most recent call last):
        ...
    ValueError: Width and height must be non-negative
    """
    if r < 0:
        raise ValueError("Radius must be non-negative")
    if rw < 0 or rh < 0:
        raise ValueError("Width and height must be non-negative")

    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))

    distance_squared = (cx - closest_x) ** 2 + (cy - closest_y) ** 2
    return distance_squared < r**2


def is_point_in_rectangle(
    px: float,
    py: float,
    rx: float,
    ry: float,
    rw: float,
    rh: float,
) -> bool:
    """
    Check if a point is inside an Axis-Aligned Bounding Box (rectangle).

    The point is defined by (px, py).
    The rectangle is defined by its top-left corner (rx, ry), width (rw),
    and height (rh).

    >>> is_point_in_rectangle(5, 5, 0, 0, 10, 10)
    True
    >>> is_point_in_rectangle(15, 15, 0, 0, 10, 10)
    False
    >>> is_point_in_rectangle(0, 0, 0, 0, 10, 10)
    True
    >>> is_point_in_rectangle(10, 10, 0, 0, 10, 10)
    False
    >>> is_point_in_rectangle(-1, 5, 0, 0, 10, 10)
    False
    >>> is_point_in_rectangle(5, 5, 0, 0, -1, 10)
    Traceback (most recent call last):
        ...
    ValueError: Width and height must be non-negative
    """
    if rw < 0 or rh < 0:
        raise ValueError("Width and height must be non-negative")

    return rx <= px < rx + rw and ry <= py < ry + rh


def is_point_in_circle(
    px: float,
    py: float,
    cx: float,
    cy: float,
    r: float,
) -> bool:
    """
    Check if a point is inside a circle.

    The point is defined by (px, py).
    The circle is defined by its center (cx, cy) and radius (r).

    >>> is_point_in_circle(3, 4, 0, 0, 10)
    True
    >>> is_point_in_circle(10, 10, 0, 0, 5)
    False
    >>> is_point_in_circle(0, 0, 0, 0, 1)
    True
    >>> is_point_in_circle(5, 0, 0, 0, 5)
    False
    >>> is_point_in_circle(3, 4, 0, 0, -1)
    Traceback (most recent call last):
        ...
    ValueError: Radius must be non-negative
    """
    if r < 0:
        raise ValueError("Radius must be non-negative")

    distance_squared = (px - cx) ** 2 + (py - cy) ** 2
    return distance_squared < r**2


def detect_all_collisions(
    objects: list[dict],
) -> list[tuple[int, int]]:
    """
    Detect all pairwise collisions among a list of geometric objects.

    Each object is a dictionary with a 'type' key ('circle' or 'rect') and
    the corresponding geometric parameters.

    Circle: {'type': 'circle', 'cx': float, 'cy': float, 'r': float}
    Rectangle: {'type': 'rect', 'x': float, 'y': float, 'w': float, 'h': float}

    Returns a list of tuples (i, j) where objects[i] and objects[j] collide.

    >>> objects = [
    ...     {'type': 'circle', 'cx': 0, 'cy': 0, 'r': 5},
    ...     {'type': 'circle', 'cx': 3, 'cy': 0, 'r': 5},
    ...     {'type': 'circle', 'cx': 100, 'cy': 100, 'r': 1},
    ... ]
    >>> detect_all_collisions(objects)
    [(0, 1)]
    >>> objects = [
    ...     {'type': 'rect', 'x': 0, 'y': 0, 'w': 10, 'h': 10},
    ...     {'type': 'rect', 'x': 5, 'y': 5, 'w': 10, 'h': 10},
    ...     {'type': 'circle', 'cx': 20, 'cy': 20, 'r': 3},
    ... ]
    >>> detect_all_collisions(objects)
    [(0, 1)]
    >>> detect_all_collisions([])
    []
    """
    collisions: list[tuple[int, int]] = []
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            if _check_collision(objects[i], objects[j]):
                collisions.append((i, j))
    return collisions


def _check_collision(obj1: dict, obj2: dict) -> bool:
    """
    Check collision between two geometric objects.

    >>> _check_collision(
    ...     {'type': 'circle', 'cx': 0, 'cy': 0, 'r': 5},
    ...     {'type': 'circle', 'cx': 3, 'cy': 0, 'r': 5},
    ... )
    True
    >>> _check_collision(
    ...     {'type': 'rect', 'x': 0, 'y': 0, 'w': 10, 'h': 10},
    ...     {'type': 'rect', 'x': 20, 'y': 20, 'w': 5, 'h': 5},
    ... )
    False
    """
    type1, type2 = obj1["type"], obj2["type"]

    if type1 == "circle" and type2 == "circle":
        return is_circle_collision(
            obj1["cx"],
            obj1["cy"],
            obj1["r"],
            obj2["cx"],
            obj2["cy"],
            obj2["r"],
        )

    if type1 == "rect" and type2 == "rect":
        return is_aabb_collision(
            obj1["x"],
            obj1["y"],
            obj1["w"],
            obj1["h"],
            obj2["x"],
            obj2["y"],
            obj2["w"],
            obj2["h"],
        )

    if type1 == "circle" and type2 == "rect":
        return is_circle_aabb_collision(
            obj1["cx"],
            obj1["cy"],
            obj1["r"],
            obj2["x"],
            obj2["y"],
            obj2["w"],
            obj2["h"],
        )

    if type1 == "rect" and type2 == "circle":
        return is_circle_aabb_collision(
            obj2["cx"],
            obj2["cy"],
            obj2["r"],
            obj1["x"],
            obj1["y"],
            obj1["w"],
            obj1["h"],
        )

    msg = f"Unknown object types: {type1}, {type2}"
    raise ValueError(msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("AABB collision:", is_aabb_collision(0, 0, 10, 10, 5, 5, 10, 10))
    print("Circle collision:", is_circle_collision(0, 0, 5, 8, 0, 5))
    print("Point in rect:", is_point_in_rectangle(5, 5, 0, 0, 10, 10))
    print("Point in circle:", is_point_in_circle(3, 4, 0, 0, 10))
    print(
        "Circle-AABB collision:",
        is_circle_aabb_collision(5, 5, 3, 0, 0, 10, 10),
    )
    print(
        "Detect all:",
        detect_all_collisions(
            [
                {"type": "circle", "cx": 0, "cy": 0, "r": 5},
                {"type": "circle", "cx": 3, "cy": 0, "r": 5},
                {"type": "rect", "x": 100, "y": 100, "w": 10, "h": 10},
            ]
        ),
    )
