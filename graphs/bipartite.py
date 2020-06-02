import sys

"""
An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the
graph joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph
is used to model connections between objects of two different types (say, boys and girls; or students and
dormitories).
An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors
(say, black and white) such that the endpoints of each edge have different colors.
"""

"""

Sample 1.

Input:
4 4
1 2
4 1
2 3
3 1
Output:
0

Explaination: This graph is not bipartite. To see this assume that the vertex 1 is colored white.
Then the vertices 2 and 3 should be colored black since the graph contains the edges
{1, 2} and {1, 3}. But then the edge {2, 3} has both endpoints of the same color.

Sample 2.
Input:
5 4
5 2
4 2
3 4
1 4
Output:
1

Explaination: This graph is bipartite: assign the vertices 4 and 5 the white color, assign all the remaining vertices
the black color.

"""


def bipartite(partition: list, adjacent_edges: list) -> int:
    test = 0
    while test < len(partition):
        node = partition[test]
        for i in adjacent_edges[test]:
            if node == 'W':
                if partition[i] == 'W':
                    return 0
            else:
                if partition[i] == 'B':
                    return 0
        test += 1
    return 1


def colour(adjacent_edges):  # Assigning alternative colours to the nodes of the graph
    queue = []
    queue.append(0)
    partition = ['c'] * len(adjacent_edges)
    partition[0] = 'W'
    step = 2
    while queue:
        node = queue.pop(0)
        flag = 0
        for i in adjacent_edges[node]:
            if partition[i] == 'c':
                flag = 1
                queue.append(i)
                if step % 2 == 0:
                    partition[i] = 'B'
                else:
                    partition[i] = 'W'
        if flag == 1:
            step += 1
    return bipartite(partition, adjacent_edges)  # return 1 if the graph is bipartite and 0 otherwise.


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    vertices, no_of_edges, *data = data
    edges = list(zip(data[0:(2 * no_of_edges):2], data[1:(2 * no_of_edges):2]))
    adjacent_edges = [[] for _ in range(vertices)]
    for (a, b) in edges:
        adjacent_edges[a - 1].append(b - 1)
        adjacent_edges[b - 1].append(a - 1)
    print(colour(adjacent_edges))
