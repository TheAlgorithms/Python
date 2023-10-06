import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from typing import List, Tuple


def create_3d_cube(vertices: List[Tuple[float, float, float]], faces: List[List[int]]) -> None:
    """
    Create a 3D cube using Matplotlib.

    Args:
        vertices (List[Tuple[float, float, float]]): List of 8 (x, y, z) vertex coordinates.
        faces (List[List[int]]): List of 12 face definitions, where each face is a list of 4 vertex indices.

    Example:
        >>> vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
        >>> faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 3, 7, 4), (1, 2, 6, 5), (0, 1, 5, 4), (2, 3, 7, 6)]
        >>> create_3d_cube(vertices, faces)  # doctest: +SKIP
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create a Poly3DCollection
    cube = [[vertices[iv] for iv in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(cube, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Remove axis labels and markings
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')
    ax.grid(False)

    plt.title('3D Cube')
    plt.show()


if __name__ == "__main__":
    # Define vertices and faces for a 3D cube
    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
                (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
    faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 3, 7, 4), (1, 2, 6, 5),
             (0, 1, 5, 4), (2, 3, 7, 6)]

    # Create and display the 3D cube
    create_3d_cube(vertices, faces)

    # Use doctest to test the function
    import doctest

    result = doctest.testmod(verbose=True)

    if result.failed == 0:
        print("All tests passed!")
    else:
        print(f"{result.failed} test(s) failed.")
