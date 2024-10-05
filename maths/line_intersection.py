# Function to calculate determinant of a 2x2 matrix
def determinant(a: float, b: float, c: float, d: float) -> float:
    """
    Calculates the determinant of a 2x2 matrix:

    | a  b |
    | c  d |

    Args:
        a, b, c, d (float): Elements of the 2x2 matrix.

    Returns:
        float: The determinant of the matrix.
    """
    return a * d - c * b


# Function to compute the line equation coefficients from two points
def line_coefficients(p1: list[float] | tuple, p2: list[float] | tuple) -> tuple:
    """
    Computes the coefficients A, B, C of the line equation Ax + By + C = 0
    from two points.

    Args:
        p1 (List[float] | tuple): First point (x, y).
        p2 (List[float] | tuple): Second point (x, y).

    Returns:
        tuple: Coefficients (A, B, C) of the line equation.
    """
    if p1[0] == p2[0]:  # Vertical line
        return 1, 0, p1[0]
    else:  # Non-vertical line
        a = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b = -1
        c = p2[1] - a * p2[0]
        return a, b, c


def segment_intersection(
    v1: list[float] | tuple,
    v2: list[float] | tuple,
    v1_prime: list[float] | tuple,
    v2_prime: list[float] | tuple,
    as_segments: bool = True,
) -> list[float] | None:
    """
    Finds the intersection point of two line segments or lines, if it exists.

    Args:
        v1 (List[float] | tuple): First point of the first segment (x, y).
        v2 (List[float] | tuple): Second point of the first segment (x, y).
        v1_prime (List[float] | tuple): First point of the second segment (x, y).
        v2_prime (List[float] | tuple): Second point of the second segment (x, y).
        as_segments (bool):  treat the inputs as line segments (True) or as infinite lines (False).

    Returns:
        List[float] | None:
            Returns the intersection point [x, y] if the segments/lines intersect, otherwise None.

    References:
        Cramer's rule: https://en.wikipedia.org/wiki/Cramer%27s_rule

    Examples:
        >>> segment_intersection([0, 0], [1, 1], [1, 0], [0, 1])
        [0.5, 0.5]

        # No intersection
        >>> segment_intersection([0, 0], [1, 1], [2, 2], [3, 3]) is None
        True

        # Parallel lines
        >>> segment_intersection([0, 0], [0, 1], [1, 0], [1, 1]) is None
        True

        # Parallel infinite lines (ignoring segment boundaries)
        >>> segment_intersection([0, 0], [1, 1], [2, 2], [3, 3], as_segments=False) is None
        True

        # Intersecting infinite lines
        >>> segment_intersection([0, 0], [1, 1], [1, 0], [0, 1], as_segments=False)
        [0.5, 0.5]
    """

    # Compute line coefficients for the two segments/lines
    a, b, c = line_coefficients(v1, v2)
    a_prime, b_prime, c_prime = line_coefficients(v1_prime, v2_prime)

    # Calculate the determinant (D) of the coefficient matrix
    d = determinant(a, b, a_prime, b_prime)

    if d == 0:
        # If D == 0, the lines are parallel or coincident (no unique solution)
        return None

    # Cramer's rule to solve for x and y
    dx = determinant(-c, b, -c_prime, b_prime)
    dy = determinant(a, -c, a_prime, -c_prime)

    # Intersection point of the lines
    x, y = dx / d, dy / d

    if as_segments:
        # Check if the intersection point lies within the bounds of both line segments
        if (
            min(v1[0], v2[0]) <= x <= max(v1[0], v2[0])
            and min(v1_prime[0], v2_prime[0]) <= x <= max(v1_prime[0], v2_prime[0])
            and min(v1[1], v2[1]) <= y <= max(v1[1], v2[1])
            and min(v1_prime[1], v2_prime[1]) <= y <= max(v1_prime[1], v2_prime[1])
        ):
            return [x, y]

        return None
    else:
        # Return the intersection point of the infinite lines
        return [x, y]
