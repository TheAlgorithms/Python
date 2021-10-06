# Profile: https://github.com/jackrsteiner
# Algorithm: https://en.wikipedia.org/wiki/Quadtree

class Location:
    """
    A class representing the x,y coordinate location of an object and it's
    optional name.

    Parameter
    ----------
    x : float
        the x coordinate of the location object
    y : float
        the y coordinate of the location object
    name : str
        optional arbitrary name of the location object

    Attributes
    ----------
    x : float
        Location's x coordinate
    y : float
        Location's y coordinate
    name : str
        Location's name, but could be any data
    """

    def __init__(self, x: float, y: float, name: str = None):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name}({self.x},{self.y})"

    def distance(self, loc) -> float:
        """
        Location method that takes a Location object and returns its distance
        to the current Location object.

        Parameters:
        loc : Location
            A Location object to calculate a distance from

        Returns:
        float: The distance from the point
        """
        return ((loc.x - self.x) ** 2 + (loc.y - self.y) ** 2) ** (1 / 2)


class QuadNode:
    """
    A class representing a quadtree node. Each parent has exactly four
    children.

    Parameters
    ----------
    origin : Location
        the bottom left corner of the node
    width : float
        width of the node
    height : float
        height of the node
    capacity : int , default = 1
        number of points node can contain

    Attributes
    ----------
    origin : Location
        the bottom left corner of the node
    width : float
        width of the node
    height : float
        height of the node
    capacity : int
        number of points node can contain
    contents : list
        list of Location instances contained in the node
    children : list
        list of first level children quadnodes this node has been segmented in to
    """

    def __init__(
        self, origin: Location, width: float, height: float, capacity: int = 1
    ):
        self.origin = origin
        self.width = width
        self.height = height
        self.capacity = capacity
        self.contents: list = []
        self.children: list = []

    def __str__(self):
        locs = []
        for loc in self.contents:
            locs.append(loc.__str__())
        quads = []
        for quad in self.children:
            quads.append(quad.__str__())
        name = (f"QuadNode origin: {self.origin}; " +
                f"width*height: {self.width}*{self.height}; " +
                f"contains: {locs}; and children: {quads}")
        return name

    def is_bounding(self, loc: Location, buffer: int = 0) -> bool:
        """
        QuadNode method that takes a Location object and return a boolean
        indicating if the Location is contained within the QuadNode instance.

        Parameters:
        loc : Location
            A Location object to determine if it bounded by the QuadNode instance
        buffer : int , default = 0
            A distance defining a buffer area: points within this distance of
            the QuadNode edge should still be included in the bounding area

        Returns:
        bool: True if loc passed to method is within the QuadNode boundary
        and/or its buffer
        """
        within_left = loc.x + buffer >= self.origin.x
        within_right = loc.x - buffer < self.origin.x + self.width
        within_bottom = loc.y + buffer >= self.origin.y
        within_top = loc.y - buffer < self.origin.y + self.height
        return within_left and within_right and within_bottom and within_top

    def create_children(self) -> list:
        """
        QuadNode method with no parameters that returns list of 4 quadtree
        node children.

        Returns:
        list[]: List of 4 child quadtree nodes for parent of self.
        """
        if self.children:
            raise Warning(
                f"create_children called on node {self.origin} with children"
            )
        else:
            # Calculate children dimensions
            child_width = self.width / 2
            child_height = self.height / 2
            # Create children nodes
            child_sw = QuadNode(self.origin, child_width, child_height, self.capacity)
            child_se = QuadNode(
                Location(self.origin.x + child_width, self.origin.y),
                self.width - child_width,
                child_height,
                self.capacity,
            )
            child_nw = QuadNode(
                Location(self.origin.x, self.origin.y + child_height),
                child_width,
                self.height - child_height,
                self.capacity,
            )
            child_ne = QuadNode(
                Location(self.origin.x + child_width, self.origin.y + child_height),
                self.width - child_width,
                self.height - child_height,
                self.capacity,
            )
        return [child_sw, child_se, child_nw, child_ne]

    def insert(self, loc: Location) -> None:
        """
        QuadNode method that takes a Location and inserts it into the first
        QuadNode contents list attribute that is not at capacity.

        Returns:
        No return
        """
        if len(self.contents) < self.capacity:
            self.contents.append(loc)
        else:
            if not self.children:
                # create children if they don't exist
                self.children = self.create_children()
            for child in self.children:
                # check child node contains Location for insertion
                if child.is_bounding(loc):
                    # recursively call insert on child
                    child.insert(loc)

    def neighbors_of(self, loc: Location, dist: float = 10) -> list:
        """
        QuadNode method returning list of Locations stored in quadtree
        that are within specified distance of given Location loc.

        Parameters:
        loc : Location
            A Location object to compare with locations stored in QuadTree
        dist : float , default = 10
            A distance threshold to determine what Locations within QuadTree
            are neighbors of loc.

        Returns:
        list: A list of Locations that are neighbors of loc.
        """
        near_points = []
        if self.is_bounding(loc, dist):
            for content in self.contents:
                if content.distance(loc) <= dist:
                    near_points.append(content)
            for child in self.children:
                near_points.extend(child.neighbors_of(loc, dist))
        return near_points

"""
Some example usage:

Initialize instances
>>> origin = Location(0, 0, "Origin")
>>> quad = QuadNode(origin, 10, 10, 3)

Generate random points and insert into quadtree
>>> rand_locs = make_rand_locations(100, quad.width, quad.height)
>>> for loc in rand_locs:
...     quad.insert(loc)

Create some known points for comparison
>>> linus = Location(10, 10, 'Linus')
>>> ada = Location(5, 5, 'Ada')
>>> galileo = Location(0, 0, 'Galileo')

Find and print nearby neighbors of each point
>>> print_neighbors(quad, linus, 3)
>>> print_neighbors(quad, ada, 10)
>>> print_neighbors(quad, galileo, 3)

"""
import random

def make_rand_locations(n: int = 100, w: int = 500, h: int = 500) -> list:
    rand_locs = []
    for i in range(0,n):
        rand_locs.append(Location(random.randint(0,w),random.randint(0,h),f'P{i}'))
    return rand_locs

def print_neighbors(quad, loc, dist):
    neighbors = quad.neighbors_of(loc, dist)
    for neighbor in neighbors:
        print(f'{neighbor} is within {dist} of {loc}')