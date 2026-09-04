# Function to calculate determinant of a 2x2 matrix
def determinant(m00: float, m01: float, m10: float, m11: float) -> float:
    """
    Calculates the determinant of a 2x2 matrix:

    | m00  m01 |
    | m10  m11 |

    Args:
        m00 (float): Element in the first row, first column.
        m01 (float): Element in the first row, second column.
        m10 (float): Element in the second row, first column.
        m11 (float): Element in the second row, second column.

    Returns:
        float: The determinant of the matrix.

    Examples:
        # Determinant of the identity matrix (should be 1)
        >>> determinant(1, 0, 0, 1)
        1

        # Determinant of a matrix with two equal rows (should be 0)
        >>> determinant(1, 2, 1, 2)
        0

        # Determinant of a matrix with a negative determinant
        >>> determinant(1, 2, 3, 4)
        -2

        # Determinant of a matrix with larger numbers
        >>> determinant(10, 20, 30, 40)
        -200
    """
    return m00 * m11 - m10 * m01


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

    Examples:
        # Vertical line (x = constant)
        >>> line_coefficients([1, 0], [1, 2])
        (1, 0, 1)

        # Horizontal line (y = constant)
        >>> line_coefficients([0, 1], [2, 1])
        (0.0, -1, 1.0)

        # Diagonal line (positive slope)
        >>> line_coefficients([0, 0], [1, 1])
        (1.0, -1, 0.0)

        # Diagonal line (negative slope)
        >>> line_coefficients([0, 1], [1, 0])
        (-1.0, -1, 1.0)
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
        as_segments (bool):
            treat the inputs as line segments (True)
            or as infinite lines (False).

    Returns:
        List[float] | None:
            Returns the intersection point [x, y] if existent, otherwise None.

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

        # Intersecting infinite lines
        >>> segment_intersection([0, 0], [1, 1], [1, 0], [0, 1], as_segments=False)
        [0.5, 0.5]

        # Parallel infinite lines (ignoring segment boundaries)
        >>> segment_intersection([0, 0], [1, 1], [2, 2], [3, 3], False) is None
        True
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
