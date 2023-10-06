import sys

"""
The famous Floyd Warshall Alogirthm to
find the shortest distance between all
pairs of given vertices.
Wikipedia link:  https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
"""


def floyd_warshall(adjacency_matrix: list[list[int]], n: int) -> list[list[int]]:
    """
    Given adjacency matrix, returns a matrix with
    shortest distance between each pair of vertices
    >>> floyd_warshall([[-1, 2, 2, -1], [1, 2, 3, -1], [-1, 2, 2, 1], [3, 5, 4, 1]],4)
    [[0, 2, 2, 3], [1, 0, 3, 4], [3, 2, 0, 1], [3, 5, 4, 0]]
    >>> floyd_warshall([[-1, 4, -1, 2], [1, 7, -1, 14], [-1, 2, 4, 9], [10, 5, 1, 2]],4)
    [[0, 4, 3, 2], [1, 0, 4, 3], [3, 2, 0, 5], [4, 3, 1, 0]]
    >>> floyd_warshall([[1, 2], [1, 11]],2)
    [[0, 2], [1, 0]]
    >>> floyd_warshall([[1, 2], [1, 11]],2)
    [[0, 2], [1, 0]]
    """
    shortest_distance = []
    for _ in range(n):
        shortest_distance.append([sys.maxsize] * n)

    if len(adjacency_matrix) == n:
        for row in adjacency_matrix:
            if len(row) != n:
                raise Exception("Incorrect Adjacency matrix")
    else:
        raise Exception("Incorrect Adjacency matrix")

    if n == 0:
        return shortest_distance

    for vertex1 in range(n):
        for vertex2 in range(n):
            if vertex1 == vertex2:
                shortest_distance[vertex1][vertex2] = 0
            elif adjacency_matrix[vertex1][vertex2] >= 0:
                shortest_distance[vertex1][vertex2] = adjacency_matrix[vertex1][vertex2]
    # print(shortest_distance)
    for intermediate_vertex in range(n):
        for vertex1 in range(n):
            for vertex2 in range(n):
                check1=(shortest_distance[vertex1][intermediate_vertex] != sys.maxsize)
                check2=(shortest_distance[intermediate_vertex][vertex2] != sys.maxsize)
                if (check1 and check2):
                    shortest_distance[vertex1][vertex2] = min(
                        shortest_distance[vertex1][vertex2],
                        shortest_distance[vertex1][intermediate_vertex]
                        + shortest_distance[intermediate_vertex][vertex2],
                    )

    for vertex1 in range(n):
        for vertex2 in range(n):
            if shortest_distance[vertex1][vertex2] == sys.maxsize:
                shortest_distance[vertex1][vertex2] = -1

    return shortest_distance


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    total_vertices = 4
    adjacency_matrix = []
    for _ in range(total_vertices):
        row = []
        for __ in range(total_vertices):
            row.append(-1)
        adjacency_matrix.append(row)
    # directed graph
    adjacency_matrix[0][1] = 2
    # vertex 1 can be reached from vertex 0 at cost/distance of 2

    adjacency_matrix[1][0] = 1
    # vertex 0 can be reached from vertex 1 at cost/distance of 1

    adjacency_matrix[1][2] = 3
    # vertex 2 can be reached from vertex 1 at cost/distance of 3

    adjacency_matrix[3][0] = 3
    # vertex 0 can be reached from vertex 3 at cost/distance of 3

    adjacency_matrix[3][1] = 5
    # vertex 1 can be reached from vertex 3 at cost/distance of 5

    adjacency_matrix[3][2] = 4
    # vertex 2 can be reached from vertex 3 at cost/distance of 4

    # print(adjacency_matrix)
    # if matrix[v1][v2] is -1, then v2 can't be reached from v1
    shortest_distance_matrix = floyd_warshall(adjacency_matrix, total_vertices)

    print(shortest_distance_matrix)
