import numpy as np
from typing import List
from hypercube_points import hypercube_points
from data_structures.kd_tree.build_kdtree import build_kdtree
from data_structures.kd_tree.nearest_neighbour_search import nearest_neighbour_search

def main() -> None:
    """
    Demonstrates the use of KD-Tree by building it from random points
    in a 10-dimensional hypercube and performing a nearest neighbor search.
    """
    num_points: int = 5000
    cube_size: int = 10
    num_dimensions: int = 10

    # Generate random points within the hypercube
    points: np.ndarray = hypercube_points(num_points, cube_size, num_dimensions)
    hypercube_kdtree = build_kdtree(points.tolist())

    # Generate a random query point within the same space
    rng = np.random.default_rng()
    query_point: List[float] = rng.random(num_dimensions).tolist()

    # Perform nearest neighbor search
    nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(
        hypercube_kdtree, query_point
    )

    # Print the results
    print(f"Query point: {query_point}")
    print(f"Nearest point: {nearest_point}")
    print(f"Distance: {nearest_dist:.4f}")
    print(f"Nodes visited: {nodes_visited}")

if __name__ == "__main__":
    main()
