# Author: Phyllipe Bezerra (https://github.com/pmba)

clothes = {
    0: "underwear",
    1: "pants",
    2: "belt",
    3: "suit",
    4: "shoe",
    5: "socks",
    6: "shirt",
    7: "tie",
    8: "watch",
}

graph = [[1, 4], [2, 4], [3], [], [], [4], [2, 7], [3], []]

visited = [0 for x in range(len(graph))]
stack = []


def print_stack(stack, clothes):
    order = 1
    while stack:
        current_clothing = stack.pop()
        print(order, clothes[current_clothing])
        order += 1


def depth_first_search(u, visited, graph):
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            depth_first_search(v, visited, graph)

    stack.append(u)


def topological_sort(graph, visited):
    for v in range(len(graph)):
        if not visited[v]:
            depth_first_search(v, visited, graph)


if __name__ == "__main__":
    topological_sort(graph, visited)
    print(stack)
    print_stack(stack, clothes)
