def nearest_neighbour_search(root, query_point):
    nearest_point = None
    nearest_dist = float('inf')
    nodes_visited = 0

    def search(node, depth=0):
        nonlocal nearest_point, nearest_dist, nodes_visited
        if node is None:
            return

        nodes_visited += 1

        # Calculate the current distance (squared distance)
        current_point = node.point
        current_dist = sum((qp - cp) ** 2 for qp, cp in zip(query_point, current_point))

        # Update nearest point if the current node is closer
        if nearest_point is None or current_dist < nearest_dist:
            nearest_point = current_point
            nearest_dist = current_dist

        # Determine which subtree to search first (based on axis and query point)
        k = len(query_point)  # dimensionality of points
        axis = depth % k

        if query_point[axis] <= current_point[axis]:
            nearer_subtree = node.left
            further_subtree = node.right
        else:
            nearer_subtree = node.right
            further_subtree = node.left

        # Search the nearer subtree first
        search(nearer_subtree, depth + 1)

        # If the further subtree has a closer point
        if (query_point[axis] - current_point[axis]) ** 2 < nearest_dist:
            search(further_subtree, depth + 1)

    search(root, 0)
    return nearest_point, nearest_dist, nodes_visited
