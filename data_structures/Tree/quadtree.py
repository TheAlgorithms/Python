class Point:
    """Model for points in the 2d map"""

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __sub__(self, other):
        return abs(self.pos_x - other.pos_x) + abs(self.pos_y - other.pos_y)

    def __str__(self):
        return '({}, {})'.format(self.pos_x, self.pos_y)


class QuadNode:
    """Model for quadnode that stores points in 2d map"""

    def __init__(self, top_left_boundary, bottom_right_boundary):
        # Boundary points
        self.top_left_boundary = top_left_boundary
        self.bottom_right_boundary = bottom_right_boundary
        # Point stored in the quad
        self.point = None
        # Children quads
        self.child_top_left = None
        self.child_top_right = None
        self.child_bottom_left = None
        self.child_bottom_right = None


class Map:
    """Model for storing 2d map information"""

    # Map from quadrant markers to attribute name.
    quadrant_to_attribute_map = {
        (0, 0): 'child_bottom_left',
        (0, 1): 'child_top_left',
        (1, 0): 'child_bottom_right',
        (1, 1): 'child_top_right',
    }
    # Map from attribute name to quadrant markers.
    attribute_to_quadrant_map = {
        'child_bottom_left': (0, 0),
        'child_top_left': (0, 1),
        'child_bottom_right': (1, 0),
        'child_top_right': (1, 1),
    }

    def __init__(
        self,
        top_left_boundary_x, top_left_boundary_y,
        bottom_right_boundary_x, bottom_right_boundary_y
    ):
        """Boundary points are required to initialize map"""
        self.top_left_boundary_x = top_left_boundary_x
        self.top_left_boundary_y = top_left_boundary_y
        self.bottom_right_boundary_x = bottom_right_boundary_x
        self.bottom_right_boundary_y = bottom_right_boundary_y
        self.quad = QuadNode(
            top_left_boundary=Point(top_left_boundary_x, top_left_boundary_y),
            bottom_right_boundary=Point(bottom_right_boundary_x, bottom_right_boundary_y),
        )

    def _validate_position(self, pos_x, pos_y):
        """Validates that given position is within boundary of map"""
        if not (
            self.top_left_boundary_x <= pos_x <= self.bottom_right_boundary_x
            and self.top_left_boundary_y >= pos_y >= self.bottom_right_boundary_y
        ):
            raise Exception('Out of boundary')
        return pos_x, pos_y

    def _get_child_quad_attribute_for_point(self, quad, point):
        """Returns name of the attribute of quadrant in which the given point should be in"""
        mid_x = (quad.top_left_boundary.pos_x + quad.bottom_right_boundary.pos_x) // 2
        mid_y = (quad.top_left_boundary.pos_y + quad.bottom_right_boundary.pos_y) // 2
        y_half = 1 if point.pos_y > mid_y else 0
        x_half = 1 if point.pos_x > mid_x else 0
        return self.quadrant_to_attribute_map[(x_half, y_half)]

    def _get_boundary_points_for_child_quadrant(self, quadrant_attribute, top_left_boundary, bottom_right_boundary):
        """Calculates and returns the boundary points for given quad and quadrant-attribute"""
        x_half, y_half = self.attribute_to_quadrant_map[quadrant_attribute]
        mid_x = (top_left_boundary.pos_x + bottom_right_boundary.pos_x) // 2
        mid_y = (top_left_boundary.pos_y + bottom_right_boundary.pos_y) // 2
        child_top_left_boundary = Point(
            top_left_boundary.pos_x if x_half == 0 else mid_x,
            top_left_boundary.pos_y if y_half == 1 else mid_y,
        )
        child_bottom_right_boundary = Point(
            bottom_right_boundary.pos_x if x_half == 1 else mid_x,
            bottom_right_boundary.pos_y if y_half == 0 else mid_y,
        )
        return child_top_left_boundary, child_bottom_right_boundary

    def _create_child_quad_for_point(self, quad, point):
        """Creates a sub quad for given point in given quad."""
        child_quad_attribute_for_point = self._get_child_quad_attribute_for_point(quad, point)
        child_quad = getattr(quad, child_quad_attribute_for_point)
        if not child_quad:
            child_top_left_boundary, child_bottom_right_boundary = self._get_boundary_points_for_child_quadrant(
                child_quad_attribute_for_point, quad.top_left_boundary, quad.bottom_right_boundary
            )
            child_quad = QuadNode(
                top_left_boundary=child_top_left_boundary,
                bottom_right_boundary=child_bottom_right_boundary,
            )
            setattr(quad, child_quad_attribute_for_point, child_quad)
        return child_quad

    def _add_point_util(self, quad, point):
        """A utility recursive function to add point to given quad"""
        if quad.top_left_boundary - quad.bottom_right_boundary <= 2:
            quad.point = point
            return
        if quad.point is None:
            quad.point = point
            return
        else:
            if quad.point != -1:
                child_quad_for_current_point = self._create_child_quad_for_point(quad, quad.point)
                child_quad_for_current_point.point = quad.point
                quad.point = -1
            child_quad = self._create_child_quad_for_point(quad, point)
            self._add_point_util(child_quad, point)

    def add_point(self, pos_x, pos_y):
        """Adds given point to the map"""
        pos_x, pos_y = self._validate_position(pos_x, pos_y)
        point = Point(pos_x, pos_y)
        self._add_point_util(self.quad, point)

    def _search_point_util(self, quad, point):
        """A utility recursive function to search point in given quad"""
        if quad.point is None:
            return None
        else:
            if quad.point != -1:
                if quad.point - point == 0:
                    return quad.point
            child_quad_attribute_for_point = self._get_child_quad_attribute_for_point(quad, point)
            child_quad = getattr(quad, child_quad_attribute_for_point)
            return self._search_point_util(child_quad, point) if child_quad else None

    def search_point(self, pos_x, pos_y):
        """Finds the point in the map with given position"""
        pos_x, pos_y = self._validate_position(pos_x, pos_y)
        return self._search_point_util(self.quad, Point(pos_x, pos_y))
