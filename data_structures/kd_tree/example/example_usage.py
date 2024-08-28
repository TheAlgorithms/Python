import numpy as np

from hypercube_points import hypercube_points
from data_structures.kd_tree.build_kdtree import build_kdtree
from data_structures.kd_tree.nearest_neighbour_search import nearest_neighbour_search


num_points = 5000
cube_size = 10
num_dimensions = 10

points = hypercube_points(num_points, cube_size, num_dimensions)
hypercube_kdtree = build_kdtree(points.tolist())

query_point = np.random.rand(num_dimensions).tolist()

nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(hypercube_kdtree, query_point)

print(f"Query point: {query_point}")
print(f"Nearest point: {nearest_point}")
print(f"Distance: {nearest_dist:.4f}")
print(f"Nodes visited: {nodes_visited}")
