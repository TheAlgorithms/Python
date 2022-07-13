"""
Implementation of QuadTree data structure
https://en.wikipedia.org/wiki/Quadtree#:~:text=A%20quadtree%20is%20a%20tree,into%20four%20quadrants%20or%20regions.
This particular data structure is a "point quadtree",
an adaptation of a binary tree used to represent two-dimensional data.
It is often very efficient in comparing 2D, ordered data points
and can operate with a time complexity of O(log n)
Point quadtrees are important because of their completeness.
"""

class Point:
    def __init__(self, x: float, y: float, name="") -> None:
        """
        Point
        x (float): x coordinate of point
        y (float): y coordinate of point
        """
        self.x = x
        self.y = y
        self.name = name  # Used for classifying points uniquely if need be
        return

    # Redefine represenation of a point for display purposes
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Rectangle:
    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        """
        Rectangle. Used for defining bounding region of QuadTree
        x (float): x coordinate of center of rectangle
        y (float): y coordinate of center of rectangle
        w (float): half-width of rectangle
        h (float): half-height of rectangle
        """
        # Note that (x,y) define the CENTER of the rectangle in Cartesian coordinates
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        return

    def contains_point(self, pt: Point) -> bool:
        """
        Test if bounding region contains Point pt
        :param point: (Point): Point being tested
        :returns: (bool) True if point is within region, False otherwise

        Tests
        -----
        p1 = Point(0.1, 0.2)
        p2 = Point(100, 25)
        p3 = Point(0.9, 1.1)
        rect = Rectangle(0.5, 0.5, 0.5, 0.5)
        >>> rect.contains_point(p1)
        True
        >>> rect.contains_point(p2)
        False
        >>> rect.contains_point(p3)
        False
        """
        return (
            self.x - self.w < pt.x < self.x + self.w
            and self.y - self.h < pt.y < self.y + self.h
        )

    def intersects_region(self, region: Rectangle) -> bool:
        """
        Test if the rectangle intersects a given region
        :param region: (Rectangle) Region to test
        :return: (bool)

        Tests
        -----
        rect1 = Rectangle(0.5, 0.5, 0.5, 0.5)
        rect2 = Rectangle(1, 1, 0.2, 0.1)
        rect3 = Rectangle(5, 4, 4, 4)
        >>> rect1.intersects_region(rect2)
        True
        >>> rect1.intersects_region(rect3)
        True
        >>> rect2.intersects_region(rect3)
        True
        """
        return not (
            region.x - region.w > self.x + self.w
            or region.x + region.w < self.x - self.w
            or region.y - region.h > self.y + self.h
            or region.y + region.h < self.y - self.h
        )


class QuadTree:
    def __init__(self, boundary: Rectangle, capacity=4) -> None:
        """
        QuadTree data structure.
        self.points tracks the points within the QuadTree
        self.divided tracks whether or not this QuadTree has split
        :param boundary: (Rectangle) Bounding region of the QuadTree
        :param capacity: (int) Maximum capacity of QuadTree. Default is 4
        """
        self.boundary = boundary
        self.capacity = capacity
        self.points = []  # Points within this region
        self.divided = False  # Whether or not this QuadTree is divided already
        return

    def _subdivide(self) -> None:
        """
        Subdivide the quad tree into 4 daughter regions
        """
        # Some local variables for making the code more readable
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        # Define northeast region of QuadTree
        ne = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        self.northeast = QuadTree(ne, self.capacity)
        # Define northwest region of QuadTree
        nw = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        self.northwest = QuadTree(nw, self.capacity)
        # Define southeast region of QuadTree
        se = Rectangle(x + w / 2, y - h / 2, w / 2, h / 2)
        self.southeast = QuadTree(se, self.capacity)
        # Define southwest region of QuadTree
        sw = Rectangle(x - w / 2, y - h / 2, w / 2, h / 2)
        self.southwest = QuadTree(sw, self.capacity)
        # Set bool to true
        self.divided = True
        return

    def insert_point(self, point: Point) -> None:
        """
        Insert point into the QuadTree
        If the QuadTree is already at maximum capacity, subdivide the QuadTree
        :param point: (Point) Point being inserted into QuadTree

        Tests
        -----
        rect = Rectangle(0.5, 0.5, 0.5, 0.5)
        qt = QuadTree(boundary=rect)
        p1 = Point(0.1, 0.1)
        p2 = Point(0.2, 0.2)
        p3 = Point(0.5, 0.1)
        p4 = Point(0.4, 0.7)
        >>> for p in [p1, p2, p3, p4]
        >>>     qt.insert_point(p)
        >>> qt.points
        [(0.1, 0.1), (0.2, 0.2), (0.5, 0.1), (0.4, 0.7)]
        >>> qt.divided
        False
        >>> qt.insert_point(Point(0.75, 0.75))
        >>> qt.divided
        True
        """
        # Check if point is within bounding region
        # If not, get outta there
        # Otherwise, proceed with adding points and possibly subdividing
        if not self.boundary.contains_point(point):
            return
        else:
            if len(self.points) < self.capacity:
                self.points.append(point)
            else:
                if not self.divided:
                    self._subdivide()
                # If we're forced to subdivide the QuadTree,
                # call this function recursively
                # until all QuadTrees are at or below their maximum capacity
                self.northeast.insert_point(point)
                self.northwest.insert_point(point)
                self.southeast.insert_point(point)
                self.southwest.insert_point(point)
            return

    def query_region(self, region: Rectangle, found=[]) -> list:
        """
        Find points within a given region
        :param found: (array) List of points found within specified region
        :param region: (Rectangle) Region to query points
        :return:

        Tests
        -----
        rect1 = Rectangle(0.5, 0.5, 0.5, 0.5)
        rect2 = Rectangle(0.75, 0.75, 0.25, 0.25)
        qt = QuadTree(boundary=rect1)
        p1 = Point(0.1, 0.1)
        p2 = Point(0.2, 0.2)
        p3 = Point(0.5, 0.1)
        p4 = Point(0.4, 0.7)
        >>> for p in [p1, p2, p3, p4]
        >>>     qt.insert_point(p)
        >>> found = qt.query_region(rect2)
        >>> found
        [(0.6, 0.7)]
        """
        # Determine if any points are found in region already
        # If there are already points found within the region, use that list
        # If not, generate an empty list to store points
        if not found:
            found = []

        # Determine if region and QuadTree overlap
        # If there is no overlap,
        # there is no way the QuadTree can find any points within the region
        if not self.boundary.intersects_region(region):
            return found
        else:
            # Iterate through all points within QuadTree
            # and determine if they are also within region of intersection
            for p in self.points:
                if region.contains_point(p):
                    found.append(p)
            # If the region has subdivided, determine which points
            # are within the regions spawned from this node
            # i.e., check all points contained within the daughter nodes
            if self.divided:
                self.northeast.query_region(region, found)
                self.northwest.query_region(region, found)
                self.southeast.query_region(region, found)
                self.southwest.query_region(region, found)
            return found


if __name__ == "__main__":
    pass
