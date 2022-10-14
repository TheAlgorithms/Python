"""
Description
    The Koch snowflake is a fractal curve and one of the earliest fractals to
    have been described. The Koch snowflake can be built up iteratively, in a
    sequence of stages. The first stage is an equilateral triangle, and each
    successive stage is formed by adding outward bends to each side of the
    previous stage, making smaller equilateral triangles.
    This can be achieved through the following steps for each line:
        1. divide the line segment into three segments of equal length.
        2. draw an equilateral triangle that has the middle segment from step 1
        as its base and points outward.
        3. remove the line segment that is the base of the triangle from step 2.
    (description adapted from https://en.wikipedia.org/wiki/Koch_snowflake )
    (for a more detailed explanation and an implementation in the
    Processing language, see  https://natureofcode.com/book/chapter-8-fractals/
    #84-the-koch-curve-and-the-arraylist-technique )

Requirements (pip):
    - matplotlib
    - numpy
"""


from __future__ import annotations

import matplotlib.pyplot as plt  # type: ignore
import numpy

# initial triangle of Koch snowflake
VECTOR_1 = numpy.array([0, 0])
VECTOR_2 = numpy.array([0.5, 0.8660254])
VECTOR_3 = numpy.array([1, 0])
INITIAL_VECTORS = [VECTOR_1, VECTOR_2, VECTOR_3, VECTOR_1]

# uncomment for simple Koch curve instead of Koch snowflake
# INITIAL_VECTORS = [VECTOR_1, VECTOR_3]


def iterate(initial_vectors: list[numpy.ndarray], steps: int) -> list[numpy.ndarray]:
    """
    Go through the number of iterations determined by the argument "steps".
    Be careful with high values (above 5) since the time to calculate increases
    exponentially.
    >>> iterate([numpy.array([0, 0]), numpy.array([1, 0])], 1)
    [array([0, 0]), array([0.33333333, 0.        ]), array([0.5       , \
0.28867513]), array([0.66666667, 0.        ]), array([1, 0])]
    """
    vectors = initial_vectors
    for _ in range(steps):
        vectors = iteration_step(vectors)
    return vectors


def iteration_step(vectors: list[numpy.ndarray]) -> list[numpy.ndarray]:
    """
    Loops through each pair of adjacent vectors. Each line between two adjacent
    vectors is divided into 4 segments by adding 3 additional vectors in-between
    the original two vectors. The vector in the middle is constructed through a
    60 degree rotation so it is bent outwards.
    >>> iteration_step([numpy.array([0, 0]), numpy.array([1, 0])])
    [array([0, 0]), array([0.33333333, 0.        ]), array([0.5       , \
0.28867513]), array([0.66666667, 0.        ]), array([1, 0])]
    """
    new_vectors = []
    for i, start_vector in enumerate(vectors[:-1]):
        end_vector = vectors[i + 1]
        new_vectors.append(start_vector)
        difference_vector = end_vector - start_vector
        new_vectors.append(start_vector + difference_vector / 3)
        new_vectors.append(
            start_vector + difference_vector / 3 + rotate(difference_vector / 3, 60)
        )
        new_vectors.append(start_vector + difference_vector * 2 / 3)
    new_vectors.append(vectors[-1])
    return new_vectors


def rotate(vector: numpy.ndarray, angle_in_degrees: float) -> numpy.ndarray:
    """
    Standard rotation of a 2D vector with a rotation matrix
    (see https://en.wikipedia.org/wiki/Rotation_matrix )
    >>> rotate(numpy.array([1, 0]), 60)
    array([0.5      , 0.8660254])
    >>> rotate(numpy.array([1, 0]), 90)
    array([6.123234e-17, 1.000000e+00])
    """
    theta = numpy.radians(angle_in_degrees)
    c, s = numpy.cos(theta), numpy.sin(theta)
    rotation_matrix = numpy.array(((c, -s), (s, c)))
    return numpy.dot(rotation_matrix, vector)


def plot(vectors: list[numpy.ndarray]) -> None:
    """
    Utility function to plot the vectors using matplotlib.pyplot
    No doctest was implemented since this function does not have a return value
    """
    # avoid stretched display of graph
    axes = plt.gca()
    axes.set_aspect("equal")

    # matplotlib.pyplot.plot takes a list of all x-coordinates and a list of all
    # y-coordinates as inputs, which are constructed from the vector-list using
    # zip()
    x_coordinates, y_coordinates = zip(*vectors)
    plt.plot(x_coordinates, y_coordinates)
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    processed_vectors = iterate(INITIAL_VECTORS, 5)
    plot(processed_vectors)
