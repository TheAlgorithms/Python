##################### -- Learning Source -- #####################

# 1. https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# 2. https://www.educative.io/answers/what-is-uniform-cost-search

# In above 1 no. link, you will get about dijkstra algorithm.
# You may have to scroll down a little bit.
# And you will get a section titled as "Practical optimizations and infinite graphs"
# This section explains about Uniform Cost Search algorithm.

# Uniform search cost is slightly similar to dijkstra.
# The main different between them is that UCS is having multiple goals.

# Below code is fully based on graph node environment
##################### --------------------- #####################


def ucs(
    graph_data: list[list[int]],
    distance: dict[
        tuple[
            int,
            int,
        ],
        int,
    ],
    goal: list[int],
    start: int,
) -> list[int]:
    """
    Returns a list of integer values which are result of optimal distance
    >>> graph_data = [[1, 2], [2, 3], [4], [4, 5], [6], [6], [], []]
    >>> distance = {(0, 1): 2, (0, 2): 1, (1, 2): 5, (1, 3): 10, (2, 4): 3, (3, 4): 2,
    (3, 5): 1, (4, 6): 4, (5, 6): 3}
    >>> goal = [6]
    >>> start = 0
    >>> ucs(graph_data, distance, goal, start)
    8
    """
    # priority queue
    heap = []
    goal_answer = []
    # Goal result to be max value initially
    for _ in range(len(goal)):
        goal_answer.append(10**8)

    # Store the starting node
    heap.append([0, start])

    # store tracks of visited nodes
    visited = {}
    final_cnt = 0
    while len(heap) > 0:
        heap = sorted(heap)
        # get the top element of the node list which has less distance value
        current_node = heap[-1]
        del heap[-1]
        current_node[0] *= -1

        # check current node is part of the goal list
        if current_node[1] in goal:
            index = goal.index(current_node[1])
            # new goal is reached or not
            if goal_answer[index] == 10**8:
                final_cnt += 1
            # if the distance is less
            if goal_answer[index] > current_node[0]:
                goal_answer[index] = current_node[0]
            # pop the element
            del heap[-1]
            heap = sorted(heap)
            # if it crosses all goals
            if final_cnt == len(goal):
                return goal_answer
        # explore new unvisited node
        if current_node[1] not in visited:
            for i in range(len(graph_data[current_node[1]])):
                # The value is negated to ensure that
                # the node with the lowest priority is placed at the top.
                heap.append(
                    [
                        (
                            current_node[0]
                            + distance[
                                (current_node[1], graph_data[current_node[1]][i])
                            ]
                        )
                        * -1,
                        graph_data[current_node[1]][i],
                    ]
                )
        visited[current_node[1]] = 1

    return goal_answer


def run() -> None:
    # start: 0, goal: 6; Distance(Minimum/Lowest): 8:
    """
    Return nothing and prints only the output
    >>> run()
    start: 0, goal: 6; Distance(Minimum/Lowest): 8
    """
    # create the graph_data
    graph_data = [[] for _ in range(8)]  # type: list[list[int]]

    # Node to node edges
    graph_data[0].append(1)
    graph_data[0].append(2)
    graph_data[1].append(2)
    graph_data[1].append(3)
    graph_data[2].append(4)
    graph_data[3].append(4)
    graph_data[3].append(5)
    graph_data[4].append(6)
    graph_data[5].append(6)

    # Distance for the edges one node to another node
    distance = {
        (0, 1): 2,
        (0, 2): 1,
        (1, 2): 5,
        (1, 3): 10,
        (2, 4): 3,
        (3, 4): 2,
        (3, 5): 1,
        (4, 6): 4,
        (5, 6): 3,
    }

    goal = []

    # Multiple goal states as uniform search distance feature
    goal.append(6)

    # get the final result
    result = ucs(graph_data, distance, goal, 0)

    print("start: 0, goal: 6; Distance(Minimum/Lowest):", result[0])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
